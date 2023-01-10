from fastapi import APIRouter
from typing import Optional

from ...db import InsertDB, QueriesDB
from .. import DATA

router = APIRouter(
    prefix="/types",
    tags=["Types"],
    )

insert_db = InsertDB(DATA["database"])
queries_db = QueriesDB(DATA["database"])


@router.post("/new/")
def insert_type(
    name: str,
    operation: str,
    description: Optional[str]="",
):
    op = insert_db.types_insert(name, operation, description)

    if not op:
        return {"result": "failed"}

    return {"result": "done"}


@router.get("/query/")
def query_type():

    op = queries_db.type_queries()

    return op
