# Python 101
Je duikt straks een nieuwe taal in. Dan zul je merken dat je eigenlijk al heel veel dingen kent, maar er in de basis een paar kleine verschillen zijn. Voornamelijk de syntax is net even anders. Daarom vind je hier de concepten die je al kent uit C, maar dan in Python. Bij elk concept staan kleine code-snippets die je kan uitvoeren in de interpreter. Dan zie je meteen hoe het werkt, en kan je er ook even mee spelen.

## De interpreter
Python is zowel een programmeertaal als een programma die code in de Python taal uitvoert. Zo'n soort programma heet een interpreter. Interpreters lezen code in en voeren deze direct uit. Er is dus geen compilatie tussenstap nodig zoals bij C. Dat betekent dat het runnen van Python code middels één commando kan:

    python hello.py

Dit voert de code in een bestand genaamd `hello.py` meteen uit. Probeer maar is, maak een bestand aan genaamd `hello.py` en zet daarin enkel deze regel code: `print("Hello, world!")`.

Dat is alle code die je nodig hebt om `Hello, world!` op je scherm te krijgen. Dat is een stuk minder dan bij [C](/problems/hello)! Python bestanden eindig je met `.py`, maar dit is geen verplichting. Het zorgt er wel voor dat programma's weten dat ze met een Python bestand te maken heb. Zo krijg je bijvoorbeeld in een code editor syntax highlighting specifiek voor Python.

Python's interpreter kent ook een REPL (Read, Evaluate, Print Loop) modus. Dan kan je regel voor regel Python code invoeren, die code wordt ge-evalueerd (lees uitgevoerd) en vervolgens wordt het resultaat geprint. Bijzonder handig als je snel even iets wilt uitproberen, gewoon om te kijken hoe iets werkt! Deze REPL modus start je zo:

    python

Vervolgens zie je dit:

    ~/workspace/ $ python
    Python 3.6.0 (default, Sep 11 2017, 19:52:36)
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Elke regel die je intypt wordt direct uitgevoerd, kijk maar:

    ~/workspace/ $ python
    Python 3.6.0 (default, Sep 11 2017, 19:52:36)
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> x = 1 + 2
    >>> x + 4
    7
    >>> 

## Variabelen
Python is een programmeertaal met een dynamisch type systeem. Dit houdt in het geval van Python in dat variabelen niet meer zijn dan namen die je toekent aan waardes. De namen zelf kennen geen type. Waar je dus in C bij elke variabele moest aangeven van welk type die is, is dat in Python niet meer nodig / mogelijk. Probeer maar eens:

    i = 6
    s = "hello"
    i = s
    print(i)

## If statements
Python kent net zoals C (en vele andere programmeertalen) if-statements en daarbij behorende else statements. Eén klein verschil, `else if` heet in Python `elif`. Dit ziet er dan als volgt uit:

    x = 20
    if x > 30:
        print("foo")
    elif x < 10:
        print("bar")
    else:
        print("baz")

## For-loops
Python kent geen "normale" for-loop zoals C die wel kent: een for-loop met een initialisatie stap, een conditie en een update stap. In plaats daarvan kent Python enkel de zogenaamde "for each" loop. Je spreekt hem als volgt uit: voor elk element in verzameling doe iets. Daarom dus ook "for each"!

Zo'n soort loop is bijzonder handig, zo kan je bijna geen infinite loops meer schrijven. Hij ziet er als volgt uit:

    for letter in "hello":
        print(letter)

    for number in [1,2,3]:
        print(number * 2)

    for i in range(3):
        print(i)

In het stukje code wordt de `range` functie gebruikt. Dat is een functie die een reeks integer getallen genereerd. Je kan hem als volgt gebruiken:

    range(5) # genereert 0,1,2,3,4
    range(1,5) # genereert 1,2,3,4
    range(1,10,2) # genereert 1,3,5,7,9

## While-loops
De do-while loop bestaat niet in Python. Een beetje Python filosofie: "There should be one-- and preferably only one --obvious way to do it.". Daarom dus geen do-while loops. De normale while loop bestaat wel en ziet er als volgt uit:

    x = 10
    while x > 1:
        x = x / 2
        print(x)

## Functies
Functies in Python lijken heel erg op die in C. Echter, ze zijn een stuk soepeler. Je hoeft namelijk niet te specificeren wat de type van de argumenten hoeven te zijn, of welk type de functie `return`ed. Kijk maar:

    def add(a, b):
        return a + b

    x = add(3, 5)
    print(x)
    print(add("hello", "bye"))

Zo kan je dus functies schrijven die bijvoorbeeld werken op integers en floats, maar ook op strings.

## Lists
Vergeet de term array voor nu, Python heeft in plaats daarvan lists. Subtiel verschil, lists zijn precies even groot als het aantal elementen dat erin zit. Je kan ook blijven toevoegen en verwijderen. Ze schalen dus mee! Zie hier:

    items = [1,2,3]
    items.append("hello")
    del items[0]
    items.remove(2)
    print(items)
