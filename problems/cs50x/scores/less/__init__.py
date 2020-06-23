import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """scores.py exists"""
    check50.exists("scores.py")


@check50.check(exists)
def compiles():
    """scores.py compiles"""
    uva.check50.py.compile("scores.py")


@check50.check(compiles)
def test5():
    """prints a single row barchart with input 5 -1"""
    result = uva.check50.py.run("scores.py", stdin=["5", "-1"])
    if "#####\n" not in result.stdout:
        raise check50.Mismatch("#####\n", result.stdout)


@check50.check(compiles)
def test123():
    """prints a three row barchart with input 1 2 3 -1"""
    result = uva.check50.py.run("scores.py", stdin=["1", "2", "3", "-1"])
    if "#\n##\n###\n" not in result.stdout:
        raise check50.Mismatch("#\n##\n###\n", result.stdout)


@check50.check(test123)
def test():
    """ignores scores bigger than 10 with input 1 11 2 20 3 -1"""
    result = uva.check50.py.run("scores.py", stdin=["1", "11", "2", "20", "3", "-1"])
    if "#\n##\n###\n" not in result.stdout:
        raise check50.Mismatch("#\n##\n###\n", result.stdout)
