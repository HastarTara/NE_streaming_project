import requests
from config import GUARDIAN_API_KEY, GUARDIAN_API_URL


def fetch_guardian_articles(query="technology", page_size=5):
    """Fetch articles from The Guardian API based on a search query"""
    params = {
        "q": query,
        "api-key": GUARDIAN_API_KEY,
        "page-size": page_size,
        "format": "json",
    }
    print("API KEY:", GUARDIAN_API_KEY)
    response = requests.get(GUARDIAN_API_URL, params=params)

    if response.status_code == 200:
        return response.json().get("response", {}).get("results", [])
    else:
        raise Exception(
            f"Error fetching articles: {response.status_code} {response.text}"
        )


if __name__ == "__main__":
    articles = fetch_guardian_articles()
    for article in articles:
        print(f"{article['webTitle']} - {article['webUrl']}")
