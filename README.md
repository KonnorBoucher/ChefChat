# ChefChat:
An application that lets you upload your recipes as PDFs and chat with them! Built with Python, FastAPI for backend, and Vite and Javascript for the frontend, and Ollama to host the LLM.

### Status:
**Backend and recipe chunking logic is done, frontend and deployment are still in progress**

## How it works

1. **Upload** — Drop in a recipe PDF (currently supports single-page recipes).
2. **Chunk & embed** — The backend parses the PDF, chunks it by recipe-relevant sections, and generates embeddings using `sentence-transformers`.
3. **Store** — Embeddings are stored in **ChromaDB** for fast semantic search.
4. **Chat** — Ask a question, and the app retrieves the most relevant recipe chunks, then passes them to a local LLM (**Llama 3.2** via **Ollama**) to generate a grounded, conversational answer.

## Tech stack

**Backend**
- Python / FastAPI
- ChromaDB (vector store)
- sentence-transformers (embeddings)
- Ollama + Llama 3.2 (local LLM inference)

**Frontend**
- React + Vite (JavaScript)

## Current limitations

- Recipes must be single-page PDFs (multi-page support planned)

## Prerequisites

- Python 3.11
- [Ollama](https://ollama.com) installed and running locally, with the Llama 3.2 model pulled:
  ```bash
  ollama pull llama3.2
  ```
- Node.js (for the frontend)

## Getting started

**Backend**
Craete a virtual environment using the given .yml file
```bash
conda env create -f environment.yml
```
Activate the environment:
```bash
conda activate chefchat
```
Start the backend:
```bash
cd backend
uvicorn main:app --reload
```

Note: Make sure Ollama is running (`ollama serve`) before starting the backend

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

## Roadmap

- [ ] Multi-page PDF support
- [ ] Multiple recipe per page support
- [ ] Recipe deletion
- [ ] Recipe grouping/sorting
- [ ] Deployement

---

Built by [Konnor Boucher](https://github.com/KonnorBoucher)
