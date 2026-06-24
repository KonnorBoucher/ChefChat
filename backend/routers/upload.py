from fastapi import UploadFile, APIRouter
from services.embeddings import embed_and_store

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile):
    contents = await file.read()

    count = embed_and_store(contents, file.filename)

    return {"message": f"found {count} recipes"}
