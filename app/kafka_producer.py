import json
from kafka import KafkaProducer
import logging

KAFKA_BOOTSTRAP = "kafka:9092"
TOPIC_NAME = "iot.sensors"

logger = logging.getLogger("broker-service")


def get_producer():
    """Creates a Kafka producer instance."""
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )


def send_message(message: dict):
    """Sends a JSON message to Kafka."""
    try:
        producer = get_producer()
        producer.send(TOPIC_NAME, message)
        producer.flush()
        logger.info(f"Message sent to Kafka: {message}")
    except Exception as e:
        logger.error(f"Error sending message: {e}")
