# RNA

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.


## Eiwitsynthese

Eiwitsynthese is het proces waarbij eiwitten worden gemaakt op basis van de informatie in het DNA. Simpel gezegd is eiwitsynthese het maken van een eiwit in een menselijke cel. De eerste stap van eiwitsynthese is de transcriptie van DNA naar RNA. (Je hoeft voorgaande niet te begrijpen.)

DNA bestaat uit verschillende moleculen, waaronder 4 nucleotiden die de DNA-code vormen: Adenine (A), Guanine (G), Cytosine (C) en Thymine (T). RNA is een zogenaamde *complementaire* transcriptie van DNA. De complementaire nucleotide van Adenine is Uracil (U), van Guanine is Cytosine, van Cysotine is Guanine en van Thymine is Adenine.

Een complementaire RNA-keten kan dus volgens een vast patroon beredeneerd worden uit de DNA-keten. Zo geeft een DNA-keten `ATGC` altijd de RNA-keten `UACG` als je bovenstaande regels toepast.


## Opdracht

Schrijf een programma dat op de command line een keten van DNA aanneemt van willkeurige lengte en de complementaire RNA-keten print. Het programma print een error message bij ongeldige invoer.


## Implementation Details

*   Implement your program in a file called `rna.c` in a directory called `rna`.

*   Your program must accept a single command-line argument, which is a string of letters.

*   Your program must be case-insensitive: capitalized letters must be interpreted the same as lowercase letters. RNA output, though, must be all capitalized.

*   If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` (which tends to signify an error) immediately.

*   If any of the characters of the command-line argument is not a valid DNA nucleotide letter, your program should print the message `Invalid DNA` and return from `main` a value of `1`.

*   So that we can automate some tests of your code, be sure that your program's output is exactly as specified in the examples, below. Don't forget to add `\n` after each line of output!

*   As with all assignments, your solution may not be hardcoded for the checks. However, the translation from DNA to RNA is fixed, so don't worry about hardcoding the translation of a single letter!

To get started, read through the examples below and finally follow the instructions under the Getting Started header.


## Examples

Ultimately, your program should behave per the examples below.

    $ ./rna ATGC
    UACG

    $ ./rna AAGGTTCCAA
    UUCCAAGGUU

    $ ./rna CGaT
    GCUA

In case of user error, your program should respond appropriately, and return exit code 1.

    $ ./rna AAF
    Invalid DNA

    $ ./rna
    Usage: ./rna ATGC


## Getting Started

First, create a new directory (i.e., folder) called `rna` inside of your `problems` directory, by executing

    ~/ $ mkdir ~/problems/rna

To start, you'll create a file called `pseudocode.txt` to help you analyze the problem. You will submit this analysis together with the final implementation in C.

Write in `pseudocode.txt` some pseudocode that implements this program, even if not (yet!) sure how to write it in code.


### How to Test Your Code

Does your code work as prescribed when you input invalid DNA? Does it correctly translate DNA to RNA? You should be able to verify this yourself using the examples above. If you find it hard to be precise, make sure that you keep trying, because `check50` will not always be with you!

You can execute the below to evaluate the correctness of your code using `check50`.

    check50 -l minprog/programmeren-ki/2021/other/rna

Execute the below to evaluate the style of your code using `style50`.

    style50 rna.c


## How to submit

As soon as you're done, submit your `rna.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `rna.c` file (that's within your `~/problems/rna` directory) and then select **Download**. You should find that your browser has downloaded `rna.c`.

2. Also download `pseudocode.txt`.

3. Make sure you are signed in to **this** website!

4. In the form below, choose the files that you just downloaded.

5. Press "Submit for grading". Presto!

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
