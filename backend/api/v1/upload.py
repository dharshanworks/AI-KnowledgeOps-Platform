from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from services.messaging.kafka_producer import publish_document

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF document.

    The uploaded file is stored locally and an event is
    published to Kafka for asynchronous processing.
    """

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    publish_document(
        filename=file.filename,
        filepath=str(file_path),
    )

    return {
        "message": "Document uploaded successfully.",
        "status": "Processing",
        "filename": file.filename,
    }