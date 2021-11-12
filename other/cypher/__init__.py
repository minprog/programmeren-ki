import check50
import check50.c

@check50.check()
def exists():
    """cypher.c exists."""
    check50.exists("cypher.c")

@check50.check(exists)
def compiles():
    """cypher.c compiles."""
    check50.c.compile("cypher.c", lcs50=True)

@check50.check(compiles)
def encrypts_hello_world():
    """encrypts "hEllo wOrld" as "SvOOL DlIOW" """
    check50.run("./cypher").stdin("hEllo wOrld").stdout("[Cc]iphertext:\s*SvOOL DlIOW\n", "ciphertext: b\n").exit(0)
