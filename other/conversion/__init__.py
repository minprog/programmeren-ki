import check50
import check50.c


@check50.check()
def exists():
    """conversion.c exists"""
    check50.exists("conversion.c")
    check50.include("C0205.txt")


@check50.check(exists)
def compiles():
    """conversion.c compiles"""
    check50.c.compile("conversion.c", lcs50=True)


@check50.check(compiles)
def testC0205():
    """input of C, 0, 20, 5 yields a well-formatted table"""
    correct = open("C0205.txt").read()
    check50.run("./conversion").stdin("C").stdin("0").stdin("20").stdin("5").stdout(correct, "table", False).exit(0)




# @check50.check(compiles)
# def test_reject_negative():
#     """rejects a negative input like -1"""
#     check50.run("./conversion").stdin("-1").reject()
#
#
# @check50.check(test_reject_negative)
# def test_041_after_negative():
#     """erroneous input of -1 and then input of 0.41 yields output of 4"""
#     check50.run("./conversion").stdin("-1").stdin("0.41").stdout(coins(4), "4\n").exit(0)
#
#
# @check50.check(compiles)
# def test_reject_foo():
#     """rejects a non-numeric input of "foo" """
#     check50.run("./conversion").stdin("foo").reject()
#
#
# @check50.check(compiles)
# def test_reject_empty():
#     """rejects a non-numeric input of "" """
#     check50.run("./conversion").stdin("").reject()
#
#
# def coins(num):
#     # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
#     return fr"(?<!\d){num}(?!\d)"
