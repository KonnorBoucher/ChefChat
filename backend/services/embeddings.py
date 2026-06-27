import fitz  # pymupdf, reading and opening pdf files
import re # used for header detection and pattern matching 
from sentence_transformers import SentenceTransformer # used for embedding
import chromadb # vector database

# Load embedding model once at startup
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ChromaDB client
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_or_create_collection(name="recipes") # persists between server restarts

def is_recipe_page(text: str) -> bool:
    recipe_keywords = [
        "ingredients",
        "instructions", 
        "directions",
        "prep time",
        "cook time",
        "serves",
        "servings",
        "yield",
        "tablespoon",
        "teaspoon",
        "cup",
        "cups",
        "halves",
        "In a bowl",
        "over medium",
        "over low",
        "stir until",
        "degrees",
        "to a boil",
        "mix together",
        "cover tightly",
        "clove",
        "whole",
        "1/8",
        "1/4",
        "1/2",
        "2/3",
        "3/4",
        "stir in",
        "cover for",
        "cover and",
        "preheat",
        "from the oven"
    ]
    text_lower = text.lower()
    matches = sum(1 for keyword in recipe_keywords if keyword in text_lower)
    return matches >= 5

def chunk_by_page(file_bytes: bytes) -> list[str]:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    chunks = []
    for page in doc:
        text = page.get_text()
        if len(text.strip()) > 100 and is_recipe_page(text):
            chunks.append(text.strip())
    return chunks



def embed_and_store(file_bytes: bytes, filename: str) -> int:
    chunks = chunk_by_page(file_bytes) # creates chunks from text

    embeddings = embedding_model.encode(chunks).tolist() # turns chunks to vectors
    ids = [f"{filename}_{i}" for i in range(len(chunks))] # gives each chunk an id

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=[{"source": filename, "recipe_index": i} for i in range(len(chunks))] # used to see where the chunk is from
    )

    return len(chunks) # amount of recipes found