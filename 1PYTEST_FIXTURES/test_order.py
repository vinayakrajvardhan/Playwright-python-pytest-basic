'''
pre-requisite : install pytest-order plugin

    # pip install pytest-ordering    # deprecated

     pip install pytest-order


'''


import pytest

# Approach 1: order tests by position

# @pytest.mark.order(3)
# def test_logout():
#     print("this is logout")
#
# @pytest.mark.order(2)
# def test_add_item():
#     print("this is add item test")
#
# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")


# Approach 2: using before , after

# @pytest.mark.order(after="test_add_item")
# def test_checkout():
#     print("this is checkout")
#
# @pytest.mark.order(before="test_checkout")
# def test_add_item():
#     print("this is add item test")
#
# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")



# Approach 3: using marker string ( user defined)

@pytest.mark.order("last")
def test_checkout():
    print("this is checkout")

@pytest.mark.order()
def test_add_item():
    print("this is add item test")

@pytest.mark.order("first")
def test_login():
    print("this is login test")













