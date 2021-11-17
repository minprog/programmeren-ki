import check50
import check50.c

@check50.check()
def exists():
    """tiles.c exists."""
    check50.exists("tiles.c")


@check50.check(exists)
def compiles():
    """tiles.c compiles."""
    # Remove sleeps from student code
    check50.run("sed -i='' '/#include <unistd.h>/a \\\n#define usleep(x)' tiles.c").exit()

    # check50.c.compile("tiles.c", lcs50=True)
    check50.run("make").exit(0)


@check50.check(compiles)
def init3():
    """initializes a 3x3 board correctly."""
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "1", "[_0]"]

    check = check50.run("./tiles 3")
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(compiles)
def init4():
    """initializes a 4x4 board correctly."""

    # check for board without swapped tiles
    invalid_board = ["15", "14", "13", "12",
                     "11", "10", "9", "8",
                     "7", "6", "5", "4",
                     "3", "2", "1", "[_0]"]

    check = check50.run("./tiles 4")

    try:
        for tile in invalid_board:
            check.stdout(tile)
        check.stdout("\n")
    except:
        # this test is supposed to raise an exception
        pass
    else:
        # raise exception if the incorrect board is found
        raise check50.Failure("board initialized incorrectly", help="did you remember to swap the last two tiles?")


    # check for fully correct board
    board = ["15", "14", "13", "12",
             "11", "10", "9", "8",
             "7", "6", "5", "4",
             "3", "1", "2", "[_0]"]

    check = check50.run("./tiles 4")
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def invalid():
    """3x3 board: catches moving 2, 4, 5, 6, 7, 8 as illegal moves."""
    moves = ["2", "4", "5", "6", "7", "8"]

    check = check50.run("./tiles 3")

    for move in moves:
        check.stdin(move).stdout("Illegal move.")

    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "1", "[_0]"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def move_up2():
    """3x3 board: move blank up twice."""
    check = check50.run("./tiles 3").stdin("3")
    board = ["8", "7", "6",
             "5", "4", "[_0]",
             "2", "1", "3"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

    check.stdin("6")
    board = ["8", "7", "[_0]",
             "5", "4", "6",
             "2", "1", "3"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def move_left2():
    """3x3 board: move blank left twice."""
    check = check50.run("./tiles 3").stdin("1")
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "[_0]", "1"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

    check.stdin("2")
    board = ["8", "7", "6",
             "5", "4", "3",
             "[_0]", "2", "1"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def move_left_right():
    """3x3 board: move blank left then right."""
    check = check50.run("./tiles 3").stdin("1")
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "[_0]", "1"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

    check.stdin("1")
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "1", "[_0]"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def move_up_down():
    """3x3 board: move blank up then down."""
    check = check50.run("./tiles 3").stdin("3")
    board = ["8", "7", "6",
             "5", "4", "[_0]",
             "2", "1", "3"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

    check.stdin("3")
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "1", "[_0]"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def invalid_center():
    """3x3 board: move blank left (tile 1) then up (tile 4), then try to move tiles 1, 2, 6, 8"""
    # move 1
    check = check50.run("./tiles 3").stdin("1")

    # check resulting board
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "[_0]", "1"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

    # move 4
    check.stdin("4")

    # check resulting board
    board = ["8", "7", "6",
             "5", "[_0]", "3",
             "2", "4", "1"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

    # try moving all corner tiles
    for move in ["1", "2", "6", "8"]:
        check.stdin(move).stdout("Illegal move.")

    # check that board state didn't change
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")


@check50.check(init3)
def solve3():
    """solves a 3x3 board."""
    steps = ["3","4","1","2","5","8","7","6",
             "4","1","2","5","8","7","6","4",
             "1","2","4","1","2","3","5","4",
             "7","6","1","2","3","7","4","8",
             "6","4","8","5","7","8","5","6",
             "4","5","6","7","8","6","5","4",
             "7","8"]

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "[_0]"]

    check = check50.run("./tiles 3")

    for step in steps:
        check.stdout("Tile to move:")
        check.stdin(step, prompt=False)

    for tile in board:
        check.stdout(tile)
    check.stdout("ftw!")


@check50.check(init4)
def solve4():
    """solves a 4x4 board."""
    steps = ["4","5","6","1","2","4","5","6",
             "1","2","3","7","11","10","9","1",
             "2","3","4","5","6","8","1","2",
             "3","4","7","11","10","9","14",
             "13","12","1","2","3","4","14",
             "13","12","1","2","3","4","14",
             "13","12","1","2","3","4","12",
             "9","15","1","2","3","4","12","9",
             "13","14","9","13","14","7","5",
             "9","13","14","15","10","11","5",
             "9","13","7","11","5","9","13",
             "7","11","15","10","5","9","13",
             "15","11","8","6","7","8","14",
             "12","6","7","8","14","12","6",
             "7","8","14","15","11","10","6",
             "7","8","12","15","11","10","15",
             "11","14","12","11","15","10",
             "14","15","11","12"]

    board = ["1", "2", "3", "4",
             "5", "6", "7", "8",
             "9", "10", "11", "12",
             "13", "14", "15", "[_0]"]

    check = check50.run("./tiles 4")

    for step in steps:
        check.stdout("Tile to move:")
        check.stdin(step, prompt=False)

    for tile in board:
        check.stdout(tile)
    check.stdout("ftw!")
