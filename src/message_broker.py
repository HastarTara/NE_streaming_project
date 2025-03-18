from config import (
    SQS_QUEUE_URL,
    MESSAGE_TTL_DAYS,
    BROKER_TYPE,
    KAFKA_TOPIC,
)
import boto3
from kafka import KafkaProducer
import botocore.exceptions


class SQSBroker:
    """SQS implementation of the message broker."""

    def __init__(self):
        self.message_ttl_days = MESSAGE_TTL_DAYS
        self.sqs = boto3.client(
            "sqs", region_name="eu-west-2"
        )  # Ensure region is correct

        # If queue URL is provided, use it; otherwise, create a new queue
        self.queue_url = SQS_QUEUE_URL or self.create_queue_if_not_exists()

    def create_queue_if_not_exists(self):
        """Create a new SQS queue if it doesn't exist and return its URL."""
        try:
            response = self.sqs.get_queue_url(QueueName="guardian_content_queue")
            return response["QueueUrl"]
        except botocore.exceptions.ClientError as e:
            error_code = e.response.get("Error", {}).get("Code")
            if error_code == "AWS.SimpleQueueService.NonExistentQueue":
                try:
                    ttl_in_seconds = (
                        self.message_ttl_days * 24 * 60 * 60
                    )  # TTL in seconds
                    response = self.sqs.create_queue(
                        QueueName="guardian_content_queue",
                        Attributes={"MessageRetentionPeriod": str(ttl_in_seconds)},
                    )
                    return response["QueueUrl"]
                except Exception as e:
                    raise e
            else:
                raise  # Re-raise unexpected errors

    def send_message(self, message):
        try:
            response = self.sqs.send_message(
                QueueUrl=self.queue_url, MessageBody=message
            )
            return response["MessageId"]
        except Exception as e:
            raise e


class KafkaBroker:
    """Kafka implementation of the message broker."""

    def __init__(self, topic):
        # Use KAFKA_BROKER_URL and KAFKA_TOPIC from the config
        self.producer = KafkaProducer(
            bootstrap_servers="localhost:9092",
            # change back to localhost:9092
            value_serializer=lambda v: v.encode("utf-8"),
        )
        self.topic = topic

    def send_message(self, message):
        # Send the message to the Kafka topic
        self.producer.send(self.topic, message)
        self.producer.flush()  # Ensure the message is sent before returning
        return "Message sent to Kafka"


def get_broker():
    """Factory method to return the correct broker based
    on environment variable."""
    if BROKER_TYPE == "sqs":
        return SQSBroker()  # SQS will handle queue creation if it doesn't exist
    elif BROKER_TYPE == "kafka":
        # Use KAFKA_TOPIC from the config to dynamically select the Kafka topic
        return KafkaBroker(KAFKA_TOPIC)
    else:
        raise ValueError(f"Unknown BROKER_TYPE: {BROKER_TYPE}")
