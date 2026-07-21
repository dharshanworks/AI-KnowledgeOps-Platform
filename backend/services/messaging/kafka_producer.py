import json
import os

from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
DOCUMENT_UPLOAD_TOPIC = os.getenv(
    "DOCUMENT_UPLOAD_TOPIC",
    "document-upload",
)

producer = None


def get_producer():
    """
    Create Kafka Producer only when required.
    """

    global producer

    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda value: json.dumps(value).encode("utf-8"),
        )

    return producer


def publish_document(filename: str, filepath: str):
    """
    Publish document upload event.
    """

    kafka_producer = get_producer()

    event = {
        "filename": filename,
        "filepath": filepath,
    }

    kafka_producer.send(
        DOCUMENT_UPLOAD_TOPIC,
        value=event,
    )

    kafka_producer.flush()

    print(f"Published document upload event: {filename}")