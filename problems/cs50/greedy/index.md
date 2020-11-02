# Greedy

## tl;dr

Implement a program that calculates the minimum number of coins required to give a user change.

~~~~
$ ./greedy
Change owed: 0.41
4
~~~~

## Background

![Coin Changer Toy](changer.jpg){: style="width:50%"}

When using a device like this, odds are you want to minimize the number of coins you're dispensing for each customer, lest you have to press levers more times than are necessary. Fortunately, computer science has given cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one "that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems."

What's all that mean? Well, suppose that a cashier owes a customer some change and on that cashier's belt are levers that dispense quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). Solving this "problem" requires one or more presses of one or more levers. Think of a "greedy" cashier as one who wants to take, with each press, the biggest bite out of this problem as possible. For instance, if some customer is owed 41¢, the biggest first (i.e., best immediate, or local) bite that can be taken is 25¢. (That bite is "best" inasmuch as it gets us closer to 0¢ faster than any other coin would.) Note that a bite of this size would whittle what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16. That is, the remainder is a similar but smaller problem. Needless to say, another 25¢ bite would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to a bite of size 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ bite followed by one 1¢ bite, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.

It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally for America's currency (and also the European Union's). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible. How few? Well, you tell us!


## Steps

So how do you tackle this problem? Let's take a look at the example from above:

    $ ./greedy
    Change owed: 0.41
    4

There's a few parts that can be identified in the input and output of this program:

1. The program prints a **prompt**, which asks how much change is owed: `Change owed:`
2. At the prompt, you type a floating point number, in this case `0.41`, and press ENTER.
3. The program prints the number of coins that would be returned: `4`.

Clearly, some kind of calculation is happening between steps 2 and 3. From the description of the calculation above, you may have inferred that doing the calculation is not as simple as the expression that you used when implementing your solution to the Water problem. No, instead, this calculation is more complicated. It is your main **algorithm**.

> <svg class="bi" width="24" height="24" fill="currentColor" size="24x24" style="svertical-align:-0.255em; float:left; margin-right:0.75rem;"><use xlink:href="/icons/bootstrap-icons.svg#info-circle"></use></svg>
>
> From now on, you will be using the [Problem Solving Steps](/steps) to analyze problems and propose solutions. We have now identified the core algorithm for this problem, so you should be able to apply the steps to find that algorithm. We suggest that you read about the steps now and then continue below.
{:.bg-light}


### Phase 1. Analyzing the problem

Let Zamyla provide you with some more background on the problem:

![embed](https://player.vimeo.com/video/353578615?byline=0&portrait=0)

If we turn this idea of greedy change into an algorithm, we notice that two numbers are in play:

- how much change do we still have to return, the **amount**
- how many coins are going to be returned, the **count**

The question is then: what algorithm will correctly convert the number `amount` into a number `count`?

> Now, head to the [Problem solving steps](/steps) and work through steps 1 to 4. You do this with a **partner** to make it easier to come up with good examples, and then help each other out to work through those example precisely.
>
> The goal of these first steps is to describe some procedure that will work well given reasonable input examples. The procedure is described in some kind of pseudo-code. Only when you are both satisfied you proceed to implementing your solution in C.
{:.bg-light}

<!-- In fact, the idea of the algorithm is to *convert* the amount of change required into the count of coins that are minimally needed to make that amount. In pseudocode, our algorithm may look like this the following, if we assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). Note the presence of both `count` and `amount` in that code:

  set amount to 32 cents
  set count to 0
  while (quarters can be used)
    increase count
    decrease amount by one quarter
  while (dimes can be used)
    increase count
    decrease amount by one dime
  (etc...)
  print number of coins used

Study this pseudocode; discuss the details. Do you understand every part? Do you have a notion of how it would be translated into C? -->


### Phase 2. Implementation

> <svg class="bi" width="24" height="24" fill="currentColor" size="24x24" style="svertical-align:-0.255em; float:left; margin-right:0.75rem;"><use xlink:href="/icons/bootstrap-icons.svg#exclamation-triangle"></use></svg>
>
> Warning! This phase should be done **individually**. Keep in mind that you do not share C code with other students or tell each other what kinds of C code to use. Do ask for help from the course's staff!
{:.bg-warning}

To get started implementing this algorithm, create a file called `greedy.c` and insert a standard `main` function. Within that `main` function, insert the following two lines, which create the variables that are needed for the algorithm:

	int amount = 32;
	int count = 0;

After those two lines, you might implement the algorithm based on the procedure that you came up with. Use `printf` from the Standard I/O library to output your final answer. Ask for help where needed!

> <svg class="bi" width="24" height="24" fill="currentColor" size="24x24" style="svertical-align:-0.255em; float:left; margin-right:0.75rem;"><use xlink:href="/icons/bootstrap-icons.svg#info-circle"></use></svg>
>
> Incidentally, so that we can automate some tests of your code, we ask that your program's last line of output be only the minimum number of coins possible: an *integer* followed by `\n`.
{:.bg-light}

When (almost) finished implementing the algorithm, it's time to test your program well. Run your program and see if it does indeed print `4` for the amount of 32 cents! And then change `amount` to 5 and see what it does.

When satisfied with the results, you have completed the basic implementation of the greedy algorithm. However, there is something still missing to make the program work with arbitrary input entered by users. That's the next step.


