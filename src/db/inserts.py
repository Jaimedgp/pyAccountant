"""
    Module with the database object used to connect into database
    and interact with it
"""

from datetime import date
import sqlite3


class InsertDB():
    """
        Manage DataBase tables for account information and activities
    """

    def __init__(self, database: str='dist/account.db'):
        """ Connect to database """

        self.connect = sqlite3.connect(database)

    def bank_insert(
        self,
        bank: str,
        alias: str,
        description: str="",
    ) -> None:
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
            self.connect.execute("""
                INSERT INTO BANK_ACCOUNT (bank, alias, description)
                    VALUES (?,?,?);
                """, (bank, alias, description))
            self.connect.commit()

        except sqlite3.OperationalError:
            pass

    def types_insert(
        self,
        name: str,
        operation: str,
        description: str="",
    ) -> None:
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
            self.connect.execute("""
                INSERT INTO TRANSFER_TYPE (name, operation, description)
                    VALUES (?,?,?);
                """, (name, operation, description))
            self.connect.commit()

        except sqlite3.OperationalError:
            pass

    def transfer_insert(
        self,
        id_bank: int,
        id_type: int,
        amount: float,
        trans_date: date=date.today(),
        description: str="",
    ) -> None:
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
            self.connect.execute("""
                INSERT INTO TRANSFER (id_bank, id_type, amount, date, description)
                    VALUES (?,?,?,?,?);
                """, (id_bank, id_type, amount, trans_date, description))
            self.connect.commit()
        except sqlite3.OperationalError:
            pass
