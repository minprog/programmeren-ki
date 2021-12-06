import check50
import check50.c

@check50.check()
def exists():
    """indexer.py exists."""
    check50.exists("indexer.py")
    check50.include("stopwords.txt")
    check50.include("texts")

@check50.check(exists)
def test_dinner():
    """correctly identifies \"dinner\" in birdman.txt"""
    check50.run("python3 indexer.py texts/birdman.txt").stdin("dinner").stdout("The word \"dinner\" can be found on lines: 549, 1542.\n", "The word \"dinner\" can be found on lines: 549, 1542.\n", timeout=5)

@check50.check(test_dinner)
def test_crash():
    """handles nonexistent words gracefully (i.e. does not crash)"""
    check50.run("python3 indexer.py texts/birdman.txt").stdin("women").stdout("Enter search term: ", "Enter search term:", timeout=5)
