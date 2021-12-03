# Indexer

> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Implement an indexing system for text research.

    $ python indexer.py texts/birdman.txt
    Index built for texts/birdman.txt. Type the word you want to look up.

    Enter search term: dinner

    The word "dinner" can be found on lines: 549, 1542.
    
    Enter search term: quit

Such an indexing system is efficient to use because it builds an index of search terms. For each possible search term, some relevant data is stored in the index. So in a way, the index is a representation of the input file. In this assignment, we store the *line numbers* where the word occurs in the text.

       original text                        index                           searches
    |-----------------|              |-----------------|              |-----------------|
    |                 |              | written: 7, 502 |------------->| written?        |
    |   birdman.txt   |------------->| little: 27, 281 | search many  |-----------------|
    |  ~22000 words   |  build once  | slowly: 24, 303 |------------->| dump?           |
    |                 |              | dump: 34        |              |-----------------|
    |-----------------|              | twitch: 42      |------------->| embrace?        |
                                     |-----------------|              |-----------------|

When that index is loaded into memory, it allows us to quickly search the text without re-loading the text or literally searching it from beginning to end. As you might imagine, such a system is very efficient when the index can be loaded once, after which many searches will be run.

## Getting started

`cd` into your `problems` directory and then download the distro:

    wget https://github.com/minprog/programmeren-ki/raw/2021/other/indexer/dist/indexer.zip

Then unzip and get started!


### Understanding

In the distro you'll find two files and a directory:

- `stopwords.txt` contains a list of words that can be ignored by the indexing system. (So, we don't have to index a gazillion occurrences of, for example, the word "the".)
- `texts` contains various text files for testing your implementation.
- `indexer.py` is your starting code.

The code in `indexer.py` revolves around a **word index** that contains for each word in the text the position where the word occurs. A "dictionary" in Python is well-suited to store such an index. You can build your dictionary like so, linking each word to a *list* of line numbers:

    {
        "dinner": [ 258, 289, 1096, ... ],
        "guest": [ ... ],
        "table": [ ... ],
        ...
    }


### Implementation details

The code in `indexer.py` has several predefined functions:

* `read_stopwords()` is partially implemented: it already reads the stop words from the file `stopwords.txt` and stores these in a list. You can complete the function by `return`ing the collection of those stop words.

* `convert_word()` is already implemented for you. It strips a word from all punctuation, whitespace, and digits, and it converts the word to lowercase.

* `create_index()` is a `TODO`. It should create an index for all words in the input file.

    * For each word in the file, the index should contain a record of all line numbers where this word occurs.
    * Words should be cleaned by `convert_words()` before being entered into the index.
    * Empty strings and stop words should not be indexed.

* `search_index()` is a `TODO`. Search the index on a specific word. Return a list of all the lines where the word occurs.

    * The functions `create_index()` and `search_index()` depend on each other.

* `show_search_results()` is a `TODO`. Print the search results like in the example above. You will need to change the function parameters for this, and that's fine!

* `user_input_search()` is already implemented for you. This function takes care of the user interaction. It repeatedly asks the user for a word and calls `search_index()` to find it. This function stops as soon as the user enters an empty string or the text "q", "Q", or "quit"


## Testing your program

- Test your code by running it on the example at the top of the page.

- Try some examples for yourself.

- What happens if you search a word that does not appear in the text?

- What happens if you search the word "the"?


## How to submit

As soon as you're done, submit your `indexer.py` implementation, below! 

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
