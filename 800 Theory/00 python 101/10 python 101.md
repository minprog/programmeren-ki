# Python 101
Je duikt straks ineens een nieuwe taal in. Dan zul je merken dat je eigenlijk al heel veel dingen kent, maar er net wat kleine verschillen zijn. Voornamelijk de syntax is telkens net even anders! Daarom hieronder een hele korte uitleg, en kleine code-snippets die je kan copy pasten en runnen. Voor meer uitleg kijk nog even naar het college van CS50. Schroom ook niet om even te googlen! :)

## Variabelen
Python is een programmeertaal met een dynamisch type systeem. Dit houdt in het geval van Python in dat variabelen niet meer zijn dan namen die je toekent aan waardes. De namen zelf kennen geen type. Waar je dus in C bij elke variabele moest aangeven van welk type die is, is dat in Python niet nodig / mogelijk. Probeer maar eens:

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
Python kent geen "normale" for-loop zoals C die wel kent: een for-loop met een initialisatie stap, een conditie en een incrementatie stap. In plaats daarvan kent Python enkel de zogenaamde "for each" loop. Je spreekt hem als volgt uit: voor elk element in verzameling doe iets. Daarom dus ook "for each"! :)

Zo'n soort loop is bijzonder handig, zo is een infinite loop schrijven een stuk moeilijker geworden. Hij ziet er als volgt uit:

    for letter in "hello":
        print(letter)

    for number in [1,2,3]:
        print(number * 2)

    for i in range(3):
        print(i)

## While-loops
De do-while loop bestaat niet in Python. Een beetje Python filosofie: "There should be one-- and preferably only one --obvious way to do it.". Daarom dus geen do-while loops. De normale while loop bestaat wel en ziet er als volgt uit:
    
    x = 10
    while x > 1:
        x = x / 2
        print(x)

## Functies
Functies in Python lijken heel erg op die in C. Echter, ze zijn een stuk soepeler. Je hoeft namelijk niet te specificeren wat de type van de argumenten hoeven te zijn, of welke type de functie `return`ed. Kijk maar:

    def add(a, b):
        return a + b

    x = add(3, 5)
    print(x)
    print(add("hello", "bye"))

## Lists
Vergeet de term array voor nu, Python heeft in plaats daarvan lists. Subtiel verschil, lists zijn precies even groot als het aantal elementen dat erin zit. Je kan ook blijven toevoegen en verwijderen. Ze schalen dus mee! Zie hier:

    items = [1,2,3]
    items.append("hello")
    del items[0]
    items.remove(2)
    print(items)
