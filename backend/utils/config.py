import os

from dotenv import load_dotenv

load_dotenv()

# ==========================
# AI Configuration
# ==========================

MODEL_NAME = os.getenv("MODEL_NAME","llama-3.3-70b-versatile",)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ==========================
# Database
# ==========================

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# ==========================
# Redis
# ==========================

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# ==========================
# Kafka
# ==========================

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")

DOCUMENT_UPLOAD_TOPIC = os.getenv(
    "DOCUMENT_UPLOAD_TOPIC",
    "document-upload",
)

# ==========================
# JWT Authentication
# ==========================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "change-this-secret-key-in-production",
)

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256",
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        60,
    )
)