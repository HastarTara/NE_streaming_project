from config import SQS_QUEUE_URL, MESSAGE_TTL_DAYS, BROKER_TYPE
import boto3
from kafka import KafkaProducer
import logging


class MessageBroker:
    """Abstract message broker interface."""

    def send_message(self, message):
        raise NotImplementedError


import os
import boto3
import logging
from config import SQS_QUEUE_URL, MESSAGE_TTL_DAYS


class SQSBroker:
    """SQS implementation of the message broker."""

    def __init__(self):
        self.message_ttl_days = MESSAGE_TTL_DAYS
        self.sqs = boto3.client(
            "sqs", region_name="eu-west-2"
        )  # Ensure region is correct

        # If queue URL is provided, use it; otherwise, create a new queue
        self.queue_url = SQS_QUEUE_URL or self.create_queue_if_not_exists()

        # Set the TTL to the value from config.py (default to 3 days if not set)

        # Setup logging (if necessary)
        logging.basicConfig(level=logging.INFO)

    def create_queue_if_not_exists(self):
        """Create a new SQS queue if it doesn't exist and return its URL."""
        try:
            logging.info("Checking if the SQS queue exists...")
            response = self.sqs.get_queue_url(QueueName="guardian_content_queue")
            logging.info(f"Queue exists: {response['QueueUrl']}")
            return response["QueueUrl"]
        except self.sqs.exceptions.QueueDoesNotExist:
            logging.info("Queue does not exist. Creating the queue...")
            ttl_in_seconds = self.message_ttl_days * 24 * 60 * 60  # TTL in seconds
            try:
                response = self.sqs.create_queue(
                    QueueName="guardian_content_queue",
                    Attributes={"MessageRetentionPeriod": str(ttl_in_seconds)},
                )
                logging.info(f"Queue created successfully: {response['QueueUrl']}")
                return response["QueueUrl"]
            except Exception as e:
                logging.error(f"Error creating the queue: {e}")
                raise

    def send_message(self, message):
        try:
            logging.info(f"Sending message: {message}")
            response = self.sqs.send_message(
                QueueUrl=self.queue_url, MessageBody=message
            )
            logging.info(f"Message sent successfully: {response['MessageId']}")
            return response["MessageId"]
        except Exception as e:
            logging.error(f"Error sending message: {e}")
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
