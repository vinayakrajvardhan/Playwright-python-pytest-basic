'''
Pre-requisite:  Install a pytest plugin "pytest-xdist" to run tests parallel
pip install pytest-xdist
'''

def test_one():
    print("running test one")
    assert True

def test_two():
    print("Running test two")
    assert True

def test_three():
    print("Running test three")
    assert True

def test_four():
    print("Running test four")
    assert True


'''
To runt he tests parallely:

    pytest day17/test_parallel.py -v -s -n=2 
    pytest day17/test_parallel.py -v -s -n 2 

'''