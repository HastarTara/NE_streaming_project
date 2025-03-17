import unittest
from unittest.mock import patch, MagicMock
from message_broker import SQSBroker, KafkaBroker, get_broker
import botocore.exceptions


class TestSQSBroker(unittest.TestCase):

    @patch("boto3.client")
    def test_send_message(self, mock_boto_client):
        # Mocking the SQS client and its methods
        mock_sqs = MagicMock()
        mock_boto_client.return_value = mock_sqs

        broker = SQSBroker()
        mock_sqs.send_message.return_value = {"MessageId": "12345"}

        # Test the send_message method
        response = broker.send_message("Test message")
        self.assertEqual(response, "12345")
        mock_sqs.send_message.assert_called_with(
            QueueUrl=broker.queue_url, MessageBody="Test message"
        )

    @patch("boto3.client")
    def test_create_queue_if_not_exists(self, mock_boto_client):
        # Mock the SQS client
        mock_sqs = MagicMock()
        mock_boto_client.return_value = mock_sqs

        # Simulating a "QueueDoesNotExist" exception properly
        mock_sqs.get_queue_url.side_effect = botocore.exceptions.ClientError(
            {
                "Error": {
                    "Code": "AWS.SimpleQueueService.NonExistentQueue",
                    "Message": "Queue does not exist",
                }
            },
            "GetQueueUrl",
        )

        # Simulate successful queue creation
        mock_sqs.create_queue.return_value = {
            "QueueUrl": "https://sqs.example.com/12345"
        }

        broker = SQSBroker()
        queue_url = broker.create_queue_if_not_exists()

        # Assert the expected queue URL is returned
        self.assertEqual(queue_url, "https://sqs.example.com/12345")


class TestKafkaBroker(unittest.TestCase):
    @patch("message_broker.KafkaProducer")
    def test_send_message(self, mock_kafka_producer):
        # Create a MagicMock instance for the producer mock
        mock_producer = MagicMock()
        mock_kafka_producer.return_value = mock_producer  # Ensure the mock
        #  producer is returned when KafkaProducer is instantiated

        # Instantiate the broker (which will use the mocked KafkaProducer)
        broker = KafkaBroker("test-topic")

        # Test the send_message method
        response = broker.send_message("Test message")

        # Assertions
        self.assertEqual(response, "Message sent to Kafka")

        # Print to check if the send method was called
        print(
            mock_producer.send.call_args_list
        )  # This will show the actual call arguments

        # Ensure the send method was called with the correct arguments
        mock_producer.send.assert_called_with("test-topic", "Test message")

        # Ensure flush was called to simulate Kafka's behavior after
        # sending the message
        mock_producer.flush.assert_called()


class TestGetBroker(unittest.TestCase):

    @patch("message_broker.BROKER_TYPE", "sqs")
    def test_get_broker_sqs(self):
        broker = get_broker()
        self.assertIsInstance(broker, SQSBroker)

    @patch("message_broker.BROKER_TYPE", "kafka")
    @patch("message_broker.KafkaProducer")  # Mock KafkaProducer here
    def test_get_broker_kafka(self, mock_kafka_producer):
        # Mock the KafkaProducer return value to prevent actual
        # Kafka connection
        mock_kafka_producer.return_value = MagicMock()

        broker = get_broker()
        self.assertIsInstance(broker, KafkaBroker)

    @patch("message_broker.BROKER_TYPE", "unknown")
    def test_get_broker_invalid(self):
        with self.assertRaises(ValueError):
            get_broker()
