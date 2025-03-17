import pytest
from unittest.mock import patch, MagicMock
from guardian_api import fetch_guardian_articles


# Test for successful article fetch
@patch("guardian_api.requests.get")
@patch("guardian_api.can_make_request", return_value=True)
def test_fetch_guardian_articles_success(mock_can_request, mock_get):
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

    with patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key"):
        result = fetch_guardian_articles(query="technology", page_size=2)

    mock_get.assert_called_once_with(
        "https://content.guardianapis.com/search",
        params={
            "q": "technology",
            "api-key": "mocked-api-key",
            "page-size": 2,
            "format": "json",
        },
    )

    assert len(result) == 2
    assert result[0]["webTitle"] == "Article 1"
    assert result[1]["webUrl"] == "http://example.com/2"


# Test for error response (non-200 status code)
@patch("guardian_api.requests.get")
@patch("guardian_api.can_make_request", return_value=True)
def test_fetch_guardian_articles_error(mock_can_request, mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_get.return_value = mock_response

    with patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key"):
        with pytest.raises(
            Exception,
            match="Error fetching articles: 500 Internal Server Error",
        ):
            fetch_guardian_articles(query="technology", page_size=2)


# Test for handling no results
@patch("guardian_api.requests.get")
@patch("guardian_api.can_make_request", return_value=True)
def test_fetch_guardian_articles_no_results(mock_can_request, mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"response": {"results": []}}
    mock_get.return_value = mock_response

    with patch("guardian_api.GUARDIAN_API_KEY", "mocked-api-key"):
        result = fetch_guardian_articles(query="technology", page_size=2)

    assert result == []


# Test when rate limiter denies the request
@patch("guardian_api.can_make_request", return_value=False)
def test_fetch_guardian_articles_rate_limit(mock_can_request):
    result = fetch_guardian_articles(query="technology", page_size=2)
    assert result == []  # No request should be made


# Test with incorrect params (function should require query & page_size)
def test_fetch_guardian_articles_missing_params():
    with pytest.raises(TypeError):
        fetch_guardian_articles()  # Should fail due to missing arguments
