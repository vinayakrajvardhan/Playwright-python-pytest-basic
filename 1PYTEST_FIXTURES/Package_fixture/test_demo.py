import pytest


def test_one():
    print("Executing Test One")

def test_two():
    print("Executing Test Two")


def test_three():
    print("Executing Test Three")


class TestClass:
    def test_four(self):
        print("Executing Test Four in TestClass")

    def test_five(self):
        print("Executing Test Five in TestClass")

    def test_six(self):
        print("Executing Test Six in TestClass")