from config import SQS_QUEUE_URL, MESSAGE_TTL_DAYS, BROKER_TYPE
import boto3
from kafka import KafkaProducer


class MessageBroker:
    """Abstract message broker interface."""

    def send_message(self, message):
        raise NotImplementedError


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
        except self.sqs.exceptions.QueueDoesNotExist:
            try:
                ttl_in_seconds = self.message_ttl_days * 24 * 60 * 60  # TTL in seconds
                response = self.sqs.create_queue(
                    QueueName="guardian_content_queue",
                    Attributes={"MessageRetentionPeriod": str(ttl_in_seconds)},
                )
                return response["QueueUrl"]
            except Exception as e:
                raise

    def send_message(self, message):
        try:
            response = self.sqs.send_message(
                QueueUrl=self.queue_url, MessageBody=message
            )
            return response["MessageId"]
        except Exception as e:
            raise


class KafkaBroker(MessageBroker):
    """Kafka implementation of the message broker."""

    def __init__(self, topic):
        self.producer = KafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v: v.encode("utf-8"),
        )
        self.topic = topic

    def send_message(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()
        return "Message sent to Kafka"


def get_broker():
    """Factory method to return the correct broker based on environment variable."""
    if BROKER_TYPE == "sqs":
        return SQSBroker()  # SQS will handle queue creation if it doesn't exist
    elif BROKER_TYPE == "kafka":
        return KafkaBroker("default-topic")
    else:
        raise ValueError(f"Unknown BROKER_TYPE: {BROKER_TYPE}")
