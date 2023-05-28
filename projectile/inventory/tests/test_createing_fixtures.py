import pytest

# Fixtures behavior
# function Run once per test
# class Run once per class of tests
# module Run once per module
# session Run once per session

@pytest.fixture(scope='session')
def fixture1():
    print("Run fixture 1")
    return 1

@pytest.fixture()
def fixture2():
    print("Run fixture 2")
    return 2

@pytest.fixture(scope='function')
def fixture3():
    print("Run fixture 3")
    return 3

@pytest.fixture
def yield_fixture():
    print("Start test phase")
    yield 6
    print("End Test phase")

def test_example1(fixture1,fixture2, fixture3):
    num1 = fixture1
    num2 = fixture2
    num3 = fixture3

    assert num1==1
    assert num2==2

def test_example2(fixture1,fixture2, fixture3):
    num1 = fixture1
    num2 = fixture2
    num3 = fixture3

    assert num1==1
    assert num2==2


def test_yield(yield_fixture):
    print("Test Yeild")
    assert yield_fixture == 6




