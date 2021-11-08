# Caffeine

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.


## Greedy Algorithms

Let's talk algorithms first. You're going to implement a **greedy** algorithm, which helps us find the best solution for a given problem.

The key idea of greedy algorithms is that for each step towards the solution, they take the option that's worth the most.

Say you've won 3 minutes of free shopping at an electronics store. Even though your shopping cart is of limited size, you will never have use for everything that you put in there. You might as well sell a few items for cash. Obviously, **if getting cash is your goal**, you will load the most expensive items in your cart first. This guarantees the best outcome: the most cash.

You can use greedyness to your advantage in other situations. Suppose that a cashier owes a customer some change and in that cashier's drawer are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). The problem to be solved is to decide which coins and how many of each to hand to the customer. Normally, cashiers will want to **minimize the number of total coins** to hand back, because this is easiest to handle and because rolls of coins actually cost money to buy at the bank.

So. If some customer is owed 41¢, the largest coin that can be taken is 25¢. It gets us closer to 0¢ faster than any other coin would. So this whittles what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16\. That is, the *remainder* is a similar but smaller problem. Needless to say, another 25¢ would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to returning 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ coin followed by one 1¢ coin, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.

It turns out that this greedy approach (i.e., algorithm) works exactly right for minimizing the amount of coins to return.

Let's use this algorithm for an entirely different problem.


## Caffeine intake

Caffeine is a stimulant from natural sources. It can be found in various plants, like in the beans of cacao plants or in kola nuts. In moderate amounts, drinking beverages containing caffeine can help people focus without negative effects. (This also depends on other factors such as body weight and how often you drink caffeine-containing beverages.)

You're going to write a program that takes as input the number of grams of caffeine that would be healthy for you to take at this moment, and it will output the number and types of beverages that you will need to consume to get to that amount.

Your program will be based on four types of beverages, for which the (rough, average, and rounded) caffeine amounts are listed in the following table. The amounts are for a normal portion of each drink and are specified in milligrams.

| drink                | caffeine |
| -------------------- | -------: |
| espresso             |    70 mg |
| black tea            |    30 mg |
| green tea            |    20 mg |
| cocoa                |    10 mg |
| piece of chocolate   |     1 mg |

Like returning change, the caffeine problem is easiest to solve in a greedy fashion. That means that to make a list of beverages to drink, you always start by selecting the beverage with the highest caffeine amount (that is still less than the amount required). And then repeat.


## Implementation Details

**Before you start coding, write some pseudocode to design your approach. Read this section, peruse the examples below, and then follow the instructions in the Getting Started section.**

Implement, in a file called `caffeine.c` in a `~/problems/caffeine` directory, a program that first asks the user how much caffeine is required and then prints the list of drinks to take, and the total number of drinks that is in the list.

*   Use `get_float` to get the user's input and `printf` to output your answer.

    *   You need not try to check whether a user's input is too large to fit in a `float`. Using `get_float` alone will ensure that the user's input is indeed a floating-point (or integral) value but not that it is non-negative.

    *   If the user fails to provide a value of at least 0.001 grams, your program should re-prompt the user for a valid amount again and again until the user complies. Recall what loop to use for this situation? ([Link to flow-control statements in the book](http://www.beej.us/guide/bgc/html/split/variables-and-statements.html#flow-control))

*   Beware the inherent imprecision of floating-point values. Recall `floats.c` from class, wherein, if `x` is `2`, and `y` is `10`, `x / y` is not precisely two tenths! And so, before doing calculations, you'll probably want to convert the user's inputted amount in grams to milligrams to avoid tiny errors that might otherwise add up!

    *   To do this, multiply the input amount by 1000 to get the number of milligrams. Take care to use `round()` to round your answer. ([Link to round in the manual](https://manual.cs50.io/3/round))
    
    *   And then save the number of milligrams in a variable of type `int`.

*   So that we can automate some tests of your code, be sure that your program's output is exactly as specified in the examples, below. Don't forget to add `\n` after each line of output!


## Examples

Ultimately, your program should behave per the examples below. Notice the `drink`/`drinks` pluralization in the last line of output!

    $ ./caffeine
    Amount in grams: 0.10
    1 espresso
    1 black tea
    That makes 2 drinks in total

    $ ./caffeine
    Amount in grams: 0.01
    1 cocoa
    That makes 1 drink in total

    $ ./caffeine
    Amount in grams: 0.25
    3 espresso
    1 black tea
    1 cocoa
    That makes 5 drinks in total

And if an amount of 0 or less is entered, the program should ask again.

    $ ./caffeine
    Amount in grams: -1.0
    Amount in grams: 0.01
    1 cocoa
    That makes 1 drink in total

Pieces of chocolate do not count for the total number of drinks.

    $ ./caffeine
    Amount in grams: 0.001
    1 piece of chocolate
    That makes 0 drinks in total


## Getting Started


*   Create a new directory `~/problems/caffeine` and `cd` into it.

*   Create a file called `pseudocode.txt` in that directory. Note at least the following:

    *   What input is required and any limitations to that input
    *   What needs to be printed at the end
    *   From the input and the output you can determine which variables will need to be used
    *   The steps to take in the greedy algorithm the determine the number of espressos etc

    And try to define your algorithm as precisely as possible without writing C code yet.


## How to Test Your Code

Does your code work as prescribed when you input

*   `-1.00` (or other negative numbers)?
*   `0.00`?
*   `0.001` (or other positive numbers)?
*   letters or words?
*   no input at all, when you only hit Enter?

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 -l minprog/programmeren-ki/2021/other/caffeine

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
