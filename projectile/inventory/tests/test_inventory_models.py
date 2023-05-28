import pytest
from inventory.models import Product,Category,Stock
from django.contrib.auth.models import User


@pytest.fixture(scope="module")
def create_user():
    print("Creating a user")
    user = User.objects.create(
        username="dipu",
        email="test.test@example.com",
        password="testpass123",
        first_name="Nurul",
        last_name="Afsar",
    )
    return user

@pytest.mark.django_db
def test_user_create(create_user):
    user = create_user.first_name="Kamrul"
    user.save()
    assert user.first_name == "Kamrul"