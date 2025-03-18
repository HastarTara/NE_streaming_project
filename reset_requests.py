import boto3
from decimal import Decimal
import time

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = "request_tracker"


def reset_request_count():
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            "id": "guardian_requests",
            "count": 0,
            "timestamp": Decimal(str(time.time())),  # Reset timestamp
        }
    )
    print("✅ Request count reset successfully.")


if __name__ == "__main__":
    reset_request_count()
