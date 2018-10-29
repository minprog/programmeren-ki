# Tuple

## Definitie
Python heeft ook `tuple`s als datastructuur in de taal ingebouwd. Een tuple is een niet-muteerbare geordende verzameling.  Laten we even goed kijken naar wat dat precies inhoud.

- Een tuple is niet muteerbaar, dat betekent dat je de verzameling niet kan aanpassen (muteren). Ofwel, zodra de verzameling eenmaal bestaat, kan je deze niet meer aanpassen.
- Een tuple is geordend, dat betekent dat de elementen in de verzameling een volgorde kennen. De volgorde waarin je elementen in een tuple zet maakt dus uit.

## Waarvoor / wanneer
Een `tuple` lijkt heel erg op een `list`. Het grote verschil is dat tuples niet veranderbaar zijn waar lists dat wel zijn. In de meeste gevallen zul je dan ook een list gebruiken. Een tuple wordt echter handig zodra je gebruik maakt van andere datastructuren die enkel over weg kunnen met niet muteerbare waardes. Voorbeelden hiervan zijn `set`s en `dict`s in Python. Je kan bijvoorbeeld geen lists in een set bewaren, maar wel tuples.

Tuples zijn snel O(1) in:

- Het ophalen van elementen op een index (welk element staat er op plek 3?)

En langzamer O(n) in andere operaties:

- Het opzoeken van een element (staat element E in tuple T?)

## Code
Een tuple maak je zo aan in Python:

    numbers = (1,3)
    print(numbers)

Hiervoor gebruik je in Python de normale haken (`()`). Wil je een lege tuple aanmaken, dan kan dat zo:

    numbers = tuple()
    print(numbers)

Omdat de makers van Python hebben gekozen voor het gebruik van ronde haken voor tuples is er wat ambiguïteit in de taal. Want wat betekent `(1)`?. Is dat het getal 1 met haakjes voor rekenregels, of een tuple met het getal 1 erin?. De keuze is uiteindelijk gevallen op het eerste, `(1)` is simpelweg het getal 1. Een tuple met 1 waarde erin maak je in Python zo aan:

    numbers = (1,)
    print(numbers)

Dit ziet er misschien wat vreemd uit, maar die extra `,` is nodig om aan te geven dat het een tuple is in dit geval!

Een tuple is geordend. Dat betekent dat de datastructuur een volgorde kent. Het maakt dus uit in welke volgorde elementen in de tuple staan:

    numbers1 = (3,4,5)
    numbers2 = (4,3,5)
    print(numbers1)
    print(numbers2)
    print(numbers1 == numbers2)

## Omgekeerde indexen
In Python kan je heel makkelijk het laatste element van een geordende verzameling zoals een tuple pakken, door gebruik te maken van het `-` teken. Dan tel je van achter naar voren, kijk maar:

    numbers = (10,20,30,40,50,60)
    print(numbers[-1]) # print 60
    print(numbers[-2]) # print 50
    print(numbers[-3]) # print 40

## Slicing
Python kent een simpele syntax om een deel van een tuple (of andere geordende verzameling) te pakken, te "slicen":

    numbers = (10,20,30,40,50,60)
    print(numbers[1:4]) # prints (20,30,40)
    print(numbers[:4]) # prints (10,20,30,40)
    print(numbers[1:]) # prints (20,30,40,50,60)
    print(numbers[:]) # prints (10,20,30,40,50,60)
    print(numbers[:-1]) # prints (10,20,30,40,50)
    print(numbers[-3:]) # prints (40,50,60)
    print(numbers[-3:-1]) # prints (50,60)

## Extended slicing
Python kent ook een stapsgrootte bij slicing, deze kan ook negatief zijn. Ontzettend handig om bijvoorbeeld een geordende verzameling zoals een tuple om te draaien:

    numbers = (10,20,30,40,50,60)
    print(numbers[1:5:2]) # prints (20,40)
    print(numbers[::2]) # prints (10,30,50)
    print(numbers[1::2]) # prints (20,40,60)
    print(numbers[::-1]) # prints (60,50,40,30,20,10)

## Toch muteren
Een niet muteerbare waarde als een tuple kun je niet aanpassen. Je kan echter wel een nieuwe tuple aanmaken met daarin de aanpassingen.

Stel je voor, we hebben een tuple `(1,2,3)` en willen daaraan het getal `4` "toevoegen". Dan kan dat zo:

    numbers = (1,2,3)
    numbers = numbers + (4,) # numbers += (4,) kan ook!
    print(numbers)

Bovenstaande stukje code past de tuple `(1,2,3)` niet aan, maar maakt in plaats daarvan een hele nieuwe tuple met daarin `(1,2,3,4)`

Stel je hebt een tuple, en je wilt een waarde daarin veranderen. Dan kan je gebruik maken van slicing om een nieuwe tuple te maken:

    numbers = (10,20,30,40,50,60)
    numbers = numbers[:2] + (70,) + numbers[3:]
    print(numbers) # prints (10,20,70,40,50,60)

## Veel muteren
Als je een tuple hebt en je wilt er veel aan veranderen, dan is een tuple niet een handige datastructuur. Je zou er bijvoorbeeld voor kunnen kiezen om de tuple om te zetten naar een list, deze aan te passen, en vervolgens weer terug naar een tuple. Zoals hier:

    numbers = (10,20,30,40,50,60)
    numbers = list(numbers)
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2 # numbers[i] *= 2 kan ook!
    numbers = tuple(numbers)
    print(numbers) # prints (20,40,60,80,100,120)
