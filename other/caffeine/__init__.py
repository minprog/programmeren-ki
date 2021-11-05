import check50
import check50.c


@check50.check()
def exists():
    """caffeine.c exists"""
    check50.exists("caffeine.c")


@check50.check(exists)
def compiles():
    """caffeine.c compiles"""
    check50.c.compile("caffeine.c", lcs50=True)


@check50.check(compiles)
def test010():
    """input of 0.10 yields output of 2 drinks"""
    check50.run("./caffeine").stdin("0.10").stdout(number(1), "1\n").stdout(number(1), "4\n").stdout(number(2), "2\n").exit(0)


@check50.check(compiles)
def test001():
    """input of 0.01 yields output of 1 drink"""
    check50.run("./caffeine").stdin("0.01").stdout("1 drink ", "That makes 1 drink in total").exit(0)


@check50.check(compiles)
def test0001():
    """input of 0.001 yields output of 0 drinks"""
    check50.run("./caffeine").stdin("0.001").stdout("0 drinks ", "That makes 0 drinks in total").exit(0)


@check50.check(compiles)
def test025():
    """input of 0.25 yields output of 5 drinks"""
    check50.run("./caffeine").stdin("0.25").stdout(number(3), "3\n").stdout(number(1), "1\n").stdout(number(1), "1\n").stdout(number(5), "5\n").exit(0)


@check50.check(compiles)
def test0251():
    """input of 0.251 yields, among other things, a piece of chocolate"""
    check50.run("./caffeine").stdin("0.251").stdout(number(3), "3\n").stdout(number(1), "1\n").stdout(number(1), "1\n").stdout(number(1), "1\n").stdout(number(5), "5\n").exit(0)

@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./caffeine").stdin("-1").reject()


@check50.check(test_reject_negative)
def test_025_after_negative():
    """erroneous input of -1 and then input of 0.25 yields output of 5"""
    check50.run("./caffeine").stdin("-1").stdin("0.25").stdout(number(3), "3\n").stdout(number(1), "1\n").stdout(number(1), "1\n").stdout(number(5), "5\n").exit(0)


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./caffeine").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./caffeine").stdin("").reject()


def number(num):
    # regex that matches `num` not surrounded by any other numbers (so number(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"
