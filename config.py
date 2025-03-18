import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# API settings
GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")
GUARDIAN_API_URL = os.getenv("GUARDIAN_API_URL")


# Message broker settings
BROKER_TYPE = os.getenv("BROKER_TYPE", "sqs")  # Default to SQS
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
KAFKA_BROKER_URL = os.getenv("KAFKA_LOCAL_IP")
# Append ":9092" if it's missing
if KAFKA_BROKER_URL and not KAFKA_BROKER_URL.endswith(":9092"):
    KAFKA_BROKER_URL += ":9092"

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# Performance limits
MAX_REQUESTS_PER_DAY = int(os.getenv("MAX_REQUESTS_PER_DAY", 50))
MESSAGE_TTL_DAYS = int(os.getenv("MESSAGE_TTL_DAYS", 3))  # Days before messages expire
