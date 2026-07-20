import json

from kafka import KafkaConsumer

from services.rag.rag_service import (
    extract_text_from_pdf,
    split_text_into_chunks,
    create_vector_store,
)

KAFKA_BROKER = "localhost:9092"
DOCUMENT_UPLOAD_TOPIC = "document-upload"
CONSUMER_GROUP = "knowledgeops-group"

consumer = KafkaConsumer(
    DOCUMENT_UPLOAD_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="latest",
    group_id=CONSUMER_GROUP,
    value_deserializer=lambda message: json.loads(
        message.decode("utf-8")
    ),
)

print("\n========================================")
print("Kafka Consumer Started")
print("Waiting for document upload events...")
print("========================================\n")


def process_document(filename: str, filepath: str):
    """
    Process a document uploaded through Kafka.
    """

    print("=" * 60)
    print(f"Processing Document : {filename}")
    print("=" * 60)

    text = extract_text_from_pdf(filepath)

    print("PDF Extracted Successfully")

    chunks = split_text_into_chunks(text)

    print(f"Chunks Created : {len(chunks)}")

    create_vector_store(
        chunks=chunks,
        source_file=filename,
    )

    print("FAISS Vector Store Updated")

    print(f"{filename} Processed Successfully\n")


for message in consumer:

    event = message.value

    filename = event["filename"]
    filepath = event["filepath"]

    try:

        process_document(
            filename=filename,
            filepath=filepath,
        )

    except Exception as e:

        print("=" * 60)
        print("Document Processing Failed")
        print("=" * 60)
        print(e)
        print()