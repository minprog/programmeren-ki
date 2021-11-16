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
def encrypts_a():
    """encrypts "a" as "Z" """
    check50.run("./cypher").stdin("a").stdout("[Cc][yi]phertext:\s*Z\n", "cyphertext: Z\n").exit(0)

@check50.check(compiles)
def encrypts_hello_world():
    """encrypts "hEllo wOrld" as "SvOOL DlIOW" """
    check50.run("./cypher").stdin("hEllo wOrld").stdout("[Cc][yi]phertext:\s*SvOOL DlIOW\n", "cyphertext: SvOOL DlIOW\n").exit(0)

@check50.check(encrypts_a)
def encrypts_a_lower():
    """encrypts "a" as "z" with the -l flag"""
    check50.run("./cypher -l").stdin("a").stdout("[Cc][yi]phertext:\s*z\n", "cyphertext: z\n").exit(0)

@check50.check(encrypts_hello_world)
def encrypts_hello_world_lower():
    """encrypts "hEllo wOrld" as "svool dliow" with the -l flag"""
    check50.run("./cypher -l").stdin("hEllo wOrld").stdout("[Cc][yi]phertext:\s*svool dliow\n", "cyphertext: svool dliow\n").exit(0)
