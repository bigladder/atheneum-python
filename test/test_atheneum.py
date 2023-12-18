#pylint:disable=missing-module-docstring

from pytheneum.atheneum import Atheneum

def test_answer():
    """Example of a python unit test"""
    assert Atheneum().answer("We apologize for the inconvenience...") == 42
