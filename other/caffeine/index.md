# Caffeine

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.


## Greedy Algorithms

Let's talk algorithms first. You're going to implement a **greedy** algorithm, which helps us find the best solution for a given problem.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one "that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems."

What's all that mean? Well, suppose that a cashier owes a customer some change and in that cashier's drawer are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). The problem to be solved is to decide which coins and how many of each to hand to the customer. Think of a "greedy" cashier as one who wants to take the biggest bite out of this problem as possible with each coin they take out of the drawer. For instance, if some customer is owed 41¢, the biggest first (i.e., best immediate, or local) bite that can be taken is 25¢. (That bite is "best" inasmuch as it gets us closer to 0¢ faster than any other coin would.) Note that a bite of this size would whittle what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16\. That is, the remainder is a similar but smaller problem. Needless to say, another 25¢ bite would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to a bite of size 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ bite followed by one 1¢ bite, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.

It turns out that this greedy approach (i.e., algorithm) works exactly right for minimizing the amount of coins to return.


## Caffeine intake

Caffeine is a stimulant from natural sources. It can be found in various plants, like in the beans of cacao plants or in kola nuts. In moderate amounts, drinking beverages containing caffeine can help people focus. Of course, this also depends on other factors such as body weight and how often you drink caffeine-containing beverages.

You're going to write a program that takes as input the number of grams of caffeine that would be healthy for you to take at this moment, and it will output the minimum number of beverages that you will need to consume to get to that amount.

Your program will be based on four types of beverages, for which the (average, rounded) caffeine amounts are listed in the following table. The amounts are for a normal portion and are specified in milligrams.

| drink        | caffeine |
| ------------ | -------: |
| espresso     |    70 mg |
| black tea    |    30 mg |
| green tea    |    20 mg |
| cocoa        |    10 mg |

Like returning change, the caffeine problem is also easiest to solve in a greedy fashion. That means that to make a list of beverages to drink, you always start by selecting the beverage with the highest caffeine amount (that is still less than the amount required). And then repeat.


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

    $ ./caffeine
    Amount in grams: 0.10
    1 espresso
    1 black tea
    0 green tea
    0 cocoa

    $ ./caffeine
    Amount in grams: 0.01
    0 espresso
    0 black tea
    0 green tea
    1 cocoa

If the amount of caffeine is worth more than 2 cups of coffee (140 mg), an additional warning is displayed.

    $ ./caffeine
    Amount in grams: 0.25
    3 espresso
    1 black tea
    0 green tea
    1 cocoa
    Warning! This might not be a healthy amount to consume.

    $ ./caffeine
    Amount in grams: 0.40
    5 espresso
    1 black tea
    1 green tea
    0 cocoa
    Warning! This might not be a healthy amount to consume.

And if an amount less than 0.01 is entered, the program should ask again.

    $ ./caffeine
    Amount in grams: 0.005
    Amount in grams: -1.0
    Amount in grams: 0.01
    0 espresso
    0 black tea
    0 green tea
    1 cocoa


## Walkthrough

TBD


## Getting Started

First, create a new directory (i.e., folder) called `caffeine` inside of your `problems` directory, by executing

    ~/ $ mkdir ~/problems/caffeine

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

    check50 -l minprog/programmeren-ki/2021/caffeine

Execute the below to evaluate the style of your code using `style50`.

    style50 caffeine.c


## How to submit

As soon as you're done, submit your `caffeine.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `caffeine.c` file (that's within your `~/problems/caffeine` directory) and then select **Download**. You should find that your browser has downloaded `caffeine.c`.

2. Also download `pseudocode.txt`.

3. Make sure you are signed in to **this** website!

4. In the form below, choose the files that you just downloaded.

5. Press "Submit for grading". Presto!

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
