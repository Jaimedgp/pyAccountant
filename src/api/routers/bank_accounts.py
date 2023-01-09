from fastapi import APIRouter
from typing import Optional

from ...db import InsertDB
from .. import DATA

router = APIRouter(
    prefix="/bank",
    tags=["Bank account"],
    )

DB = InsertDB(DATA["database"])


@router.post("/new/")
def insert_bank(
    bank: str,
    alias: str,
    description: Optional[str]="",
):

    op = DB.bank_insert(bank, alias, description)

    if not op:
        return {"result": "failed"}

    return {"result": "done"}
