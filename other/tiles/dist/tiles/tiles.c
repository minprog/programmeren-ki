/*
 * Implements Tiles (for a puzzle size of d x d)
 */

#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "board.h"
#include "helpers.h"

#define COLOR "\033[32m"

// Prototypes
int validate_arguments(int argc, string argv[]);

void clear_screen(void);
void greet_user(void);
void draw_board(void);
void draw_tile(int value);

void init_board(void);
bool move(int tile);
bool is_won(void);

int main(int argc, string argv[])
{
    // Validate arguments, else stop program
    int error = validate_arguments(argc, argv);
    if (error > 0)
    {
        return error;
    }

    // Start logging for testing purposes
    start_log();

    // Greet user with instructions
    greet_user();

    // Initialize the board
    init_board();

    // Accept moves until game is won
    while (true)
    {
        // Clear the screen
        clear_screen();

        // Draw the current state of the board
        draw_board();

        // Log the current board for testing purposes
        log_board();

        // Check for win
        if (is_won())
        {
            printf("ftw!\n");
            break;
        }

        // Prompt for move
        int tile = get_int("Tile to move: ");

        // Quit if user inputs 0(for testing)
        if (tile == 0)
        {
            break;
        }

        // Log the requested move for testing purposes
        log_move(tile);

        // Move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // Sleep thread for animation's sake
        usleep(50000);
    }

    // Stop logging to neatly close logfile
    end_log();

    // Success
    return 0;
}

// Runs a couple of checks on the command-line arguments and prints usage hints
int validate_arguments(int argc, string argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: tiles d\n");
        return 1;
    }

    // Ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board dimension d must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }
    return 0;
}

// Clears screen using ANSI escape sequences
void clear_screen(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

// Greets player
void greet_user(void)
{
    clear_screen();
    printf("WELCOME TO TILES\n");
    usleep(2000000);
}

// Initializes the game 's board with tiles numbered 1 through d*d - 1
//  (i.e., fills 2-D array with values but does not actually print them)
void init_board(void)
{
    // TODO
}

// Prints the board in its current state
void draw_board(void)
{
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            draw_tile(board[i][j]);
        }
        printf("\n\n");
    }
}

// Prints a single tile's number, or _ in case of empty tile
void draw_tile(int value)
{
    if (value == 0)
    {
        printf("  _  ");
    }
    else
    {
        printf("%3d  ", value);
    }
}

// If tile borders empty space, moves tile and returns true, else returns false
bool move(int tile)
{
    // TODO
    return false;
}

// Returns true if game is won (i.e., board is in winning configuration), else false
bool is_won(void)
{
    int number = 1;

    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            if (number == d * d && board[i][j] == 0)
            {
                return true;
            }
            else if (board[i][j] != number)
            {
                return false;
            }
            number++;
        }
    }
    
    // if all else is correct, we should never reach this line
    return false;
}
