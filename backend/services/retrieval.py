import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model once at startup
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ChromaDB client
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_or_create_collection(name="recipes")

def retrieve_recipes(question:str) -> str:
    embeddings = embedding_model.encode(question).tolist()
    results = collection.query(query_embeddings=[embeddings], n_results=3) # returns 3 recipes

    documents = results["documents"][0] # list of all recipes collected
    final_results = "\n\n---\n\n".join(documents) # join and separate each recipe

    return final_results

