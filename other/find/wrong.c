/**
* Checks if search returns false upon non-positive size value
*/

#include "helpers.h"

int main(void)
{
    int needle = 4;
    int haystack[3] = {1, 2, 4};

    return search(needle, haystack, -1);
}
