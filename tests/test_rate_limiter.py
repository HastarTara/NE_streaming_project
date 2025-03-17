import pytest
from unittest.mock import patch, MagicMock
from rate_limiter import (
    can_make_request,
    load_request_count,
    save_request_count,
    create_table_if_not_exists,
)


@pytest.fixture
def mock_dynamodb():
    with patch("rate_limiter.dynamodb") as mock_db:
        mock_table = MagicMock()
        mock_db.Table.return_value = mock_table
        yield mock_table


def test_create_table_if_not_exists(mock_dynamodb):
    with patch(
        "rate_limiter.dynamodb.meta.client.list_tables",
        return_value={"TableNames": []},
    ):
        with patch(
            "rate_limiter.dynamodb.meta.client.create_table"
        ) as mock_create:
            with patch(
                "rate_limiter.dynamodb.meta.client.get_waiter"
            ) as mock_waiter:
                create_table_if_not_exists()
                mock_create.assert_called_once()
                mock_waiter.return_value.wait.assert_called_once()


def test_load_request_count(mock_dynamodb):
    mock_dynamodb.get_item.return_value = {
        "Item": {"count": 10, "timestamp": "1700000000"}
    }

    with patch("time.time", return_value=1700000500):  # Within 24 hours
        assert load_request_count() == 10

    with patch("time.time", return_value=1700864000):  # After 24 hours
        assert load_request_count() == 0  # Should reset


def test_save_request_count(mock_dynamodb):
    with patch("time.time", return_value=1700000000):
        save_request_count(5)
        mock_dynamodb.put_item.assert_called_once_with(
            Item={
                "id": "guardian_requests",
                "count": 5,
                "timestamp": 1700000000,
            }
        )


def test_can_make_request(mock_dynamodb):
    with patch("rate_limiter.MAX_REQUESTS_PER_DAY", 5):
        with patch("rate_limiter.load_request_count", return_value=4):
            with patch("rate_limiter.save_request_count") as mock_save:
                assert can_make_request() is True
                mock_save.assert_called_once_with(5)

        with patch("rate_limiter.load_request_count", return_value=5):
            assert (
                can_make_request() is False
            )  # Should deny request when limit is reached
