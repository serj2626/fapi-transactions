from fastapi import APIRouter, Form
from typing import Annotated, Optional

router = APIRouter(prefix="/transactions", tags=["Транзакции "])


@router.post("/")
async def create_transaction(
    amount: Annotated[float, Form()],
    description: Annotated[str | None, Form()] = None,
):
    return {"amount": amount, "description": description}
