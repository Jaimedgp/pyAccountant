from fastapi import FastAPI

import sqlite3
import pkg_resources

DATA = {}

def get_database():

    database_fl = pkg_resources.resource_filename("src.db", "dist/accountant.db")
    database = sqlite3.connect(database_fl)

    # Create tables
    sql_fl = pkg_resources.resource_filename("src.db", "create.sql")
    with open(sql_fl, 'r') as sql:
        database.cursor().executescript(sql.read())

        return database


def create_api(database=get_database()) -> FastAPI:
    global DATA

    DATA = {"database": database}

    app = FastAPI()

    from .routers.bank_accounts import router as bank
    app.include_router(bank)

    from .routers.trans_types import router as types
    app.include_router(types)

    from .routers.transactions import router as transactions
    app.include_router(transactions)

    return app
