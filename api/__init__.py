import sqlite3
import pkg_resources

from fastapi import FastAPI

DATA = {}

def get_database():

    database_fl = pkg_resources.resource_filename(
        "src.db", "dist/accountant.db")
    database = sqlite3.connect(database_fl,
                               check_same_thread=False)

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

    @app.get('/')
    def root():
        return {"status": "up"}

    return app
