import sqlite3
import pkg_resources

database=sqlite3.connect(
    pkg_resources.resource_filename("src.db", "dist/test_db.db"),
    check_same_thread=False
    )

sql_fl = pkg_resources.resource_filename("src.db", "create.sql")
with open(sql_fl, 'r') as sql:
    database.cursor().executescript(sql.read())

