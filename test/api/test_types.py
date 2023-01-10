import pytest

from . import client


@pytest.mark.parametrize(
    'name, operation, description', [
    ("ingresos uc",  "income", "Prueba 1"),
    ("ingresos cic", "income", "Prueba 2"),
    ("gastos comunes", "expenditure", "Prueba 1"),
])
def test_new_types(name, operation, description):

    response = client.post("/types/new/",
                           params={"name": name,
                                   "operation": operation,
                                   "description": description
                                   }
                           )
    assert response
