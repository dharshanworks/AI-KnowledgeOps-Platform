from services.kafka_producer import publish_document

publish_document(
    {
        "filename":"test.pdf",
        "path":"uploads/test.pdf"
    }
)

print("Done")