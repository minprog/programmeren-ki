# Decryptor

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Implement a program that decrypts messages using Caesar's cipher, per the below.

    $ ./decryptor ghFrgh Fdhvdu
    decode caesar


## Background

Supposedly, Caesar (yes, that Caesar) used to "encrypt" (i.e., conceal in a reversible way) confidential messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D, ..., and, wrapping around alphabetically, Z as A. And so, to say HELLO to someone, Caesar might write IFMMP. Upon receiving such messages from Caesar, recipients would have to "decrypt" them by shifting letters in the opposite direction by the same number of places.

The secrecy of this "cryptosystem" relied on only Caesar and the recipients knowing a secret, the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly secure by modern standards, but, hey, if you're perhaps the first in the world to do it, pretty secure!

Unencrypted text is generally called _plaintext_. Encrypted text is generally called _ciphertext_. And the secret used is called a _key_.

To be clear, then, here's how encrypting `HELLO` with a key of 1 yields `IFMMP`:

| plaintext    | H | E | L | L | O |
| ------------ | - | - | - | - | - |
| + key        | 1 | 1 | 1 | 1 | 1 |
| = ciphertext | I | F | M | M | P |

More formally, Caesar's algorithm (i.e., cipher) encrypts messages by "rotating" each letter by _k_ positions. More formally, if _p_ is some plaintext (i.e., an unencrypted message), _pi_ is the _ith_ character in _p_, and _k_ is a secret key (i.e., a non-negative integer), then each letter, _ci_, in the ciphertext, _c_, is computed as

ci = (pi + k) % 26

wherein `% 26` here means "remainder when dividing by 26." This formula perhaps makes the cipher seem more complicated than it is, but it's really just a concise way of expressing the algorithm precisely. Indeed, for the sake of discussion, think of A (or a) as 0, B (or b) as 1, …, H (or h) as 7, I (or i) as 8, …, and Z (or z) as 25\. Suppose that Caesar just wants to say Hi to someone confidentially using, this time, a key, _k_, of 3\. And so his plaintext, _p_, is Hi, in which case his plaintext's first character, _p0_, is H (aka 7), and his plaintext's second character, _p1_, is i (aka 8). His ciphertext's first character, _c0_, is thus K, and his ciphertext's second character, _c1_, is thus L. Can you see why?


## Frequency attacks

Especially lengthier messages encoded using a Caesar cypher are suceptible to "frequency attacks". This means that one can use knowledge of the language used to infer how the message was encrypted. Here is a diagram of letter frequencies in different languages:

![A list of languages, including for each language a bar from left to right divided in to sections. The width of the sections indicates the frequency of a particular letter in that language. In many languages, including English and Dutch, the letter E occurs most often, with A coming after.](frequencies.png)

So for messages in various languages, you could try assuming that the most frequently used letter is the letter E. With that in mind, all you need to do is analyze the *encrypted* message to find the most commonly occuring letter. For example, in the message

    ghFrgh Fdhvdu

the letter `h` is most common. What if that letter is actually an `E`? Well, from `h` to `E` is 3 steps down. Let's try subtracting 3 from each of the letters, and we'll get:

| plaintext    | g | h | F | r | G | h | F | d | h | v | d | u |
| ------------ | - | - | - | - | - | - | - | - | - | - | - | - |
| - key        | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| = ciphertext | d | e | C | o | D | e | C | a | e | s | a | r |

That seems to be English! Although the message wasn't so interesting, our algorithm does yield a correct result. The message's decryption key is -3.


## Assignment

Write a program that decodes messages encrypted using a Caesar cypher without knowledge of the key used. Your program must use a frequency analysis to decide what the most likely used key was, and decode the message using it.


## Specification

*   Implement your program in a file called `decrypt.c` in a directory called `decrypt`.

*   Your program must accept any number of command line arguments equal to or greater than 1, meaning a sentence of at least one word.

*   Your program then decrypts the message using the ideas from the explanation above.

*   Your program must not try to decode non-letters, but instead print these unchanged.

*   Your program must preserve the input's casing.

*   **Restriction:** You may not change the input string in-place or create a new string for storing the output. Instead, after deciding on the correct decryption key, you must decode each letter and print it to the screen immediately.


## How to Test Your Code

Use the examples above, and your own examples, to check whether your program works perfectly. After submitting your programma will also be automatically checked.

And for good measure, time permitting, use `style50` to eliminate basic style mistakes:

    style50 decryptor.c


## How to submit

As soon as you're done, submit your `decryptor.c` implementation, below! 
