/*
 * Logging helpers for Tiles game
 */

#include <stdio.h>

#include "board.h"

FILE *log_file;

void start_log()
{
    // Open log
    log_file = fopen("log.txt", "w");
    if (log_file == NULL)
    {
        // return 3;
    }
}

void log_board()
{
    // Log the current state of the board (for testing)
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            fprintf(log_file, "%i", board[i][j]);
            if (j < d - 1)
            {
                fprintf(log_file, "|");
            }
        }
        fprintf(log_file, "\n");
    }
    fflush(log_file);
}

void end_log()
{
    // Close log
    fclose(log_file);
}

void log_move(int tile)
{
    // Log move (for testing)
    fprintf(log_file, "%i\n", tile);
    fflush(log_file);
}
