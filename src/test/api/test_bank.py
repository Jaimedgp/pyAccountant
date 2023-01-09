import pytest

from . import client


@pytest.mark.parametrize(
    'bank, alias, description', [
    ("CaixaBank", "Principal", "Esto es una prueba"),
    ("CaixaBank", "Ocio", "Esto es una prueba"),
    ("Unicaja", "Ahorros", "Esto es una prueba"),
])
def test_new_bank(bank, alias, description):

    response = client.post("/bank/new/",
                           params={"bank": bank,
                                   "alias": alias,
                                   "description": description
                                   }
                           )
    assert response
