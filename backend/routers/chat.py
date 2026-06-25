from services.generation import generate_answer
from services.retrieval import retrieve_recipes
from fastapi import APIRouter
from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

router = APIRouter()

@router.post("/chat")
async def get_answer(chat: ChatRequest) -> str:
    recipe_results = retrieve_recipes(chat.question)
    answer = generate_answer(chat.question, recipe_results)
    return answer
