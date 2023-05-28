import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db(databases=['default',])
def test_create_user():
    user = User.objects.create(
        username="kamrul",
        email="kamrul.test@example.com",
        password="testpass123",
        first_name="Kamrul",
        last_name="Hasan",
    )
    assert User.objects.count() ==1
    r_user = User.objects.get(username="kamrul")
    assert r_user.is_superuser == False
    assert user.username == r_user.username


def test_example():
    ls = [
        {"name": "kamrul", "age": 30},
        {"name": "Shanjida", "age": 23},
        ]
    s = {"name": "Shanjida", "age": 23}
    assert s in ls





