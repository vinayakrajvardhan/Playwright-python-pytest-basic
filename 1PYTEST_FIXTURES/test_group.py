'''
grouping tests:
--------------
test_LoginByEmail -> sanity , regression
test_LoginByFacebook -> sanity
test_LoginByPhone -> regression
test_signupByEmail -> sanity, regression
test_signupByFacebook -> regression
test_signupbyphone -> sanity
test_paymentindollor -> sanity, regression
test_paymentinrupees -> regression

'''

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1


@pytest.mark.sanity
def test_loginbyfacebook():
    print("this is login by facebook")
    assert 1 == 1


@pytest.mark.regression
def test_loginbyphone():
    print("this is login by phone")
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    print("This is signup by email test")
    assert True == True


@pytest.mark.regression
def test_signupbyfacebook():
    print("This is signup by facebook test")
    assert True == True


@pytest.mark.sanity
def test_signupbyphone():
    print("This is signup by phone test")
    assert True == True


@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollor():
    print("this is payment in dollor test")
    assert 1 == 1


@pytest.mark.regression
def test_paymentinrupess():
    print("this is payment in rupees test")
    assert 1 == 1


'''
1) run sanity tests (5)
     pytest day17/test_grouping.py -v -s -m "sanity"

2) run only regression tests (6)
    pytest day17/test_grouping.py -v -s -m "regression"

3) run tests which are belongs to both sanity and regression
    pytest day17/test_grouping.py -v -s -m "sanity and regression"

4) run only sanity tests which are not belongs to regression
    pytest day17/test_grouping.py -v -s -m "sanity" -m "not regression"

5) run only regression which are not belongs to sanity
    pytest day17/test_grouping.py -v -s -m "regression" -m "not sanity"

'''
