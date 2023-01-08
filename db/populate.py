"""
Populate Account database with data if exists
"""


import pandas as pd

from inserts import DataBase


if __name__ == '__main__':

    bank_fl = 'data/db/banks_accounts.csv'
    trans_type_fl = 'data/db/transfers_types.csv'
    trans_fl = 'data/db/transactions.csv'

    # Connect to database
    c = DataBase()

    # INSERT BANKS ACCOUNTS INFO
    # --------------------------------

    if bank_fl != '':
        bank_data = pd.read_csv(bank_fl)

        for _, row in bank_data.iterrows():
            c.bank_insert(**row.to_dict())

    # INSERT TRANSFER TYPE INFO
    # --------------------------------

    if trans_type_fl != '':
        trans_type_data = pd.read_csv(trans_type_fl)

        for _, row in trans_type_data.iterrows():
            c.types_insert(**row.to_dict())

    # INSERT TRANSACTIONS INFO
    # --------------------------------

    if trans_fl != '':
        trans_data = pd.read_csv(trans_fl)

        for _, row in trans_data.iterrows():
            c.transfer_insert(**row.to_dict())
