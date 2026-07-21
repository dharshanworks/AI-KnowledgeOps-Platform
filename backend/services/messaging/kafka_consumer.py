import json
import os
import time

from dotenv import load_dotenv
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
DOCUMENT_UPLOAD_TOPIC = os.getenv(
    "DOCUMENT_UPLOAD_TOPIC",
    "document-upload",
)

producer = None


def get_producer():
    """
    Create Kafka producer only when needed.
    Retries until Kafka becomes available.
    """

    global producer

    if producer is not None:
        return producer

    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=KAFKA_BROKER,
                value_serializer=lambda value: json.dumps(value).encode("utf-8"),
            )

            print("\n========================================")
            print("Kafka Producer Connected")
            print(f"Broker : {KAFKA_BROKER}")
            print("========================================\n")

            return producer

        except NoBrokersAvailable:
            print(f"Kafka not available at {KAFKA_BROKER}. Retrying in 5 seconds...")
            time.sleep(5)


def publish_document(filename: str, filepath: str) -> None:
    """
    Publish a document upload event to Kafka.
    """

    kafka_producer = get_producer()

    event = {
        "filename": filename,
        "filepath": filepath,
    }

    try:
        kafka_producer.send(
            DOCUMENT_UPLOAD_TOPIC,
            value=event,
        )

        kafka_producer.flush()

        print(f"Published document upload event: {filename}")

    except Exception as e:
        print(f"Failed to publish Kafka event: {e}")
        raise