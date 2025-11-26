import pytest

def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1

@pytest.mark.skip
def test_loginbyfacebook():
    print("this is login by facebook")
    assert 1 == 1

@pytest.mark.skip
def test_loginbyphone():
    print("this is login by phone")
    assert 1 == 1

@pytest.mark.skip
def test_signupbyemail():
    print("This is signup by email test")
    assert True == True


@pytest.mark.skip
def test_signupbyfacebook():
    print("This is signup by facebook test")
    assert True == True


def test_signupbyphone():
    print("This is signup by phone test")
    assert True == True
