from fastapi import APIRouter
from app import utils

router = APIRouter()

@router.get("/health")
def get_health():
    return {"message": "OK"}


@router.post("/encode")
def encode_sentence(sentence: str):
    return utils.encode(sentence=sentence, dim=500)
