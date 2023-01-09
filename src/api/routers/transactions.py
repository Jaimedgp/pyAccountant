from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
    )


@router.post("/new/")
def insert_transaction(
):
    return {"result": "done"}

