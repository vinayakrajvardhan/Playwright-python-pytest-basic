import pytest

@pytest.fixture
def setup():
    print("setup the browser")
    yield
    print("close the browser")