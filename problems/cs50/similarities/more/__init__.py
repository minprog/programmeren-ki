import os

import check50
import check50.py

@check50.check()
def exists():
    """helpers.py exists"""
    check50.exists("helpers.py")

@check50.check(exists)
def imports():
    """can import helpers.py """
    check50.py.import_("helpers.py")

@check50.check(imports)
def edit_empty(self):
    """takes 0 operation to convert "" to "" """
    check_distance("", "", 0)

@check50.check(imports)
def edit_from_empty(self):
    """takes 3 operation to convert "dog" to "" """
    check_distance("dog", "", 3)

@check50.check(imports)
def edit_to_empty(self):
    """takes 4 operation to convert "" to "dog" """
    check_distance("", "dog", 3)

@check50.check(imports)
def edit_a_b(self):
    """takes 1 operation to convert "a" to "b" """
    check_distance("a", "b", 1)

@check50.check(imports)
def edit_insertion(self):
    """takes 1 operation to convert "cat" to "coat" """
    check_distance("cat", "coat", 1)

@check50.check(imports)
def edit_deletion(self):
    """takes 1 operation to convert "frog" to "fog" """
    check_distance("frog", "fog", 1)

@check50.check(imports)
def edit_substitution(self):
    """takes 1 operation to convert "year" to "pear" """
    check_distance("year", "pear", 1)

@check50.check(imports)
def edit_identical(self):
    """takes 0 operations to convert "today" to "today" """
    check_distance("today", "today", 0)

@check50.check(imports)
def edit_to_longer(self):
    """takes 5 operations to convert "today" to "yesterday" """
    check_distance("today", "yesterday", 5)

@check50.check(imports)
def edit_to_shorter(self):
    """takes 6 operations to convert "tomorrow" to "today" """
    check_distance("tomorrow", "today", 6)

@check50.check(imports)
def edit_handles_case(self):
    """takes 3 operations to convert "today" to "ToDaY" """
    check_distance("today", "ToDaY", 3)

def check_distance(a, b, expected):
    helpers = check50.py.import_("helpers.py")
    check50.log(f"checking edit distance for inputs {repr(a)} and {repr(b)}...")
    try:
        with open(os.devnull, "w") as f:
            actual = helpers.distances(a, b)[len(a)][len(b)][0]
        if actual != expected:
            raise check50.Failure(f"expected {expected} matches, not {actual}")
    except Exception as e:
        raise check50.Failure(str(e))
