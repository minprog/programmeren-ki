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

For this aspect in particular, you can use `style50` to help you out!
