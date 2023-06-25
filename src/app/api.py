from fastapi import APIRouter
import utils

router = APIRouter()


@router.post("/encode")
def encode_sentence(sentence: str):
    return utils.encode(sentence=sentence, dim=500)
