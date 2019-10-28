# Whitespace

Consistent use of whitespace makes expressions and statements more readable. Now there is no golden standard on just how you format your code. It is important however to format your code consistently and to be able to adhere to a set of rules set by for instance your company or the team you work in. In this course we ask that you:

-   Use a space around every binary operator:

		-3 + 5 - 4 * -2 < 10

-   Add a space after keywords like `while`, `for` and `if`:

		while (count < 0)
		{
			if (count > 5)
			{
				printf("foo");
			}
		}

-   Do not use a space between the name of a function and its opening `(`:

		printf("foo");
		int answer = atoi("42");

Using empty lines between blocks of code makes your program easier to read. Keep blocks of `if` and `else` statements together, but place an empty line between blocks of code that do not belong together.

So don't do this:

		int counter = 5;
		for (int i = 0; i < 4; i++)
		{
			counter += 3;
		}
		if (x > 10)
		{
			counter /= 2;
		}

Or this:

		int foo = 5;

		int bar = 7;

		if (foo > 10)
		{
			bar /= 2;

		}

		else
		{
			bar \*= 2;
		}

But do this:

		int baz = 5;
		int qux = 7;
		for (int i = 0; i < 4; i++)
		{
			baz += 3;
			qux \*= 6;
		}

		if (x > 10)
		{
			baz /= 2;
		}
		else
		{
			baz \*= 2;
		}

		if (qux == 7)
		{
			qux = 0;
		}

For this aspect in particular, you can use `style50` to help you out!
