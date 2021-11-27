# Sort

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Implement a program that sorts numbers, per the below.

    $ ./generate 5 | ./sort
    1122
    51316
    58314
    60815
    64289

## Distribution

    $ wget https://github.com/minprog/programmeren-ki/raw/2021/other/sort/dist/sort.zip
    $ unzip sort.zip
    $ rm sort.zip
    $ cd sort
    $ ls
    Makefile    sort.c      generate.c  helpers.c   helpers.h


### Understanding

Implemented in `generate.c` is a program that uses a "pseudorandom-number generator" (via a function called `drand48`) to generate a whole bunch of random (well, pseudorandom, since computers can't actually generate truly random) numbers, one per line, each of which is in [0, `LIMIT`), where `LIMIT` is a constant defined within the file, so to speak. That is, each is greater than or equal to 0 and less than `LIMIT`.

Go ahead and compile this program by executing the command below.

    make generate

Now run the program you just compiled by executing the command below.

    ./generate

You should be informed of the program's proper usage, per the below.

    Usage: generate n [s]

As this output suggests, this program expects one or two command-line arguments. The first, `n`, is required; it indicates how many pseudorandom numbers you'd like to generate. The second, `s`, is optional, as square brackets imply; if supplied, it represents the value that the pseudorandom-number generator should use as its "seed." A seed is simply an input to a pseudorandom-number generator that influences its outputs. For instance, if you seed `drand48` by first calling `srand48` (another function whose purpose is to "seed" `drand48`) with an argument of, say, `0`, and then call `drand48` itself three times, `drand48` might return `0.170828`, then `0.749902`, then `0.096372`. But if you instead seed `drand48` by first calling `srand48` with an argument of, say, `1`, and then call `drand48` itself three times, `drand48` might instead return `0.041630`, then `0.454492`, then `0.834817`. But if you re-seed `drand48` by calling `srand48` again with an argument of `0`, the next three times you call `drand48`, you'll again get `0.170828`, then `0.749902`, then `0.096372`! See, not so random.

Go ahead and run this program again, this time with a value of, say, `10` for `n`, as in the below; you should see a list of 10 pseudorandom numbers.

    ./generate 10

Run the program a third time using that same value for `n`; you should see a different list of 10 numbers. Now try running the program with a value for `s` too (e.g., `0`), as in the below.

    ./generate 10 0

Now run that same command again:

    ./generate 10 0

Bet you saw the same "random" sequence of ten numbers again? Yup, that's what happens if you don't vary a pseudorandom number generator's initial seed.

Now take a look at `generate.c` itself. (Remember how?) Comments atop that file explain the program's overall functionality. But it looks like we forgot to comment the code itself. Read over the code carefully until you understand each line and then comment our code for us, replacing each `TODO` with a phrase that describes the purpose or functionality of the corresponding line(s) of code. (Know that an `unsigned int` is just an `int` that cannot be negative.) And for more details on `drand48` and `srand48`, recall that you can execute:

    man drand48

and:

    man srand48

Once done commenting `generate.c`, re-compile the program to be sure you didn't break anything by re-executing the command below.

    make generate

If `generate` no longer compiles properly, take a moment to fix what you broke!

Now, recall that `make` automates compilation of your code so that you don't have to execute `clang` manually along with a whole bunch of switches. Notice, in fact, how `make` just executed a pretty long command for you, per the tool's output. However, as your programs grow in size, `make` won't be able to infer from context anymore how to compile your code; you'll need to start telling `make` how to compile your program, particularly when they involve multiple source (i.e., `.c`) files. And so we'll start relying on "Makefiles," configuration files that tell `make` exactly what to do.

How did `make` know how to compile `generate` in this case? It actually used a configuration file that we wrote. Go ahead and look at the file called `Makefile` that's in the same directory as `generate.c`. This `Makefile` is essentially a list of rules that we wrote for you that tells make how to build generate from `generate.c` for you. The relevant lines appear below.

    generate: generate.c
        clang -ggdb3 -O0 -std=c11 -Wall -Werror -o generate generate.c

The first line tells `make` that the "target" called `generate` should be built by invoking the second line's command. Know that the leading whitespace on that second line is not a sequence of spaces but, rather, a tab. Unfortunately, `make` requires that commands be preceded by tabs, so be careful not to change them to spaces, else you may encounter strange errors! The `-Werror` flag, recall, tells `clang` to treat warnings (bad) as though they're errors (worse) so that you're forced (in a good, instructive way!) to fix them.

Now take a look at `sort.c`. Notice that this program expects a single command-line argument: a "needle" to search for in a "haystack" of values. Once done looking over the code, go ahead and compile the program by executing the command below.

    make sort

Notice, per that command's output, that `make` actually executed the below for you.

    clang -ggdb3 -O0 -std=c11 -Wall -Werror -o sort sort.c helpers.c -lcs50 -lm

Notice further that you just compiled a program comprising not one but two `.c` files: `helpers.c` and `sort.c`. How did `make` know what to do? Well, again, open up `Makefile` to see the man behind the curtain. The relevant lines appear below.

    sort: sort.c helpers.c helpers.h
        clang -ggdb3 -O0 -std=c11 -Wall -Werror -o sort sort.c helpers.c -lcs50 -lm

Per the dependencies implied above (after the colon), any changes to `sort.c`, `helpers.c`, or `helpers.h` will compel `make` to rebuild `sort` the next time it's invoked for this target.

Go ahead and run this program by executing, say, the below.

    ./sort

You'll be prompted to provide some integers. As soon as you tire of providing integers, hit **ctrl-d** to send the program an `EOF` (end-of-file) character. That character will compel `get_int` from the CS50 Library to return `INT_MAX`, a constant that, per `sort.c`, will compel `sort` to stop prompting for integers. And then it goes about sorting the integers and printing them, in order. At least, it should, but it won't sort anything yet! That's where you come in. More on your role in a bit.

It turns out you can automate this process of providing integers, though, by "piping" the output of `generate` into `sort` as input. For instance, the command below passes 1,000 pseudorandom numbers to `sort`, which then searches those values for `42`.

    ./generate 1000 | ./sort

Note that, when piping output from `generate` into `sort` in this manner, you won't actually see ``generate``'s numbers, but you will see ``sort``'s prompts.

Alternatively, you can "redirect" ``generate``'s output to a file with a command like the below.

    ./generate 1000 > numbers.txt

You can then redirect that file's contents as input to `sort` with the command below.

    ./sort < numbers.txt

Let's finish looking at that `Makefile`. Notice the line below.

    all: sort generate

This target implies that you can build both `generate` and `sort` simply by executing the below.

    make all

Even better, the below is equivalent (because `make` builds a ``Makefile``'s first target by default).

    make

If only you could whittle this whole problem set down to a single command! Finally, notice these last lines in `Makefile`:

    clean:
        rm -f *.o a.out core sort generate

This target allows you to delete all files ending in `.o` or called `core` (more on that soon!), `sort`, or `generate` simply by executing the command below.

    make clean

Be careful not to add, say, `*.c` to that last line in `Makefile`! (Why?)

Notice now that, in `sort.c`, `main` calls `sort`, a function declared in `helpers.h`. Unfortunately, we forgot to implement that function fully in `helpers.c`! Indeed, take a peek at `helpers.c`, and you'll see that `sort` always returns without doing anything else.

To be sure, we could have put the contents of `helpers.h` and `helpers.c` in `find.c` itself. But it's sometimes better to organize programs into multiple files, especially when some functions are essentially "utility functions" that might later prove useful to other programs as well, much like those in the CS50 Library.

Notice too, per `helpers.h`, that the prototype for `sort` is:

    void sort(int values[], int n);

The function takes an array, `values`, as one of the arguments, as well as an integer, `n`, the size of that array. That's because, when passing an array to a function, you have to pass in its size separately; you can't infer an array's size from the array itself.


## Specification

Complete the implementation of the program `sort` by completing the implementation of the function `sort` in `helpers.c`.

Sort must be implemented using the following algorithm, which is **not** any of the algorithms discussed in earlier assignments. However, many of the sorting algorithms do indeed look quite alike.

**Do not attempt do this assignment before studying the other sorting algorithms very well.**

*   The algorithm must consider each number in the array from left to right, and progressively sort the numbers.
    * This means that, in each step, more numbers get sorted from left to right, unless they're already sorted, of course.
    * This also means that the algorithm need never consider the last number in the array, because as soon as that number is reached, it has already been sorted while considering the other numbers. (In other words, if `n-1` numbers are indeed sorted, the last number would by definition also be sorted.)
*   Then **for each** of the numbers that we consider from left to right, consider **all** numbers to the right of it.
    * For each **combination** of numbers, if the first one is larger, swap those numbers.
*   You may not alter the function's declaration. Its prototype must remain:

        void sort(int values[], int n);
*   You may not use recursion to perform the sort, i.e. the function `sort` may never call itself.

Be sure to translate this description of the algorithm's properties to some form of pseudocode before you take to translating it into C.


## Usage

Your program should behave per the examples below. (`^d` represents the ctrl-d character described above)

    $ ./sort
    2
    1
    ^d
    1
    2

    $ ./sort
    50
    42
    ^d
    42
    50

It's up to you to test using different test cases, i.e. different numbers and different *amounts* of numbers.


### Automated tests

When you're completely satisfied that your program works as expected using manual testing, you can run `check50` to check for corner cases that may have escaped your attention.

    check50 -l minprog/programmeren-ki/2021/other/sort


## How to submit

When you're done, submit your implementation, below!

1. Download `helpers.c` from the `~/problems/sort` directory in your IDE.

3. In the form below, choose the files that you just downloaded.
