import sqlite3
import pkg_resources

from fastapi.testclient import TestClient

from src.api import create_api

database=sqlite3.connect(
    pkg_resources.resource_filename("src.db", "dist/test_api.db"),
    check_same_thread=False
    )

sql_fl = pkg_resources.resource_filename("src.db", "create.sql")
with open(sql_fl, 'r') as sql:
    database.cursor().executescript(sql.read())

client = TestClient(create_api(database))
