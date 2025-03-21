import requests
from config import GUARDIAN_API_KEY, GUARDIAN_API_URL
from rate_limiter import can_make_request


def fetch_guardian_articles(query, page_size):
    if not can_make_request():  # Check before making a request
        return []
    """Fetch articles from The Guardian API based on a search query"""
    params = {
        "q": query,
        "api-key": GUARDIAN_API_KEY,
        "page-size": page_size,
        "format": "json",
    }
    response = requests.get(GUARDIAN_API_URL, params=params)

    if response.status_code == 200:
        return response.json().get("response", {}).get("results", [])
    else:
        raise Exception(
            f"Error fetching articles: {response.status_code} {response.text}"
        )
