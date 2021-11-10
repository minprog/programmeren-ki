import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import re

@check50.check()
def exists():
    """goldbach.c exists"""
    check50.exists("goldbach.c")

@check50.check(exists)
def compiles():
    """goldbach.c compiles"""
    check50.c.compile("goldbach.c", lcs50=True)

@check50.check(compiles)
def test_output():
    """handles printing the right numbers in the right format (we think)"""
    with logged_check_factory("./goldbach") as create_check:
        create_check().stdout()

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
