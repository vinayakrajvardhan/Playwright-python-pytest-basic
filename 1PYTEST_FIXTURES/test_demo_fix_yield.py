import pytest

@pytest.fixture
def setup():
    print("setup the browser")
    yield
    print("close the browser")



def test_one(setup):
    print("Executing Test One")



def test_two(setup):
    print("Executing Test Two")


def test_three():
    print("Executing Test Three")


