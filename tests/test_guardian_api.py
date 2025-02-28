import pytest
from unittest.mock import patch, MagicMock
from guardian_api import fetch_guardian_articles


# Test for successful article fetch
@patch("guardian_api.requests.get")
@patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key")
def test_fetch_guardian_articles_success(mock_get):
    # Mock the value of GUARDIAN_API_KEY in the config dictionary
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "response": {
            "results": [
                {"webTitle": "Article 1", "webUrl": "http://example.com/1"},
                {"webTitle": "Article 2", "webUrl": "http://example.com/2"},
            ]
        }
    }
    mock_get.return_value = mock_response

    # Call the function
    result = fetch_guardian_articles(query="technology", page_size=2)

    # Assert that the mock was called with the correct parameters
    mock_get.assert_called_once_with(
        "https://content.guardianapis.com/search",
        params={
            "q": "technology",
            "api-key": "mocked-api-key",
            "page-size": 2,
            "format": "json",
        },
    )

    # Assert the returned result is as expected
    assert len(result) == 2

    assert result[0]["webTitle"] == "Article 1"
    assert result[1]["webUrl"] == "http://example.com/2"


# Test for error response (non-200 status code)
@patch("guardian_api.requests.get")
@patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key")
def test_fetch_guardian_articles_error(mock_get):
    # Mock the error response from the API
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_get.return_value = mock_response

    # Call the function and check if it raises an exception
    with pytest.raises(
        Exception, match="Error fetching articles: 500 Internal Server Error"
    ):
        fetch_guardian_articles(query="technology", page_size=2)


# Test for handling no results
@patch("guardian_api.requests.get")
@patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key")
def test_fetch_guardian_articles_no_results(mock_get):
    # Mock the response with no articles
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"response": {"results": []}}
    mock_get.return_value = mock_response

    # Call the function
    result = fetch_guardian_articles(query="technology", page_size=2)

    # Assert the result is an empty list
    assert result == []


# Test for default behavior (no query, no page_size passed)
@patch("guardian_api.requests.get")
@patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key")
def test_fetch_guardian_articles_default_params(mock_get):
    # Mock the response from the API
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "response": {
            "results": [
                {"webTitle": "Default Article", "webUrl": "http://example.com/default"}
            ]
        }
    }
    mock_get.return_value = mock_response

    # Call the function with default parameters
    result = fetch_guardian_articles()

    # Assert that the mock was called with the default parameters
    mock_get.assert_called_once_with(
        "https://content.guardianapis.com/search",
        params={
            "q": "technology",
            "api-key": "mocked-api-key",
            "page-size": 5,
            "format": "json",
        },
    )

    # Assert the returned result is as expected
    assert len(result) == 1
    assert result[0]["webTitle"] == "Default Article"
