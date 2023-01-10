from fastapi import APIRouter
from typing import Optional

from ...db import InsertDB, QueriesDB
from .. import DATA

router = APIRouter(
    prefix="/bank",
    tags=["Bank account"],
    )

insert_db = InsertDB(DATA["database"])
queries_db = QueriesDB(DATA["database"])


@router.post("/new/")
def insert_bank(
    bank: str,
    alias: str,
    description: Optional[str]="",
):

    op = insert_db.bank_insert(bank, alias, description)

    if not op:
        return {"result": "failed"}

    return {"result": "done"}


@router.get("/query/")
def query_bank():

    op = queries_db.bank_queries()

    return op
