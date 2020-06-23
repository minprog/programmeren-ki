import check50
import check50.flask
import re


@check50.check()
def exists():
    """bleep exists"""
    check50.exists("bleep.py")
    check50.include("banned.txt", "banned2.txt")


@check50.check(exists)
def test_reject_no_args():
    """rejects len(sys.argv) less than 2"""
    check50.run("python3 bleep.py").exit(1)


@check50.check(exists)
def test_reject_many_args():
    """rejects len(sys.argv) more than 2"""
    check50.run("python3 bleep.py banned.txt banned.txt").exit(1)


@check50.check(exists)
def test_no_banned_words():
    """input of 'hello world' outputs 'hello world'"""
    (check50.run("python3 bleep.py banned.txt")
            .stdin("Hello world")
            .stdout("Hello world\s*\n", "Hello world\n")
            .exit(0))


@check50.check(exists)
def test_darn():
    """input of 'This darn world' outputs 'This **** world'"""
    text = "This darn world"

    check_hardcoded(text)

    (check50.run("python3 bleep.py banned.txt")
            .stdin(text)
            .stdout("This \*\*\*\* world\s*\n", "This **** world\n")
            .exit(0))


@check50.check(exists)
def handles_capitalized():
    """input of 'THIS DARN WORLD' outputs 'THIS **** WORLD'"""
    text = "THIS DARN WORLD"

    check_hardcoded(text)

    (check50.run("python3 bleep.py banned.txt")
            .stdin(text)
            .stdout("THIS \*\*\*\* WORLD\s*\n", "THIS **** WORLD\n")
            .exit(0))


@check50.check(exists)
def substrings():
    """doesn't censor substrings"""
    text = "Darning my socks"

    check_hardcoded(text)

    (check50.run("python3 bleep.py banned.txt")
            .stdin(text)
            .stdout("Darning my socks\s*\n", "Darning my socks\n")
            .exit(0))


@check50.check(exists)
def handles_other_wordlists():
    """handles banned words lists with arbitrary words in them"""
    text = "My cat and dog are great"

    check_hardcoded(text)

    (check50.run("python3 bleep.py banned2.txt")
            .stdin(text)
            .stdout("My \*\*\* and \*\*\* are great\s*\n", "My *** and *** are great\n")
            .exit(0))


def check_hardcoded(text):
    """check if a string is hardcoded"""
    regex = r"(.*|\n)"

    for word in text.split():
        regex += word + "(.*|\n)"

    with open("bleep.py") as file:
        file_content = file.read()

    if re.search(regex, file_content, re.IGNORECASE | re.DOTALL):
        raise check50.Failure(f"Looks like you hardcoded \"{text}\" in your code?")