## User input

Your program currently has `amount` **hardcoded** into the program (that is, you have to change the code to make the program behave differently). You'll need to change it to allow a user to input an amount from the keyboard each time the program is run. As you can see in the example atop this problem document, input is actually given in *dollars*, not cents. Up until now you hardcoded the `amount` as cents.

Important to understand is that you should not change your algorithm to do the calculation in dollars entirely. That's not needed, and might introduce floating-point calculation errors! Instead, we take user input as a `float` (for dollars), and after we have a valid dollar amount, we **convert** it to an integer (for cents).

First, to get the dollar amount from the keyboard, use `get_float` from the CS50 Library and assign the result to a variable named `dollars` of type `float`. Add code to do this right at the top of your `main` function.

> <svg class="bi" width="24" height="24" fill="currentColor" size="24x24" style="svertical-align:-0.255em; float:left; margin-right:0.75rem;"><use xlink:href="/icons/bootstrap-icons.svg#info-circle"></use></svg>
>
> We ask that you use `get_float` so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed 9.75 dollars (as in the case where a newspaper costs 25¢ but the customer pays with a 10 dollar bill), assume that your program's input will be `9.75` and not `$9.75` or `975`. However, if some customer is owed $9 exactly, assume that your program's input will be `9.00` or just `9` but, again, not `$9` or `900`. Of course, by nature of floating-point values, your program will likely work with inputs like `9.0` and `9.000` as well; you need not worry about checking whether the user's input is "formatted" like money should be.
>
> You need not try to check whether a user's input is too large to fit in a `float`. Using `get_float` alone will ensure that the user's input is indeed a floating-point (or integral) value but not that it is non-negative.
{:.bg-light}

Now, if the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies. This is a perfect case for a `while`-loop, or even better, a `do`-`while`-loop!

## Connecting input to the algorithm

Hopefully, you've now written a few lines of code (with a loop!) that allow user input. All that's left is connecting that input with the algorithm. The first thing you can do in preparation, is removing the `int amount` declaration. We're going to replace that one.

Remember that the input variable `dollars` is a `float`, but the algorithm requires and `int`. So right after the point where we know the input is done, we need to convert it. What would be the right formula? Well, how many cents does one dollar equal? Write that conversion yourself.

> <svg class="bi" width="24" height="24" fill="currentColor" size="24x24" style="svertical-align:-0.255em; float:left; margin-right:0.75rem;"><use xlink:href="/icons/bootstrap-icons.svg#info-circle"></use></svg>
>
> But even with the right mathematical formula for converting a dollar amount to cents, there may still be errors. This is because if your user types `0.41`, which should become 41 cents, this may actually be represented in the computer as `40.999999999..` cents. When converting to an integer, this will become `40` cents instead of `41`! That's why you should use the `round()` function that's available in the C standard library. Recall that if you round the number 40.99, this will indeed yield 41.
{:.bg-light}

If all is well, your program should now be testable again. Check by running and entering `0.41` when prompted. And then also try the examples that you'll find below, under **Usage**. Anything not quite right? Ask for help!


## Explanation

Why can't the algorithm just work with `floats`? That would save us converting the input, right?
Well, beware the inherent imprecision of floating-point values. For instance, `0.1` cannot be represented exactly as a `float`. Try printing its value to, say, `55` decimal places, with code like the below:

~~~~
float f = 0.1;
printf("%.55f\n", f);
~~~~

And so, before making change, you'll probably want to convert the user's input entirely to cents (i.e., from a `float` to an `int`) to avoid tiny errors that might otherwise add up!


## Usage

When finished, your program should behave per the examples below. Do check if each works correctly!

~~~~
$ ./greedy
Change owed: 0.01
1
~~~~

~~~~
$ ./greedy
Change owed: 0.41
4
~~~~

~~~~
$ ./greedy
Change owed: -0.41
Change owed: -0.41
Change owed: foo
Change owed: 0.41
4
~~~~

~~~~
$ ./greedy
Change owed: 1.00
4
~~~~


## Testing

Before submitting, use `check50` to make sure that you covered every corner case of this particular problem. Anything still wrong? First thing to try is to make sure your **procedure** from problem solving phase 1 works correctly with the example from `check50`. Are you sure it works? Then the problem is more likely to be found in your **implementation**.

~~~~
check50 -l minprog/cs50x/2020/greedy
~~~~


## What about Phase 3 and 4?

The Problem Solving Steps comprise four phases, of which you have now completed the first two (hopefully!). You should now first submit your `greedy.c` in the form below. Then, you can take a look at **Mario**, another problem for this module.

After you have finished Greedy and Mario, you will start Phase 3. Together with a partner, you will review each other's code, and you will have the opportunity to revise your own solutions and resubmit. Only then do you continue to Phase 4.


## Submitting

1. When ready to submit, log into [CS50 IDE](https://ide.cs50.io/).

2. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `greedy.c` file (that's within your `module1` directory) and then select **Download**. You should find that your browser has downloaded `greedy.c`.

3. Make sure you are signed in to this website!

4. In the form below the problem, add the file that you downloaded.

5. Then, create a PDF with the notes from your analysis (see Phase 1 above), and add that to the form.

6. Press "Submit for grading". Presto!
