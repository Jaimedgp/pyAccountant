from fastapi import APIRouter

router = APIRouter(
    prefix="/types",
    tags=["Transactions", "Types"],
    )


@router.post("/new/")
def insert_type(
):
    return {"result": "done"}
