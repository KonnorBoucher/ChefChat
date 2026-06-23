import fitz  # pymupdf
import re
from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model once at startup
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ChromaDB client
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_or_create_collection(name="recipes")


def extract_text_from_pdf(file_bytes: bytes) -> str:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def chunk_by_recipe(text: str) -> list[str]:
    # Common recipe header patterns in cookbooks
    recipe_patterns = [
        r'\n(?=[A-Z][A-Z\s]{3,}\n)',      # ALL CAPS TITLE
        r'\n(?=\d+\.\s+[A-Z])',            # Numbered recipes like "1. Pasta..."
        r'\n(?=Recipe\s*:)',               # "Recipe:" prefix
        r'\n(?=#{1,3}\s)',                 # Markdown headers
    ]

    combined_pattern = '|'.join(recipe_patterns)
    chunks = re.split(combined_pattern, text)

    # Filter out chunks too short to be a real recipe
    chunks = [c.strip() for c in chunks if len(c.strip()) > 100]

    return chunks


def embed_and_store(file_bytes: bytes, filename: str) -> int:
    text = extract_text_from_pdf(file_bytes)
    chunks = chunk_by_recipe(text)

    embeddings = embedding_model.encode(chunks).tolist()
    ids = [f"{filename}_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=[{"source": filename, "recipe_index": i} for i in range(len(chunks))]
    )

    return len(chunks)