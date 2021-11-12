# Cypher

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Implement a program that encrypts messages using an inverted alphabet, per the below.

    $ ./cypher 
    plaintext:  hEllo wOrld
    cyphertext: SvOOL DlIOW


## Background

Let's dive into cryptography. There are plenty of ways to hide messages in plain sight. You might consider [writing messages using invisible ink](https://en.wikipedia.org/wiki/Invisible_ink). Or you can learn sign language, which many people still don't understand. Chances are that no one will get your message... unless someone knows how to get it.

Cryptography is the field of study that considers ways of encrypting messages into *other messages* that aren't as easy to read. Such methods have been in use since at least the era of [classical antiquity](https://en.wikipedia.org/wiki/History_of_cryptography). One way of encrypting messages is by applying a **cypher**, i.e. substituting letters by different letters in a systematic fashion.

The algorithm that you're going to implement is composed of two different cyphers:

1. Replace *each letter* in the text with matching letters on the other end of the alphabet. For example, the letter `a` might be replaced with `z` and `b` with `y`.

2. Switch each letter's *casing*: i.e. any lowercase letters will be uppercased in the output, and any uppercase letters will be lowercased.

Implementing this cypher as a C program will yield output as per the example above.


## Specification

Design and implement a program, `cypher`, that encrypts messages using the cypher described above.

*   Implement your program in a file called `cypher.c` in a directory called `cypher`.
*   Your program must output `plaintext:` (without a newline) and then prompt the user for a `string` of plaintext (using `get_string`).
*   Your program must output `cyphertext:` (without a newline) followed by the plaintext's corresponding cyphertext.
*   After outputting cyphertext, you should print a newline. Your program should then exit by returning `0` from `main`.


## Getting Started

*   Use a strategy of changing strings "in-place". This means that you store an input string in a variable, and then you consider each character in the string, changing it when applicable.

    For example, to change every character in a string by `'a'`, you can use:
    
        for(int pos = 0; pos < strlen(s); pos++)
        {
            s[pos] = 'a';
        }

    As soon as you have made all necessary changes, you can then display the string to your user using `printf`.

*   Take care to design the different steps of your program by sketching it out and writing pseudocode! This will help you understand the problem better.

## How to test your code

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 -l minprog/programmeren-ki/2021/other/cypher

Execute the below to evaluate the style of your code using `style50`.

    style50 cypher.c


## How to submit

As soon as you're done, submit your `cypher.c` implementation, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `cypher.c` file (that's within your `~/problems/cypher` directory) and then select **Download**. You should find that your browser has downloaded `cypher.c`.

3. Make sure you are signed in to **this** website!

4. In the form below, choose the file that you just downloaded.

5. Press "Submit for grading". Presto!

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
