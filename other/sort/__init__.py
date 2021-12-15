import check50
import check50.c

@check50.check()
def exists():
    """helpers.c exists."""
    check50.exists("helpers.c")


@check50.check(exists)
def compiles():
    """helpers.c compiles."""
    check50.include("helpers.h", "sort.c")
    check50.c.compile("sort.c", "helpers.c", exe_name="sort", lcs50=True)


@check50.check(compiles)
def sort_reversed():
    """sorts {5,4,3,2,1}"""
    test_sorted([5, 4, 3, 2, 1])


@check50.check(compiles)
def sort_shuffled():
    """sorts {5,3,1,2,4,6}"""
    test_sorted([5, 3, 1, 2, 4, 6])


@check50.check(compiles)
def sort_last():
    """sorts {5,3,6,1,2,4}"""
    test_sorted([5, 3, 6, 1, 2, 4])


def test_sorted(items):
    check = check50.run("./sort")
    for i in items:
        check.stdin(str(i))
    check.stdin(check50.EOF)
    for i in sorted(items):
        check.stdout(str(i))
    check.exit(0)
