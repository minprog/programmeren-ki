import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import re

@check50.check()
def exists():
    """figure.c exists"""
    check50.exists("figure.c")

@check50.check(exists)
def compiles():
    """figure.c compiles"""
    check50.c.compile("figure.c", lcs50=True)

@check50.check(compiles)
def test_reject_negative():
    """rejects a height of -1"""
    check50.run("./figure").stdin("-1").reject()

@check50.check(compiles)
def test0():
    """rejects a height of 0"""
    check50.run("./figure").stdin("0").reject()

@check50.check(compiles)
def test_output():
    """handles drawing figures (we think)"""
    with logged_check_factory("./figure") as create_check:
        create_check().stdin("4").stdout()
        create_check().stdin("5").stdout()
        create_check().stdin("6").stdout()
        create_check().stdin("7").stdout()
        create_check().stdin("8").stdout()

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    check50.run("./figure").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("./figure").stdin("").reject()

def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)

# helpers --------------------------------------------------------------------

class Stream:
    """Stream-like object that stores everything it receives"""
    def __init__(self):
        self.entries = []

    @property
    def text(self):
        return "".join(self.entries)

    def write(self, entry):
        entry = entry.replace("\r\n", "\n").replace("\r", "\n")
        self.entries.append(entry)

    def flush(self):
        pass

    def reset(self):
        self.entries = []

@contextlib.contextmanager
def logged_check_factory(command):
    """
    A factory of checks that logs everything on stdin/stdout.
    The log is written to the data.output field of check50's json output.
    """
    stream = Stream()

    def create_check():
        check = check50.run(command)
        check.process.logfile = stream
        return check

    try:
        yield create_check
    finally:
        check50.data(output=stream.text)
