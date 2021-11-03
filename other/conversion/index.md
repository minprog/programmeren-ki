# Temperatuurtabellen

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.


## Temperaturen

Graden Celsius C en graden Fahrenheit F staan met elkaar in verband via `F = (18C + 320) / 10` en andersom `C = (10F - 320) / 18`. Een conversietabel kan er zo uitzien:

|      C |   F|
|-------:|---:|
|      0 |  32|
|      5 |  41|
|     10 |  50|
|     15 |  59|
|     20 |  68|


## Programma

Schrijf een programma dat de gebruiker vraagt om de eenheid van temperatuur, of C van Celsius of F van Fahrenheit. Vervolgens vraagt het programma om de begintemperatuur, de eindtemperatuur en de stapsgrootte. Waarna een nette tabel wordt uitgeprint met op iedere rij de gekozen temperatuur en de temperatuur in de andere eenheid.

Vraag de gebruiker opnieuw om input als er iets anders dan C of F wordt gekozen voor de eenheid van temperatuur. Vraag de gebruiker ook opnieuw om input als er een stapgrootte kleiner dan 1 wordt ingevuld. 


## Implementation Details

Implement, in a file called `conversion.c` in a `~/problems/conversion` directory, a program that first asks the user how much change is owed and then prints the minimum number of coins with which that change can be made.

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

    $ ./conversion
    Welke eenheid van temperatuur (C of F)? C
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 20
    Wat is de stapgrootte? 5
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68

    $ ./conversion
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 10
    Wat is de stapgrootte? 2
      F |   C
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12

    $ ./conversion 
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 100
    Wat is de eindtemperatuur? 0
    Wat is de stapgrootte? 3
      F |   C

     $ ./conversion 
    Welke eenheid van temperatuur (C of F)? c
    Welke eenheid van temperatuur (C of F)? v
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 9
    Wat is de stapgrootte? -3
    Wat is de stapgrootte? 0
    Wat is de stapgrootte? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12






## Walkthrough

TBD

> Tip: zo print je een waarde uit met een vaste lengte `printf("%3d", getal)`. Is `getal` hier bijvoorbeeld `9`, dan worden er twee spaties uitgeprint voor de `9` om zo toch de opgegeven lengte 3 te krijgen.



## Getting Started

First, create a new directory (i.e., folder) called `conversion` inside of your `problems` directory, by executing

    ~/ $ mkdir ~/problems/conversion

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

    check50 -l minprog/programmeren-ki/2021/conversion

Execute the below to evaluate the style of your code using `style50`.

    style50 conversion.c


## How to submit

As soon as you're done, submit your `conversion.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `conversion.c` file (that's within your `~/problems/conversion` directory) and then select **Download**. You should find that your browser has downloaded `conversion.c`.

2. Also download `pseudocode.txt`.

3. Make sure you are signed in to **this** website!

4. In the form below, choose the files that you just downloaded.

5. Press "Submit for grading". Presto!

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
