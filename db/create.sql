-- DATABASE : ACCOUNTANT
-- SOURCE   : SQLITE 3
--
-- Database with bank accounts information and activities
--

CREATE TABLE IF NOT EXISTS BANK_ACCOUNT(
    id              INTEGER         NOT NULL     PRIMARY KEY     AUTOINCREMENT,
    bank            VARCHAR(200)    NOT NULL,
    alias           VARCHAR(50)     NOT NULL,
    description     VARCHAR(200),

    CONSTRAINT bank_unq UNIQUE (bank, alias)
);


CREATE TABLE IF NOT EXISTS TRANSFER_TYPE(
    id              INTEGER         NOT NULL     PRIMARY KEY     AUTOINCREMENT,
    name            VARCHAR(50)     NOT NULL,
    description     VARCHAR(200),

    CONSTRAINT name_unq UNIQUE (name)
);


CREATE TABLE IF NOT EXISTS TRANSFER(
    id          INTEGER     NOT NULL PRIMARY KEY     AUTOINCREMENT,
    id_bank     INTEGER     NOT NULL,
    id_type     INTEGER     NOT NULL,
    amount      FLOAT       NOT NULL,
    date        DATE        NOT NULL,
    description VARCHAR(200),

    FOREIGN KEY (id_bank) REFERENCES BANK_ACCOUNT(id),
    FOREIGN KEY (id_type) REFERENCES TRANSFERS_TYPES(id)
);
