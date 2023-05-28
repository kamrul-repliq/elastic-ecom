import pytest

class MyClass:
    def __init__(self, value):
        self.value = value

    def add_one(self):
        self.value += 1

@pytest.fixture
def my_class():
    # Setup
    obj = MyClass(10)

    yield obj  # Return the object as the fixture value

    # Teardown (optional)
    # Clean up any resources used by the object, if needed

def test_my_class_add_one(my_class):
    # Access the fixture object
    assert my_class.value == 10

    # Call a method on the fixture object
    my_class.add_one()
    assert my_class.value == 11
