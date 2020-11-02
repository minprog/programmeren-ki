# Formatting

There are several rules of thumb that you can apply to make your code easier to read and understand.
Several of those rules concern the formatting of individual lines of code, or the formatting of several related lines of code.
Other rules concern details that, however small, occur very often in code.

One important idea that you will encounter is that of **consistency**: choosing a rule and applying it the same everywhere.
The reason that consistency pops up is that there are often several equally valid options to choose from when formatting your code.
Hence, choosing rules, agreeing upon those with others, and applying them consistently is a common practice in programming.

## Indentation

Indentation is putting one or more spaces before each line of code.
The number of spaces is dependent on the **structure** of the code itself.
By following the structure, indentation enhances your code **visually**, making it easier to recognize common patterns and to understand what the program is doing.
To achieve this, code **within** a pair of brackets is indented once.
We recommend that you indent code using four spaces at a time.

    // print arguments
    printf("\n");
    for (int i = 0; i < argc; i++)
    {
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        {
            printf("%c\n", argv[i][j]);
        }
        printf("\n");
    }

It is important to distinguish between **spaces and tabs** in this case. A tab is a single character that is displayed as multiple spaces (in most editors).
Sometimes, your editor may even insert spaces instead of the tab character as you type it.
The reason to make a clear distinction is that each editor may interpret a tab as being a different number of spaces.
So when you save your code with tab characters in it, it may actually look different in another editor.
You should be aware of this, and especially avoid **mixing** tabs and spaces (why?).
To make it easier for yourself, we recommend that you check that your editor is set to indent using **four spaces**, even if you type a tab character.

> You can check that your code is indented correctly using `style50`.
> You can find instructions on using `style50` alongside the problem specifications.

## Spaces

Consistent use of spaces makes expressions and statements easier to read.
To get started, we ask that you use the following rules consistently:

- Use a space around every binary operator.

        -3 + 5 - 4 * -2 < 10

- Add a space after keywords like `while`, `for` and `if`.

        while (count < 0)
        {
            if (count > 5)
            {
                printf("foo");
            }
        }

- Do not use a space between the name of a function and its opening `(`.

        printf("foo");
        int answer = atoi("42");


## Placing brackets

Our final example of formatting consistency is the placement of brackets. You can actually vary the placement of brackets. A pair of brackets defines a **code block**. Below, we see a `for`-loop, its control statements, and the block of code that is to be repeated by the loop. It is formatted like the examples above, with the **opening bracket** on a separate line.

    for (int i = 0; i < 4; i++)
    {
        x += 3;
        y *= 6;
    }

But one could also write it like this, with the opening bracket on the same line as the `for` keyword:

    for (int i = 0; i < 4; i++) {
        x += 3;
        y *= 6;
    }

Writing code like that has become quite common in some programming languages and within some programming teams.
This is a fine choice, although in this course we prefer the room that is added by putting the opening bracket on its own line. It must be noted, however, that this is just a **preference**.
We are not currently aware of studies that prove that one of both styles is easier to read.

> It is fine if you choose to use a different style of formatting, as long as it is a style that is commonly used with modern programming languages, and as long as you ensure that all code you hand in is consistently formatted (even the parts that you didn't write yourself.)

### Omitting brackets

Loops and `if`s do not actually require code blocks --- they merely require **one statement** that describes the action to take or to repeat. A code block itself is a statement, too, which is why the examples above are all valid. In case your code block contains just a single statement, you could choose to omit the block and just include that statement:

    if (y == 7)
        y = 0;

This is completely valid code. However, for reasons of clarity, and to prevent errors, we recommend always putting the brackets in.

## Grouping

Using empty lines between blocks of code makes your program easier to read.
As before, this enhances the visual structure of your program so another person can more easily recognize the patterns and make sense of the algorithms.
As you write longer code, you will encounter many options for grouping parts of it.
For now, you should at least use blank lines to **separate** `for`, `while`, `if` and other statements that contain blocks of code.
On the other hand, you can omit the blank line to keep an `if` and its related `else if` and `else` statements together.

So don't do this:

    int x = 5;
    for (int i = 0; i < 4; i++)
    {
        x += 3;
    }
    if (x > 10)
    {
        x /= 2;
    }

And don't do this:

    int x = 5;

    int y = 7;

    if (x > 10)
    {
        x /= 2;

    }

    else
    {
        y *= 2;
    }

But do this, i.e. grouping related statements:

    int x = 5;
    int y = 7;

    for (int i = 0; i < 4; i++)
    {
        x += 3;
        y *= 6;
    }

    if (x > 10)
    {
        x /= 2;
    }
    else
    {
        x *= 2;
    }

    if (y == 7)
    {
        y = 0;
    }

## Learn more

Want to know more about writing neatly formatted code? Have a look at these chapters:

- Steve McConnell, *Code complete: a practical handbook of software construction*. Chapter 31, *Layout and style*. Microsoft Press, 2004.
- Robert Martin, *Clean code: a handbook of agile software craftsmanship*. Chapter 5, *Formatting*. Pearson Education, 2009.
