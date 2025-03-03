import boto3
import time
from decimal import Decimal
from config import MAX_REQUESTS_PER_DAY

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = "request_tracker"


# Check if table exists, if not, create it
def create_table_if_not_exists():
    existing_tables = dynamodb.meta.client.list_tables()["TableNames"]
    if TABLE_NAME not in existing_tables:
        table = dynamodb.meta.client.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
        )
        print(f"Creating DynamoDB table {TABLE_NAME}...")
        waiter = dynamodb.meta.client.get_waiter("table_exists")
        waiter.wait(TableName=TABLE_NAME)


# Load request count from DynamoDB
def load_request_count():
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={"id": "guardian_requests"})
    item = response.get("Item")

    if item:
        timestamp = float(item["timestamp"])
        if time.time() - timestamp < 86400:  # If within 24 hours
            return item["count"]

    return 0  # Reset count if past 24 hours


# Save updated request count
def save_request_count(count):
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            "id": "guardian_requests",
            "count": count,
            "timestamp": Decimal(str(time.time())),
        }
    )


# Function to check if a request can be made
def can_make_request():
    create_table_if_not_exists()  # Ensure table exists
    count = load_request_count()

    if count >= MAX_REQUESTS_PER_DAY:
        print("Daily request limit reached. Try again tomorrow.")
        return False

    save_request_count(count + 1)  # Increment and save count
    return True
