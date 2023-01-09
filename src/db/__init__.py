import sqlite3
import pkg_resources


database_fl = pkg_resources.resource_filename(__name__, "dist/accountant.db")
database = sqlite3.connect(database_fl)
print(database)

# Create tables

sql_fl = pkg_resources.resource_filename(__name__, "create.sql")
with open(sql_fl, 'r') as sql:
    database.cursor().executescript(sql.read())

from .inserts import InsertDB
