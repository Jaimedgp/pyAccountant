import pytest

from ...db import InsertDB


DATABASE = InsertDB(database='dist/test.db')

@pytest.mark.parametrize(
    'bank, alias, description', [
    ("CaixaBank", "Principal", "Esto es una prueba"),
    ("CaixaBank", "Ocio", "Esto es una prueba"),
    ("Unicaja", "Ahorros", "Esto es una prueba"),
])
def test_bank(bank, alias, description):
    DATABASE.bank_insert(bank, alias, description)

    assert True


@pytest.mark.parametrize(
    'name, operation, description', [
    ("ingresos uc",  "income", "Prueba 1"),
    ("ingresos cic", "income", "Prueba 2"),
    ("gastos comunes", "expenditure", "Prueba 1"),
])
def test_types(name, operation, description):
    DATABASE.types_insert(name, operation, description)

    assert True


@pytest.mark.parametrize(
    "id_bank, id_type, amount, trans_date, description", [
    (1, 1, 125.5, "2022/01/21", "Prueba 1"),
    (2, 3, 125.5, "2022/02/26", "Prueba 2"),
    (1, 2, 125.5, "2022/06/04", "Prueba 3"),
    (3, 1, 125.5, "2022/01/07", "Prueba 4"),
])
def test_trans(id_bank, id_type, amount, trans_date, description):
    DATABASE.transfer_insert(id_bank, id_type, amount, trans_date, description)

    assert True
