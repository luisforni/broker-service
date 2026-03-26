from kafka.admin import KafkaAdminClient, NewTopic
import logging
import time

KAFKA_BOOTSTRAP = "kafka:9092"
TOPIC_NAME = "iot.sensors"

logger = logging.getLogger("broker-service")


def create_topic():
    """Creates Kafka topic if it does not exist."""
    admin = None

    # Kafka tarda unos segundos en estar disponible
    for _ in range(10):
        try:
            admin = KafkaAdminClient(bootstrap_servers=KAFKA_BOOTSTRAP)
            break
        except Exception:
            logger.warning("Kafka not ready, retrying...")
            time.sleep(3)

    if admin is None:
        logger.error("Kafka is not reachable")
        return

    try:
        topics = admin.list_topics()
        if TOPIC_NAME not in topics:
            logger.info(f"Creating topic: {TOPIC_NAME}")
            topic = NewTopic(
                name=TOPIC_NAME,
                num_partitions=1,
                replication_factor=1
            )
            admin.create_topics([topic])
        else:
            logger.info(f"Topic already exists: {TOPIC_NAME}")
    except Exception as e:
        logger.error(f"Error creating topic: {e}")
    finally:
        admin.close()
