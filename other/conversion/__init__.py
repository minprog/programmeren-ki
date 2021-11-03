import check50
import check50.c


@check50.check()
def exists():
    """conversion.c exists"""
    check50.exists("conversion.c")
    check50.include("C0205.txt", "F0102.txt", "F10003.txt", "F193.txt", "F093.txt")


@check50.check(exists)
def compiles():
    """conversion.c compiles"""
    check50.c.compile("conversion.c", lcs50=True)


@check50.check(compiles)
def testC0205():
    """input of C, 0, 20, 5 yields a well-formatted table"""
    correct = open("C0205.txt").read()
    check50.run("./conversion").stdin("C").stdin("0").stdin("20").stdin("5").stdout(correct, correct, False).exit(0)


@check50.check(compiles)
def testF0102():
    """input of F, 0, 10, 2 yields a well-formatted table"""
    correct = open("F0102.txt").read()
    check50.run("./conversion").stdin("F").stdin("0").stdin("10").stdin("2").stdout(correct, correct, False).exit(0)


@check50.check(compiles)
def testF0102():
    """input of F, 100, 0, 3 yields a well-formatted table"""
    correct = open("F10003.txt").read()
    check50.run("./conversion").stdin("F").stdin("100").stdin("0").stdin("3").stdout(correct, correct, False).exit(0)


@check50.check(compiles)
def testF193():
    """input of F, 1, 9, 3 yields a well-formatted table"""
    correct = open("F193.txt").read()
    check50.run("./conversion").stdin("F").stdin("1").stdin("9").stdin("3").stdout(correct, correct, False).exit(0)


@check50.check(compiles)
def testF093_after_negative():
    """input of v, F, 0, 9, -3, 0, 3 yields a well-formatted table"""
    correct = open("F093.txt").read()
    check50.run("./conversion").stdin("v").stdin("F").stdin("0").stdin("9").stdin("-3").stdin("0").stdin("3").stdout(correct, correct, False).exit(0)
