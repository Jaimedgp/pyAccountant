"""
    Module with the database object used to c into database
    and interact with it
"""

import sqlite3
from datetime import date
from typing import Optional

import pandas as pd


class QueriesDB():
    """
        Manage DataBase tables for account information and activities
    """

    from . import database

    def __init__(self, database: sqlite3.Connection=database):
        """ Connect to database """

        self.c = database.cursor()

    def bank_queries(
        self,
        ) -> list:

        data = self.c.execute("""
            SELECT *
                FROM BANK_ACCOUNT;
            """).fetchall()

        return data

    def type_queries(
        self,
        ) -> list:

        data = self.c.execute("""
            SELECT *
                FROM TRANSFER_TYPE;
            """).fetchall()

        return data

    def transactions_queries(
        self,
        ) -> dict:

        data = self.c.execute("""
            SELECT *
                FROM [ transaction ];
            """).fetchall()

        return pd.DataFrame(data=data,
                            columns=["id", "amount/eur", "date", "transfer",
                                     "count", "bank", "description"]
                            ).to_dict()
