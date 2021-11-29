# Find

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Implement a program that finds a number among numbers, per the below.

    $ ./generate 1000 | ./find 42
    Didn't find needle in haystack.


## Distribution

    $ wget https://github.com/minprog/cs50x/raw/2021/find/dist/find.zip
    $ unzip find.zip
    $ rm find.zip
    $ cd find
    $ ls
    Makefile    find.c      generate.c  helpers.c   helpers.h


### Understanding

Remember `generate.c`? In a previous assignment, you used it for testing and you commented it.

Now take a look at `find.c`. Notice that this program expects a single command-line argument: a "needle" to search for in a "haystack" of values. Once done looking over the code, go ahead and compile the program by executing the command below.

    make find

Go ahead and run this program by executing, say, the below.

    ./find 13

You'll be prompted to provide some hay (i.e., some integers), one "straw" at a time. As soon as you tire of providing integers, hit ctrl-d to send the program an `EOF` (end-of-file) character. That character will compel `get_int` from the CS50 Library to return `INT_MAX`, a constant that, per `find.c`, will compel `find` to stop prompting for hay. The program will then look for that needle in the hay you provided, ultimately reporting whether the former was found in the latter. In short, this program searches an array for some value. At least, it should, but it won't find anything yet! That's where you come in. More on your role in a bit.

It turns out you can automate this process of providing hay, though, by "piping" the output of `generate` into `find` as input. For instance, the command below passes 1,000 pseudorandom numbers to `find`, which then searches those values for `42`.

    ./generate 1000 | ./find 42

Note that, when piping output from `generate` into `find` in this manner, you won't actually see ``generate``'s numbers, but you will see ``find``'s prompts.

Alternatively, you can "redirect" ``generate``'s output to a file with a command like the below.

    ./generate 1000 > numbers.txt

You can then redirect that file's contents as input to `find` with the command below.

    ./find 42 < numbers.txt

Notice now that, in `find.c`, `main` calls `search`, a function declared in `helpers.h`. Unfortunately, we forgot to implement that function fully in `helpers.c`! Indeed, take a peek at `helpers.c`, and you'll see that `search` always returns `false`, whether or not `value` is in `values`. To be sure, we could have put the contents of `helpers.h` and `helpers.c` in `find.c` itself. But it's sometimes better to organize programs into multiple files, especially when some functions are essentially "utility functions" that might later prove useful to other programs as well, much like those in the CS50 Library.

Notice too, per `helpers.h`, that the prototype for `search` is:

    bool search(int value, int values[], int n);

And the prototype for `sort` is:

    void sort(int values[], int n);

Both functions take an array, `values`, as one of their arguments as well as an integer, `n`, the size of that array. That's because, when passing an array to a function, you have to pass in its size separately; you can't infer an array's size from the array itself.


## Specification

Complete the implementation of `find` by completing the implementation of `search` and `sort` in `helpers.c`.

* Search must be implemented as [Binary Search](https://www.youtube.com/watch?v=T98PIp4omUA).

    *   Your implementation must return `false` immediately if `n` is non-positive.

    *   Your implementation must return `true` if `value` is in `values` and `false` if `value` is not in `values`.

    *   You may not alter the function's declaration. Its prototype must remain:

            bool search(int value, int values[], int n);

* Sort must be implemented as [Counting Sort](https://en.wikipedia.org/wiki/Counting_sort).

    *   Your implemenation must sort, from smallest to largest, the array of numbers that it's passed.

    *   You may not alter the function's declaration. Its prototype must remain:

            void sort(int values[], int n);


## Usage

Your program should behave per the examples below. (`^d` represents the ctrl-d character described above)

    $ ./find 42
    50
    43
    ^d
    Didn't find needle in haystack.

    $ ./find 42
    50
    42
    ^d
    Found needle in haystack!


## Testing

When ready to check the correctness of your program, try running the command below.

    ./generate 1000 50 | ./find 127

Because one of the numbers outputted by `generate`, when seeded with `50`, is `127`, your code should find that "needle"! By contrast, try running the command below as well.

    ./generate 1000 50 | ./find 128

Because `128` is not among the numbers outputted by `generate`, when seeded with `50`, your code shouldn't find that needle. Best to try some other tests as well, as by running `generate` with some seed, taking a look at its output, then piping that same output to `find`, looking for a "needle" you know to be among the "hay".

Incidentally, note that `main` in `find.c` is written in such a way that `find` returns `0` if the needle is found, else it returns `1`. You can check the so-called "exit code" with which `main` returns by executing

    echo $?

after running some other command. For instance, assuming your implementation of `search` is correct, if you run

    ./generate 1000 50 | ./find 127
    echo $?

you should see `0`, since `127` is, again, among the 1,000 numbers outputted by `generate` when seeded with `50`, and so `search` (written by you) should return `true`, in which case `main` (written by us) should return (i.e., exit with) `0`. By contrast, assuming your implementation of `search` is correct, if you run

    ./generate 1000 50 | ./find 128
    echo $?

you should see `1`, since `128` is, again, not among the 1,000 numbers outputted by `generate` when seeded with `50`, and so `search` (written by you) should return `false`, in which case `main` (written by us) should return (i.e., exit with) `1`. Make sense?


### Automated tests

When you're completely satisfied that your program works as expected using manual testing, you can run `check50` to check for corner cases that may have escaped your attention.

    check50 -l minprog/programmeren-ki/2020/other/find


## How to submit

When you're done, submit your implementation, below!

1. Download `helpers.c` from the `~/problems/find` directory in your IDE.

3. In the form below, choose the files that you just downloaded.
