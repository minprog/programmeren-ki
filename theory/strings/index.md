# String

## Definitie
Python heeft een aantal datastructuren in de taal ingebouwd, één zo'n structuur is een `string`. Een string is een niet-muteerbare geordende verzameling van tekens.  Laten we even goed kijken naar wat dat precies inhoud.

- Een string is niet muteerbaar, dat betekent dat je de verzameling niet kan aanpassen (muteren). Ofwel, zodra de verzameling eenmaal bestaat, kan je deze niet meer aanpassen.
- Een string is geordend, dat betekent dat de elementen in de verzameling een volgorde kennen. De volgorde waarin je elementen in de string zet maakt dus uit. Zo is `"hello"` niet hetzelfde als `"olleh"`!
- Strings zijn verzamelingen van tekens. Elk element van een string, elk teken, is een string opzich. Python maakt geen onderscheid tussen strings en characters zoals C dat wel doet. Een character in Python is dus simpelweg een string met 1 teken erin!

## Waarvoor / wanneer
Een string gebruik je om tekst te representeren, net zoals in C.

Strings zijn snel O(1) in:

- Het ophalen van elementen op een index (welk element staat er op plek 3?)

En langzamer O(n) in:

- Het opzoeken van een element (staat element E in String Sß?)

## Code
Een string maak je zo aan:

    text = "Hello, world!"
    print(text)

Zo print je een string letter voor letter, elke op een nieuwe regel:

    text = "abcdef"
    for letter in text:
        print(letter)

Zo print je individuele letters:

    text = "abcdef"
    print(text[2])
    print(text[4])

## Omgekeerde indexen
In Python kan je heel makkelijk het laatste element van een geordende verzameling zoals een string pakken, door gebruik te maken van het `-` teken. Dan tel je van achter naar voren, kijk maar:

    text = "abcdef"
    print(text[-1]) # print f
    print(text[-2]) # print e
    print(text[-3]) # print d

## Slicing
Python kent een simpele syntax om een deel van een string (of andere geordende verzameling) te pakken, te "slicen":

    text = "abcdef"
    print(text[1:4]) # prints "bcd"
    print(text[:4]) # prints "abcd"
    print(text[1:]) # prints "bcdef"
    print(text[:]) # prints "abcdef"
    print(text[:-1]) # prints "abcde"
    print(text[-3:]) # prints "def"
    print(text[-3:-1]) # prints "ef"

## Extended slicing
Python kent ook een stapsgrootte bij slicing, deze kan ook negatief zijn. Ontzettend handig om bijvoorbeeld een geordende verzameling zoals een string om te draaien:

    text = "abcdef"
    print(text[1:5:2]) # prints "bd"
    print(text[::2]) # prints "ace"
    print(text[1::2]) # prints "bdf"
    print(numbers[::-1]) # prints "fedcba"

## Toch muteren
Een niet muteerbare waarde als een string kun je niet aanpassen. Je kan echter wel een string tuple aanmaken met daarin de aanpassingen.

Stel je voor, we hebben een string `"abc"` en willen daaraan `"d"` "toevoegen". Dan kan dat zo:

    text = "abc"
    text = text + "d" # text += "4" kan ook!
    print(numbers)

Bovenstaande stukje code past de string `"abc"` niet aan, maar maakt in plaats daarvan een hele nieuwe string met daarin `"abcd"`

Stel je hebt een tuple, en je wilt een waarde daarin veranderen. Dan kan je gebruik maken van slicing om een nieuwe tuple te maken:

    text = "abcdef"
    text = text[:2] + "g" + text[3:]
    print(text) # prints "abgdef"

Een string kent veel methodes die een nieuwe string aanmaken op basis van een bestaande string:

    text = "  abcdef  "
    print(text.strip()) # prints "abcdef"
    text = "abba"
    print(text.replace("a", "c")) # prints "cbbc"
    print(text.upper()) # prints "ABBA"

Voor meer zulke methodes zie de Python 3 documentatie: https://docs.python.org/3/library/stdtypes.html#string-methods
