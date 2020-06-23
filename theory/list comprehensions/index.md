# Comprehensions

In Python heb je comprehensions om op één regel een collectie aan te maken. We gaan binnen deze cursus enkel focus leggen op `list` comprehensions. Houd wel in je achterhoofd dat er meer bestaan!

Een comprehension is eigenlijk niet meer dan een for-loop op een regel om een collectie te maken. In het geval van een `list` comprehension maken we dus op één regel een `list`. Dit ziet er als volgt uit:

    some_list = [i * 2 for i in range(10)]

Bovenstaande creëert een lijst met alle tweevouden van 0 t/m 18, oftewel `[0,2,4,6,8,10,12,14,16,18]`. Je leest dit als volgt: zet voor elke `i` in `range(10)` `i*2` neer in de lijst. Het is effectief een korte manier om het volgende voor elkaar te krijgen:

    some_list = []
    for i in range(10):
        some_list.append(i * 2)

Behalve enkel iets met de waarde i doen kan je list comprehensions ook heel handig gebruiken om de uitkomsten van meerdere functie aanroepen te verzamelen:

    import random
    random_numbers = [random.random() for i in range(100)]

Maar er is meer, zo kan je bijvoorbeeld ook een conditie verwerken in een list comprehension. De volgende twee stukken code zijn dan ook functioneel equivalent:

    some_list = [i * 2 for i in range(10) if i % 2 == 0]

    some_list = []
    for i in range(10):
        if i % 2 == 0
            some_list.append(i * 2)

Behalve nieuwe lijsten aanmaken kan je list comprehensions ook gebruiken om operaties op collecties uit te voeren. Dan loopen we niet door `range(10)` maar de bestaande collectie. Bijvoorbeeld:

    numbers = [1,4,9,3,2,5,10,6]
    strings = [str(number) for number in numbers]

Ook kan je list comprehensions gebruiken om te filteren, door middel van zo'n if statement. Bijvoorbeeld:

    numbers = [1,4,9,3,2,5,10,6]
    even_numbers = [number for number in numbers if number % 2 == 0]

List comprehensions kunnen dus heel handig zijn om met heel weinig code, veel voor elkaar te krijgen. Vaak zijn ze ook nog leesbaarder dan een grote for-loop! Als je een for-loop schrijft, denk dan eens of je dit simpeler kan maken met een list comprehension.

Let wel, je kan heel ver gaan. Zo kun je multidimensionele list comprehensions schrijven met allerlei condities erin. Op een gegeven moment moet je jezelf afvragen of het nog echt overzichtelijker is dan een gewone for-loop!

    dont_do_this_at_home = [[a * b for a in range(10) for b in range(5) if a > b] for i in range(3)]
