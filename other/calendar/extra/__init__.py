import check50
import check50.c


@check50.check()
def exists():
    """calendar.c exists."""
    check50.exists("calendar.c")


@check50.check(exists)
def compiles():
    """calendar.c compiles."""
    check50.c.compile("calendar.c", lcs50=True)


@check50.check(compiles)
def cal_1_1800():
    """displays the calendar for Jan 1800"""
    check = check50.run("./calendar 1800 1")

    # header
    check.stdout("Jan 1800")

    # weekdays until first day of month
    check.stdout("Sun Mon Tue Wed Thu Fri Sat")

    # padding before first day
    check.stdout("\n" + "    " * 3, "<padding>")

    # all days but last
    for daynum in range(1, 31):
        check.stdout(format(daynum, "3d"), format(daynum, "d"))

    # final day + newline
    check.stdout("31\s*\n", "31")

    # make sure nothing follows
    remainder = str(check.stdout())
    if len(remainder) > 0:
        raise check50.Failure("expected end of output after last day")


@check50.check(cal_1_1800)
def cal_11_2021():
    """displays the calendar for Nov 2021"""
    check = check50.run("./calendar 2021 11")

    # header
    check.stdout("Nov 2021")

    # weekdays until first day of month
    check.stdout("Sun Mon Tue Wed Thu Fri Sat")

    # padding before first day
    check.stdout("\n" + "    " * 1, "<padding>")

    # all days but last
    for daynum in range(1, 30):
        check.stdout(format(daynum, "3d"), format(daynum, "d"))

    # final day + newline
    check.stdout("30\s*\n", "30")

    # make sure nothing follows
    remainder = str(check.stdout())
    if len(remainder) > 0:
        raise check50.Failure("expected end of output after last day")


@check50.check(compiles)
def rejects_wrong_command_line():
    """rejects any wrong number of command-line arguments"""
    check50.run("./calendar").stdout("Usage: ./calendar year month").exit(1)
    check50.run("./calendar 2021 11 -l").stdout("Usage: ./calendar year month").exit(1)
