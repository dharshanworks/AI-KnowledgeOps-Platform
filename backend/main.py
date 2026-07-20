from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.upload import router as upload_router
from api.v1.chat import router as chat_router
from api.v1.auth import router as auth_router

app = FastAPI(
    title="Enterprise AI KnowledgeOps Platform",
    description="Enterprise AI Knowledge Management Platform",
    version="1.0.0",
)

# ==========================
# CORS Configuration
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# API Routers
# ==========================

app.include_router(
    upload_router,
    prefix="/api/upload",
    tags=["Upload"],
)

app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"],
)

app.include_router(
    auth_router,
    prefix="/api",
)

# ==========================
# Health APIs
# ==========================

@app.get("/")
def root():
    return {
        "application": "Enterprise AI KnowledgeOps Platform",
        "status": "Running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
    }