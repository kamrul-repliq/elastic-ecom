import pytest
from inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name,slug, is_active",
    [
        (1,"fashion","fashion",1),
        (18,"trainer","fashion",1),
        (32,"baseball","baseball",1)
    ],
)
def test_inventory_category_db_fixure(db, django_db_setup):
    pass
