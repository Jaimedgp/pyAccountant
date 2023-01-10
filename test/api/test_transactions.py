import pytest

from . import client


@pytest.mark.parametrize(
    "id_bank, id_type, amount, trans_date, description", [
    (1, 1, 125.5, "2022/01/21", "Prueba 1"),
    (2, 3, 125.5, "2022/02/26", "Prueba 2"),
    (1, 2, 125.5, "2022/06/04", "Prueba 3"),
    (3, 1, 125.5, "2022/01/07", "Prueba 4"),
])
def test_new_transaction(id_bank, id_type, amount, trans_date, description):

    response = client.post("/transactions/new/",
                           params={"id_bank": id_bank,
                                   "id_type": id_type,
                                   "amount": amount,
                                   "trans_date": trans_date,
                                   "description": description
                                   }
                           )
    assert response

