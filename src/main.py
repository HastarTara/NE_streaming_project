import argparse
from guardian_api import fetch_guardian_articles
from message_broker import get_broker
from config import BROKER_TYPE


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Guardian articles and publish to a message broker."
    )
    parser.add_argument(
        "query", type=str, help="Search query for Guardian articles"
    )
    parser.add_argument(
        "--page-size", type=int, default=5, help="Number of articles to fetch"
    )
    args = parser.parse_args()

    articles = fetch_guardian_articles(
        query=args.query, page_size=args.page_size
    )

    broker = get_broker()

    for article in articles:
        message = article["webTitle"]
        broker.send_message(message)

    print(f"Sent {len(articles)} messages to {BROKER_TYPE}.")


if __name__ == "__main__":
    main()
