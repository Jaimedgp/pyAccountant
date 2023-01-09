"""
    Module with the database object used to c into database
    and interact with it
"""

import sqlite3
from datetime import date
from typing import Optional


class InsertDB():
    """
        Manage DataBase tables for account information and activities
    """

    from . import database

    def __init__(self, database: sqlite3.Connection=database):
        """ Connect to database """

        self.c = database.cursor()

    def bank_insert(
        self,
        bank: str,
        alias: str,
        description: Optional[str],
    ) -> bool:
        """
        Insert new bank account information into the database

        Parameters
        ----------
        bank : str
            Bank name
        alias : str
            Alias of the bank account. This is used to identify different
            accounts in the same bank by it's use.
        description : str
            Short description of the use of this account
        """

        try:
            self.c.execute("""
                INSERT INTO BANK_ACCOUNT (bank, alias, description)
                    VALUES (?,?,?);
                """, (bank, alias, description))
            #self.c.commit()

            return True
        except sqlite3.OperationalError as e:
            print(e)
            return False

    def types_insert(
        self,
        name: str,
        operation: str,
        description: Optional[str],
    ) -> bool:
        """
        Insert new transaction type information into the database

        Parameters
        ----------
        name : str
            Name of the transaction. This is used to identify the nature of the
            operation.
        operation : str
            Can be an Income or a expenditure
        description : str
            Short description of the use of the transaction type
        """

        try:
            self.c.execute("""
                INSERT INTO TRANSFER_TYPE (name, operation, description)
                    VALUES (?,?,?);
                """, (name, operation, description))
            #self.c.commit()

            return True
        except sqlite3.OperationalError as e:
            print(e)
            return False

    def transfer_insert(
        self,
        id_bank: int,
        id_type: int,
        amount: float,
        description: Optional[str],
        trans_date: date=date.today(),
    ) -> bool:
        """
        Insert new transaction information into the database

        Parameters
        ----------
        id_bank : int
            BANK_ACCOUNT id
        id_type : int
            TRANSFER_TYPE id
        amount : float
            amount of the transaction
        trans_date : datetime.date, default: today
            Date of the transaction
        description : str
            Short description of the transaction
        """

        try:
            self.c.execute("""
                INSERT INTO TRANSFER (id_bank, id_type, amount, date, description)
                    VALUES (?,?,?,?,?);
                """, (id_bank, id_type, amount, trans_date, description))
            #self.c.commit()

            return True
        except sqlite3.OperationalError as e:
            print(e)
            return False
