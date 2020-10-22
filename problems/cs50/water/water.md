# Water

## tl;dr

Implement a program that reports a user's water usage, converting minutes spent in the shower to bottles of drinking water.

	$ ./water
	Minutes: 1
	Bottles: 12

	$ ./water
	Minutes: 10
	Bottles: 120


## Background

Suffice it to say that the longer you shower, the more water you use. But just how much? Even if you have a "low-flow" showerhead, odds are your shower spits out 1.5 gallons of water per minute. A gallon, meanwhile, is 128 ounces, and so that shower spits out 1.5 × 128 = 192 ounces of water per minute. A typical bottle of water (that you might have for a drink, not a shower), meanwhile, might be 16 ounces. So taking a 1-minute shower is akin to using 192 ÷ 16 = 12 bottles of water. Taking (more realistically, perhaps!) a 10-minute shower, then, is like using 120 bottles of water. Deer Park, that's a lot of water! Of course, bottled water itself is wasteful; best to use reusable containers when you can. But it does put into perspective what's being spent in a shower!


## Getting Started

Log into <https://ide.cs50.io/> and execute, if you haven't already, the below in a terminal window:

	mkdir ~/module0
	cd ~/module0

Then, to start implementing this problem, create a new file called "water.c" and proceed below.


## Steps

This problem looks a bit like the `ints.c` program from lecture. You might study the examples at the top of this problem and think about which parts of `ints.c` you might reuse in your solution.

You program should have some kind of `input` statement, as well as a `print` statement combined with a small calculation. So only a few lines inside `main` are needed.

Don't know where to start? Ask a question!


## Specification

Now if you *think* you're finished with the program, the specification, together with the examples of running the program, provide you with guidelines as to how your program should work _exactly_. 

Normally, you will probably read them before starting to program, so as to take into account the requirements and design a solution even **before you start coding** (unlike now!). But just as important, when you think you are finished, have another look and validate whether you haven't forgotten anything!

Here are the requirements for `water.c`:

* Write, in a file called `water.c` in your `~/module1/` directory, a program that prompts the user for the length of his or her shower in minutes (as a positive integer) and then prints the equivalent number of bottles of water (as an integer)

* For simplicity, you may assume that the user will input a positive integer, so no need for error-checking (or any loops) this time! And no need to worry about overflow!


## Usage

Your program should behave per the example below:

	$ ./water
	Minutes: 10
	Bottles: 120


## Hint

You can use the function `get_int` to prompt the user to input an integer value, as per the below:

	int minutes = get_int();


## Testing

To verify whether your program is indeed running well, you may use `check50`.

	check50 -l minprog/cs50x/2020/water


## Submitting

As soon as you're done, submit your `water.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `water.c` file (that's within your `module1` directory) and then select **Download**. You should find that your browser has downloaded `water.c`.

3. Make sure you are signed in to this website!

4. In the form below the problem, add the file that you downloaded.

5. Press "Submit for grading". Presto!
