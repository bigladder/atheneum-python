#pylint:disable=C0114

from atheneum import Atheneum

def test_answer():
    """Example of a python unit test"""
    assert Atheneum().answer("We apologize for the inconvenience...") == 42
