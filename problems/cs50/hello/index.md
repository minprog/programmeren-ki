# Hello

Meet Zamyla! She'll be offering us tips and tricks throughout the modules of this course.

![embed](https://www.youtube.com/embed/DmE9lCvrxgU)

## Hello, World

Meet your first C program:

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }

## Dive into the IDE

Hello, world! Hopefully you have succeeded in creating a CS50 IDE instance for yourself. You should have watched Doug's video on its use before continuing here. Let's make programs!

Go to the Terminal and issue the following command:

    mkdir ~/module0

You should see in the file list on the left that your first folder has been created. We call it `module0` so it can contain all programs that you write for the current module.

Now, point to the File menu and choose New. This will open a new editor with a blank "Untitled1" file in it. First thing to do is to give it a name and save it into your new directory. Press **CTRL-S** or **Cmd-S** to open the file dialog. For **Filename**, type `hello.c`. Then below, choose (click) the `module1` folder that you just created and click on **Save**.

In your new file, type the C code for "Hello, World" as seen above. Save it once more.

Let's point the terminal towards our new folder:

    cd ~/module0

The **prompt** is what the Terminal shows on your screen to "prompt" you to enter a new command. The prompt includes a portion to show what folder the Terminal is pointed towards. It should look like this, indicating that the **current folder** for the Terminal is indeed `~/module0`.

    ~/module0/ $

Next, type precisely the below (in lowercase), then hit Enter:

    ls

You should see just `hello.c`. That's because you've just listed the files in that same folder, this time using a command-line interface (CLI), using just your keyboard, rather than the graphical user interface (GUI) represented by that folder icon. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list." (It's such a frequently used command that its authors called it just `ls` to save keystrokes.) Make sense?

Here on out, to execute (i.e., run) a command means to type it into a terminal window and then hit Enter. Commands are "case-sensitive," so be sure not to type in uppercase when you mean lowercase or vice versa.

## Compiling Programs

Now, before we can execute the program at right, recall that we must *compile* it with a *compiler* (e.g., `clang`), translating it from *source code* into *machine code* (i.e., zeroes and ones). Execute the command below to do just that:

    clang hello.c

And then execute this one again:

    ls

This time, you should see not only `hello.c` but `a.out` listed as well? (You can see the same graphically if you click that folder icon again.) That's because `clang` has translated the source code in `hello.c` into machine code in `a.out`, which happens to stand for "assembler output," but more on that another time.

Now run the program by executing the below.

    ./a.out

Hello, world, indeed!

## Naming Programs

Now, `a.out` isn't the most user-friendly name for a program. Let's compile `hello.c` again, this time saving the machine code in a file called, more aptly, `hello`. Execute the below.

    clang -o hello hello.c

Take care not to overlook any of those spaces therein! Then execute this one again:

    ls

You should now see not only `hello.c` (and `a.out` from before) but also `hello` listed as well? That's because `-o` is a *command-line argument*, sometimes known as a *flag* or a *switch*, that tells `clang` to output (hence the `o`) a file called `hello`. Execute the below to try out the newly named program.

    ./hello

Hello there again!

## Making Things Easier

Recall that we can automate the process of executing `clang`, letting `make` figure out how to do so for us, thereby saving us some keystrokes. Execute the below to compile this program one last time.

    make hello

You should see that `make` executes `clang` with even more command-line arguments for you? More on those, too, another time!

Now execute the program itself one last time by executing the below.

    ./hello

Phew!

## Getting User Input

Suffice it to say, no matter how you compile or execute this program, it only ever prints `hello, world`. Let's personalize it a bit, just as we did in class.

Modify this program in such a way that it first prompts the user for their name and then prints `hello, so-and-so`, where `so-and-so` is their actual name.

> <svg class="bi" width="24" height="24" fill="currentColor" size="24x24" style="svertical-align:-0.255em; float:left; margin-right:0.75rem;"><use xlink:href="/icons/bootstrap-icons.svg#info-circle"></use></svg>
>
> David's Lecture 1 should help you find the right commands to include in your code. This is often the case: lectures include many examples of working code, along with an explanation of the inner workings, which should help you get started on some of the parts of an assignment.
{:.bg-light}

As before, be sure to compile your program with:

    make hello

And be sure to execute your program, testing it a few times with different inputs, with:

    ./hello

### Staff's Solution

To try out the staff's implementation of this problem, execute

    ./hello

within [this sandbox](http://bit.ly/2Qp0a2g). You can do that to be 100% sure that you understand
what is required of your own program.

### Hints

#### Don't recall how to prompt the user for their name?

Recall that you can use `get_string` as follows, storing its *return value* in a variable called `name` of type `string`.

    string name = get_string("What is your name?\n");

#### Don't recall how to format a string?

Don't recall how to join (i.e., concatenate) the user's name with a greeting? Recall that you can use `printf` not only to print but to format a string (hence, the `f` in `printf`), a la the below, wherein `name` is a `string`.

    printf("hello, %s\n", name);

#### Use of undeclared identifier?

Seeing the below, perhaps atop other errors?

    error: use of undeclared identifier 'string'; did you mean 'stdin'?

Recall that, to use `get_string`, you need to include `cs50.h` (in which `get_string` is *declared*) atop a file, as with:

    #include <cs50.h>

## Testing

To verify whether your program is indeed running well, you may use `check50` in the Terminal. Make sure that your Terminal is still pointing towards the directory that your `hello.c` resides in!

    check50 -l minprog/cs50x/2020/hello

## Submitting

As soon as you're done, submit your `hello.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `hello.c` file (that's within your `module0` directory) and then select **Download**. You should find that your browser has downloaded `hello.c`.

2. Make sure you are signed in to **this** website!

3. In the form below, choose the file that you just downloaded.

4. Press "Submit for grading". Presto!

Your program will then again be checked using `check50` and the result will be recorded on this website. If the check fails, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal!
