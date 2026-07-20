from fastapi import APIRouter
from pydantic import BaseModel

from services.cache.redis_service import (
    cache_answer,
    get_cached_answer,
)
from services.llm.groq_service import generate_answer
from services.rag.rag_service import search_documents

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):
    """
    Ask a question against the uploaded documents.
    """

    # Retrieve relevant documents first (needed for citations)
    documents = search_documents(request.question)

    sources = []

    for doc in documents:
        sources.append(
            {
                "document": doc.metadata.get("source"),
                "chunk": doc.metadata.get("chunk"),
                "uploaded_at": doc.metadata.get("uploaded_at"),
            }
        )

    # Remove duplicate sources
    unique_sources = []
    seen = set()

    for source in sources:
        key = (
            source["document"],
            source["chunk"],
        )

        if key not in seen:
            seen.add(key)
            unique_sources.append(source)

    # Check Redis Cache
    cached_answer = get_cached_answer(request.question)

    if cached_answer:
        print("✅ Cache Hit")

        return {
            "question": request.question,
            "answer": cached_answer,
            "llm": "redis-cache",
            "sources": unique_sources,
        }

    print("❌ Cache Miss")

    # Build context for the LLM
    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    # Generate answer using Groq
    answer = generate_answer(
        request.question,
        context,
    )

    # Cache answer
    cache_answer(
        request.question,
        answer,
    )

    return {
        "question": request.question,
        "answer": answer,
        "llm": "groq",
        "sources": unique_sources,
    }