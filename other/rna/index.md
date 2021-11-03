# RNA

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.


## Eiwitsynthese

Eiwitsynthese is het proces waarbij eiwitten worden gemaakt op basis van de informatie in het DNA. Simpel gezegd is eiwitsynthese het maken van een eiwit in een menselijke cel. De eerste stap van eiwitsynthese is de transcriptie van DNA naar RNA. (Je hoeft voorgaande niet te begrijpen.)

DNA bestaat uit verschillende moleculen, waaronder 4 nucleotiden die de DNA-code vormen: Adenine (A), Guanine (G), Cytosine (C) en Thymine (T). RNA is een zogenaamde *complementaire* transcriptie van DNA. De complementaire nucleotide van Adenine is Uracil (U), van Guanine is Cytosine, van Cysotine is Guanine en van Thymine is Adenine.

Een complementaire RNA-keten kan dus volgens een vast patroon beredeneerd worden uit de DNA-keten. Zo geeft een DNA-keten `ATGC` altijd de RNA-keten `UACG` als je bovenstaande regels toepast.


## Transcriptie

Schrijf een programma dat een keten van DNA aanneemt en de complementaire RNA-keten print. Je mag aannemen dat de DNA-keten altijd in hoofdletters wordt ingevuld. Het programma print een error message als deze een ongeldige nucleotide bevat (dus een andere letter dan A, G, C of T).




## Implementation Details

Implement, in a file called `caffeine.c` in a `~/problems/caffeine` directory, a program that first asks the user how much change is owed and then prints the minimum number of coins with which that change can be made.

*   Use `get_float` to get the user's input and `printf` to output your answer.

*   You need not try to check whether a user's input is too large to fit in a `float`. Using `get_float` alone will ensure that the user's input is indeed a floating-point (or integral) value but not that it is non-negative.

*   If the user fails to provide a value of at least 0.01 grams, your program should re-prompt the user for a valid amount again and again until the user complies.

*   So that we can automate some tests of your code, be sure that your program's output is exactly as specified in the examples, below. Don't forget to add `\n` after each line of output!

*   Beware the inherent imprecision of floating-point values. Recall `floats.c` from class, wherein, if `x` is `2`, and `y` is `10`, `x / y` is not precisely two tenths! And so, before doing calculations, you'll probably want to convert the user's inputted amount in grams to milligrams to avoid tiny errors that might otherwise add up!

    *   To do this, multiply the input amount by 1000 to get the number of milligrams. Take care to use `round()` to round your answer.
    
    *   And then save the number of milligrams in a variable of type `int`.

To get started, read through the examples below, then watch the Walkthrough and finally follow the instructions under the Getting Started header.


## Examples

Ultimately, your program should behave per the examples below.

    $ ./rna
    DNA-keten: ATGC
    Dit is de bijbehorende RNA-keten: UACG

    $ ./rna
    DNA-keten: AAF
    Ongeldige DNA-keten

    $ ./rna
    DNA-keten: AAGGTTCCAA
    Dit is de bijbehorende RNA-keten: UUCCAAGGUU



## Walkthrough

TBD


## Getting Started

First, create a new directory (i.e., folder) called `rna` inside of your `problems` directory, by executing

    ~/ $ mkdir ~/problems/rna

To start, you'll create a file called `pseudocode.txt` to help you analyze the problem. You will submit this analysis together with the final implementation in C.

Write in `pseudocode.txt` some pseudocode that implements this program, even if not (yet!) sure how to write it in code. There's no one right way to write pseudocode, but short English sentences suffice. Recall how we wrote pseudocode for finding Mike Smith! Odds are your pseudocode will use (or imply using!) one or more functions, conditions, Boolean expressions, loops, and/or variables.


### How to Test Your Code

Does your code work as prescribed when you input

*   `-1.00` (or other negative numbers)?
*   `0.00`?
*   `0.01` (or other positive numbers)?
*   letters or words?
*   no input at all, when you only hit Enter?

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 -l minprog/programmeren-ki/2021/rna

Execute the below to evaluate the style of your code using `style50`.

    style50 rna.c


## How to submit

As soon as you're done, submit your `caffeine.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `rna.c` file (that's within your `~/problems/rna` directory) and then select **Download**. You should find that your browser has downloaded `rna.c`.

2. Also download `pseudocode.txt`.

3. Make sure you are signed in to **this** website!

4. In the form below, choose the files that you just downloaded.

5. Press "Submit for grading". Presto!

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
