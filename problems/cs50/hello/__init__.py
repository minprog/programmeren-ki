import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists."""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles."""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def veronica():
    """responds to name Zamyla."""
    check50.run("./hello").stdin("Zamyla").stdout("Zamyla").exit()

@check50.check(compiles)
def brian():
    """responds to name Doug."""
    check50.run("./hello").stdin("Doug").stdout("Doug").exit()
