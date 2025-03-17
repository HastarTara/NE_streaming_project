import pytest
from unittest.mock import patch, MagicMock
from lambda_handler import lambda_handler
import json  # Add this import for json.loads


@pytest.fixture
def mock_articles():
    return [
        {
            "webPublicationDate": "2024-11-21T11:11:31Z",
            "webTitle": "Example Article",
            "webUrl": "https://www.theguardian.com/example",
        }
    ]


@patch("lambda_handler.fetch_guardian_articles")
@patch("lambda_handler.get_broker")
def test_lambda_handler(
    mock_get_broker, mock_fetch_guardian_articles, mock_articles
):
    # Mock the articles that the fetch_guardian_articles function will return
    mock_fetch_guardian_articles.return_value = mock_articles

    # Mock the broker
    mock_broker = MagicMock()
    mock_get_broker.return_value = mock_broker

    # Simulate the event that would trigger the Lambda function
    event = {"query": "machine learning", "date_from": "2025-01-01"}

    # Call the Lambda handler function
    response = lambda_handler(event, None)

    # Parse the response body as it's returned as a JSON string
    body = json.loads(response["body"])

    # Check for correct status code
    assert response["statusCode"] == 200

    # Check that the response contains the expected keys
    assert "message" in body
    assert "count" in body

    # Check that the response message is as expected
    assert body["message"] == "Articles sent successfully"

    # Check that the count matches the number of articles
    assert body["count"] == len(mock_articles)

    # Verify that the fetch_guardian_articles was called with
    #  the correct parameters
    mock_fetch_guardian_articles.assert_called_with(
        query="machine learning", page_size=10
    )

    # Verify that the send_message function was called for each article
    assert mock_broker.send_message.call_count == len(mock_articles)
