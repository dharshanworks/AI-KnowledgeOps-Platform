import json

from kafka import KafkaProducer

KAFKA_BROKER = "localhost:9092"
DOCUMENT_UPLOAD_TOPIC = "document-upload"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
)


def publish_document(filename: str, filepath: str) -> None:
    """
    Publish a document upload event to Kafka.
    """

    event = {
        "filename": filename,
        "filepath": filepath,
    }

    try:
        producer.send(
            DOCUMENT_UPLOAD_TOPIC,
            value=event,
        )

        producer.flush()

        print(f"✅ Published document upload event: {filename}")

    except Exception as e:
        print(f"❌ Failed to publish Kafka event: {e}")
        raise