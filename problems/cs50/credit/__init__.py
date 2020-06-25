import check50
import check50.c

@check50.check()
def exists():
    """credit.c exists."""
    check50.exists("credit.c")

@check50.check(exists)
def compiles():
    """credit.c compiles."""
    check50.c.compile("credit.c", lcs50=True)

@check50.check(compiles)
def test1():
    """identifies 378282246310005 as AMEX"""
    check50.run("./credit").stdin("378282246310005").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """identifies 371449635398431 as AMEX"""
    check50.run("./credit").stdin("371449635398431").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """identifies 5555555555554444 as MASTERCARD"""
    check50.run("./credit").stdin("5555555555554444").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """identifies 5105105105105100 as MASTERCARD"""
    check50.run("./credit").stdin("5105105105105100").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test5():
    """identifies 4111111111111111 as VISA"""
    check50.run("./credit").stdin("4111111111111111").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test6():
    """identifies 4012888888881881 as VISA"""
    check50.run("./credit").stdin("4012888888881881").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test7():
    """identifies 1234567890 as INVALID"""
    check50.run("./credit").stdin("1234567890").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test8():
    """identifies 369421438430814 as INVALID"""
    check50.run("./credit").stdin("369421438430814").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test9():
    """identifies 4062901840 as INVALID"""
    check50.run("./credit").stdin("4062901840").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test10():
    """identifies 5673598276138003 as INVALID"""
    check50.run("./credit").stdin("5673598276138003").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test11():
    """identifies 4111111111111113 as INVALID"""
    check50.run("./credit").stdin("4111111111111113").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./credit").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./credit").stdin("").reject()

@check50.check(compiles)
def test_reject_repeated():
    """rejects any number of invalid inputs"""
    check = check50.run("./credit")
    for i in range(8):
        for value in ["foo", ""]:
            check.stdin(value)
    check.reject()
