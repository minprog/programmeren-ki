# Calendar

> **Individuele opdracht.**
>
> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.
>
> **Je gebruikt deze opdracht om dit te leren:**
>
> - Hoe je een programma kunt opdelen in (veel) functies, en
> - hoe functies samenwerken om een probleem op te lossen.
>
> Na maken van de opdracht kun je extra bestuderen hoe je bovenstaande dingen hebt aangepakt.

Implement a month calendar display, per the below:

    $ ./calendar 2021 11
              Nov 2021
    ---------------------------
    Sun Mon Tue Wed Thu Fri Sat
          1   2   3   4   5   6 
      7   8   9  10  11  12  13 
     14  15  16  17  18  19  20 
     21  22  23  24  25  26  27 
     28  29  30 

## Background

Displaying a calendar grid is not a hugely difficult task. You can build on your experience with writing other programs that present multiple lines of similar information.

Algorithmically, there is a little bit of challenge to the task: the calendar also displays weekdays (Sun--Sat), and the day numbers have to match up to the right weekdays. To do that correctly, you will need to calculate on what weekday the month's first day falls (we'll show you how in just a second.)

But more importantly, what we're going to do in this assignment is **decompose** the programming problem into manageable pieces. It's up to you then, to convert these pieces into functions in a C program, together with a `main` function that neatly ties everything together.

## Decomposition

Let us take you on a tour through the program just as we break it up in smaller pieces. As with any program, we start in the `main` function. This programs's goal of *displaying calendars* can be broken up into two main tasks: retrieving the month and year from the command-line arguments, and displaying the calendar for that month.

    main
     |---- get year, month
     \---- display calendar (f)

*Getting the year and month* from the command-line arguments can be done in one line each. Just call `atoi` to convert the numbers from a string into an integer (remember how?). *Displaying the calendar*, that's quite a huge task. Let's decompose further. We can distinghuish two parts of the calendar in the sample output: displaying the header, and displaying the actual grid with day numbers.

    display calendar
     |---- display header (f)
     \---- display grid (f)

*Displaying the header* consist of displaying the month and year, then a horizontal line (its width is always the same, so no problem to hard-code!). We'll leave it up to you if you'd like to implement these in separate functions. *Displaying the grid* is again quite a big task. You will need two crucial pieces of information: what weekday is the first day of the month, and how many days are in the month. When combined with the printing task, we can decompose into four tasks:

    display grid
     |---- get first day of month (f)
     |---- get number of days in month (f)
     |---- print spaces as padding
     \---- print number grid

*Getting the first day of month* can be done using a straightforward algorithm if we pick a reasonable starting point. Let's take 1 January 1800 as that starting point. We can find out that it's a Wednesday, so we'll define a constant `START_1800` to be `3`. What we can then do is count the number of days between 1 January 1800, and then we can use this expression to calculate the first day of the month: `(number_of_days_from_1800 + START_1800) % 7`.

    get first day of month
     |---- count number of days from 1800 (f)
     \---- calculate

To count the *number of days from 1800*, you can first count the number of days from 1800 per year, until the requested calendar year. Then you can count the number of days from 1 January in the requested year up until the requested month. Add these two numbers to get your answer. But how do you find the number of days in one year or month? Well, for months we have a couple of fixed rules:

- 31 days for Jan, Mar, May, Jul, Aug, Oct, Dec.
- 30 days for Apr, Jun, Sep, Nov.
- February has 28 days, except in a leap year, where it has 29 days.

So for a whole year we have 365 days, except for leap years, which have 366 days. In conclusion, we need at least three more functions:

    count number of days from 1800
     |---- count number of days from 1800 until year (f)
     |---- count number of days from 1 Jan until month (f)
     \---- check leap year (f)

The above should provide you with enough information to implement the full program.

Incidentally, did you notice that **decomposition** is more or less the same as **splitting up your problem**?

## Specification

Implement the calendar program, using *at least* the functions that are implied in the diagrams in the Decomposition section, above (marked with `(f)`). You may decompose problems further to your liking.

To get started, create a file called `calendar.c` and write a `main` function according to the specification. Then white the `display_calendar()` function that's used in `main`. And so on, until everything works. One or two functions will be a bit more of an algorithmical challenge, the rest of the functions will remain quite small.

Don't forget that you need to write function **prototypes** above main to be able to compile correctly, like so:

    // prototype
    void display_calendar(...);
    
    int main(void)
    {
        // use the function
        display_calendar(...);
    }
    
    void display_calendar(...)
    {
        // actual implementation of this function
    }

## Testing

You can use `check50` to find obvious mistakes, such as months starting on the wrong weekdate. But you should be able to easily test your program manually by `make`ing and running it.

    check50 -l minprog/programmeren-ki/2021/other/calendar

Before you hand in your solution, also check for obvious style mistakes using `style50`. But don't overdo it. You'll be doing a code review again next week.
