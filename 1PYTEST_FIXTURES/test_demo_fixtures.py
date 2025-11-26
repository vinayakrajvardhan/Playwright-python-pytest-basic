import pytest

@pytest.fixture
def setup():
    print("this function")
    return "some value"



def test_one(setup):
    print("Executing Test One")
    print(setup)

def test_two(setup):
    print("Executing Test Two")


def test_three():
    print("Executing Test Three")


