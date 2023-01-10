CREATE VIEW [ transaction ] AS
    SELECT t.id, t.amount, t.date, typ.name, b.alias, b.bank, t.description
        FROM ((TRANSFER AS t
            INNER JOIN BANK_ACCOUNT as b
                ON b.id = t.id_bank)
            INNER JOIN TRANSFER_TYPE as typ
                ON typ.id = t.id_type);
