# Scope

Try to restrict the scope, the lifespan, of a variable as much as possible. That way you let go of unused memory as fast as possible, but more importantly you do not clutter the namespace with unused variables. That makes it just a little easier to find names for new variables, without resorting to names like `new_count` and `user2`.

For instance, take this for-loop:

    int i;
    for (i = 0; i < 10; i++) {
        printf("hello");
    }

Here the variable `i` continues to exist beyond the body of the for-loop, even though it probably won't see any use. So do this instead of the above:

    for (int i = 0; i < 10; i++) {
        printf("hello");
    }

The same rule goes for "global" variables, that are declared outside the scope of a function. In some cases, it may be useful to store a few items of data globally, so every function may access these (an example is the `board` variable in `fifteen`).

However, using a global variable requires you to be extra careful in designing your program. It should be prevented that one function changes a variable in such a way that is confusion for another function.

So global aren't always the best choice. If you do not *need* to share all information between all functions, always declare the variables where you need them: "locally" in a function.

There are several solutions for preventing global variables while still sharing information between functions (like using function parameters!). This is beyond the scope for find/fifteen, but definitely ask if you need inspiration!


## Late declaration

Try to declare your variables as late as possible by moving your variables as close as possible to the code where it's actually used. Not only does this make your code easier to read, it also makes it much easier to spot which pieces of code are independent of each other.

So don't do this:

    void my_function()
    {
        int count = 0;
        // code
        // some more code
        count += 1;
    }

But do this:

    void my_function()
    {
        // code
        // some more code
        int count = 0;
        count += 1;
    }

