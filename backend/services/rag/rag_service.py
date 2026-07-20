from datetime import datetime
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

VECTOR_STORE_PATH = "vectorstore"


def get_embeddings():
    """
    Load the Hugging Face embedding model.
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF document.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def split_text_into_chunks(text: str):
    """
    Split extracted text into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    return splitter.split_text(text)


def create_vector_store(chunks, source_file):
    """
    Create a new FAISS vector store or update
    the existing one with new document chunks.
    """

    embeddings = get_embeddings()

    documents = []

    for index, chunk in enumerate(chunks):

        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": source_file,
                    "chunk": index,
                    "uploaded_at": datetime.utcnow().isoformat(),
                },
            )
        )

    vectorstore_path = Path(VECTOR_STORE_PATH)

    if not vectorstore_path.exists():

        vector_db = FAISS.from_documents(
            documents,
            embeddings,
        )

        print("Created New Vector Store")

    else:

        vector_db = FAISS.load_local(
            VECTOR_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True,
        )

        vector_db.add_documents(documents)

        print("Updated Existing Vector Store")

    vector_db.save_local(VECTOR_STORE_PATH)

    print(
        f"Indexed {len(documents)} chunks from {source_file}"
    )


def load_vector_store():
    """
    Load the FAISS vector store.
    """

    embeddings = get_embeddings()

    return FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )


def search_documents(question: str, k: int = 3):
    """
    Retrieve the most relevant document chunks.
    """

    vector_db = load_vector_store()

    return vector_db.similarity_search(
        question,
        k=k,
    )