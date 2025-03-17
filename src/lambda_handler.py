import json
from guardian_api import fetch_guardian_articles
from message_broker import get_broker


def lambda_handler(event, context):
    """AWS Lambda entry point to fetch articles and
    send them to a message broker."""

    query = event.get("query", "technology")
    # date_from = event.get("date_from", None)
    page_size = event.get("page_size", 10)

    articles = fetch_guardian_articles(query=query, page_size=page_size)

    messages = []
    for article in articles[:10]:
        message = {
            "webPublicationDate": article.get("webPublicationDate"),
            "webTitle": article.get("webTitle"),
            "webUrl": article.get("webUrl"),
        }
        messages.append(json.dumps(message))

    broker = get_broker()

    for msg in messages:
        broker.send_message(msg)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Articles sent successfully", "count": len(messages)}
        ),
    }
