import check50
import check50.c

@check50.check()
def exists():
    """rna.c is correct"""
    check50.exists("rna.c")

@check50.check(exists)
def compiles():
    """rna.c compiles"""
    check50.c.compile("rna.c", "-lcs50")

@check50.check(compiles)
def testATGC():
    """transcribes ATGC as UACG"""
    (check50.run("./rna ATGC")
        .stdout("UACG", str_output="UACG"))

@check50.check(testATGC)
def testAAGGTTCCAA():
    """transcribes AAGGTTCCAA as UUCCAAGGUU"""
    (check50.run("./rna AAGGTTCCAA")
        .stdout("UUCCAAGGUU", str_output="UUCCAAGGUU"))

@check50.check(testAAGGTTCCAA)
def testCGaT():
    """transcribes CGaT as GCUA"""
    (check50.run("./rna CGaT")
        .stdout("GCUA", str_output="GCUA"))

@check50.check(testCGaT)
def testAAF():
    """handles invalid input"""
    (check50.run("./rna AAF")
        .stdout("[I|i]nvalid DNA", str_output="Invalid DNA")).exit(1)

@check50.check(testAAF)
def handles_no_argv():
    """handles lack of argv[1]"""
    check50.run("./rna").stdout("[U|u]sage: ./rna ATGC", str_output="Usage: ./rna ATGC").exit(1)

@check50.check(testAAF)
def handles_too_many_argv():
    """handles having too many command-line arguments"""
    check50.run("./rna ATGC ATGC").stdout("[U|u]sage: ./rna ATGC", str_output="Usage: ./rna ATGC").exit(1)
