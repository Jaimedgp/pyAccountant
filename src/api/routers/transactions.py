from datetime import date as dt
from fastapi import APIRouter
from typing import Optional

from ...db import InsertDB, QueriesDB
from .. import DATA


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
    )

insert_db = InsertDB(DATA["database"])
queries_db = QueriesDB(DATA["database"])


@router.post("/new/")
def insert_transaction(
    id_bank: int,
    id_type: int,
    amount: float,
    date: dt=dt.today(),
    description: str="",
):

    op = insert_db.transfer_insert(
        id_bank=id_bank,
        id_type=id_type,
        amount=amount,
        description=description,
        trans_date=date,
    )

    if not op:
        return {"result": "failed"}

    return {"result": "done"}


@router.get("/query/")
def query_type():

    op = queries_db.transactions_queries()

    return op
