# Tiles

> **Samenwerkopdracht.**
>
> Bij deze opdracht is het helemaal prima om samen te werken met één of twee medestudenten. Zorg dat je gezamenlijk op één scherm kunt kijken en echt samen het probleem probeert op te lossen. Heeft iemand een goed idee, dan moet die zorgen dat de anderen het ook begrijpen. De bedoeling is dat alle samenwerkers evenveel hebben bijgedragen aan de opdracht. Iedereen levert uiteindelijk een eigen versie in.
>
> **Je gebruikt deze opdracht om dit te leren:**
>
> - Goed begrijpen hoe 2D-arrays werken,
> - hoe je ze concreet gebruikt, en
> - hoe je nested for-loops kunt gebruiken om met 2D-arrays te werken.
>
> Na maken van de opdracht kun je extra bestuderen hoe je bovenstaande dingen hebt aangepakt.

Implement Tiles, per the below.

    $ ./tiles 3
    WELCOME TO TILES

    8  7  6

    5  4  3

    2  1  _

    Tile to move:

## Background

Tiles is a puzzle played on a square, two-dimensional board with numbered tiles that slide. The goal of this puzzle is to arrange the board's tiles from smallest to largest, left to right, top to bottom, with an empty space in board's bottom-right corner, as in the below.

![Tiles](330px-15-puzzle.svg.png){:.w-25}

Sliding any tile that borders the board's empty space in that space constitutes a "move."  Although the configuration above depicts a game already won, notice how the tile numbered 12 or the tile numbered 15 could be slid into the empty space. Tiles may not be moved diagonally, though, or forcibly removed from the board.

Although other configurations are possible, we shall assume that this game begins with the board’s tiles in reverse order, from largest to smallest, left to right, top to bottom, with an empty space in the board’s bottom-right corner. *If, however, and only if the board contains an odd number of tiles (i.e., the height and width of the board are even), the positions of tiles numbered 1 and 2 must be swapped, as in the below.* The puzzle is solvable from this configuration.

![Tiles](adapted.png){:.w-25}

## Downloading

    $ cd ~/problems
    $ wget https://github.com/minprog/programmeren-ki/raw/2021/other/tiles/dist/tiles.zip
    $ unzip tiles.zip
    $ rm tiles.zip
    $ cd tiles
    $ ls
    3x3.txt     Makefile    helpers.c   questions.txt
    4x4.txt     board.h     helpers.h   tiles.c

## Understanding

Take a look at `tiles.c`. Within this file is an entire framework for Tiles. The challenge up next is to complete this game's implementation.

But first go ahead and compile the framework. (Can you figure out how?) And, even though it's not yet finished, go ahead and run the game. (Can you figure out how?) Odds are you'll want to run it in a larger terminal window than usual, which you can open clicking the green plus (+) next to one of your code tabs and clicking *New Terminal*. Alternatively, you can full-screen the terminal window toward the bottom of CS50 IDE's UI (within the UI's "console") by clicking the *Maximize* icon in the console's top-right corner.

Anyhow, it appears that the game is at least partly functional. Granted, it's not much of a game yet. But that's where you come in!

## The Board

As you might see atop `tiles.c`, there is an included file `board.h`. This file defines the **board**, which is in our program a data structure (a 2-D array, in this case) to store the game "state" as the game progresses.

Whenever a move is made in the game, this will first result in a change to the `board` variable to reflect the new game state (a tile that's been moved). Only then, the game state is re-drawn on the screen to represent this game state. So, what's on the screen is a *representation* of what's in memory.

Given the above, it should come as no surprise that `board` is an important variable in the program. Every action that a player takes results in inspecting the `board` variable or even changing it. This way, the board variable is the central data structure of the whole program.

## Questions

Read over the code and comments in `tiles.c` and then answer the questions below in `questions.txt`, which is a (nearly empty) text file that we included for you inside of the distribution's `tiles` directory. No worries if you're not quite sure how `fprintf` or `fflush` work; we're simply using those to automate some testing.

1. Besides 4 × 4, what other dimensions does the framework allow?
1. With what sort of data structure is the game's board represented?
1. What number is used in the board data structure to signify the *empty* tile?
1. What functions do you apparently need to implement?
{: start="0"}

## Functions

Within the framework, there are many functions that implement a part of the program. Some have been left to be implemented by you! Let us guide you through them all. Part of this assignment is reading the code and making sense of it.

### `int validate_arguments(int argc, string argv[])`

This function implements a validity check for the command-line arguments. As usual, `main` gets these arguments first, but here it passes those directly to the `validate_arguments` function. That function `return`s an error code when needed --- and `main` then stops the program by also `return`ing that code.

### `void clear_screen(void)`

This function sends special "ANSI control codes" to the screen via `printf`. These codes can do more than just print letters or newlines. The control codes that we used here clear the screen and return the blinking text *cursor* to line 0, column 0.

### `void greet_user(void)`

This function calls `clear_screen` first and then prints a welcome message. It uses `usleep`, about which you can find more information in the CS50 Manual (but you will need to switch off the "less comfortable" mode before being able to find it!).

### `void init_board(void)`

Whoa, this one's `TODO`! The goal of the function is to fill the `board` variable with initial tiles in a solvable position (like you've read about above). How could you do this? Can you identify a few separate actions that have to be taken?

### `void draw_board(void)`

This function loops the `board` variable (which is a 2-D array, so we use two coordinates to loop it). For each coordinate, we call the function `draw_tile`. To finish each line (but not each tile) two newlines are printed.

### `void draw_tile(int value)`

This function draws (prints) the number for one tile to the screen. For most numbers it simply prints whatever was in the `board`. However, when the number 0 is passed to this function, this signifies the "empty tile", and an underscore `_` is printed.

### `bool move(int tile)`

And here we find another `TODO`. This function moves one particular tile, but only if it is right next to the empty tile. All you're provided is the number of the tile that is to be moved. Here's an idea on how to approach this:

1. Find, in the `board`, the coordinates of the tile that's to be moved
2. Find, in the `board`, the coordinates of the empty tile
3. Check if the empty tile is above, below, to the left or to the right of the tile to be moved, and only move (i.e. swap tiles) if that's the case.

Note that the function should `return true` when the move succeeds, and `return false` otherwise.

### `bool is_won(void)`

This function checks if the puzzle has been solved. To do this, we count all tiles in increasing order and finally check if the blank tile comes last, which means that it's in the bottom-right corner.

## Specification

So what to do?

1. Answer the questions above in `questions.txt`.
1. Implement Tiles, per the comments in `tiles.c` and the information from this specification.
{: start="0"}

## Testing

To test your implementation of `tiles`, you can certainly try playing it. (Know that you can force your program to quit by hitting ctrl-c.) Be sure that you (and we) cannot crash your program, as by providing bogus tile numbers.

You can automate execution of this game to help debugging. In fact, we have provided you with `3x3.txt` and `4x4.txt`, winning sequences of moves for a 3 × 3 board and a 4 × 4 board, respectively. To test your program with, say, the first of those inputs, execute the below.

    ./tiles 3 < 3x3.txt

(Feel free to tweak the appropriate argument to `usleep` to speed up animation.)

Note that `check50` assumes that your board's blank space is implemented in the array `board` as `0`; if you've chosen some other value, best to change to `0` for ``check50``'s sake. Also note that `check50` assumes that you're indexing into `board` a la `board[row][column]`, not `board[column][row]`.

    check50 -l minprog/programmeren-ki/2021/other/tiles
