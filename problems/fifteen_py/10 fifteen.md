# fifteen.py

![](fifteen.png){: style="width:40%"}

In deze opdracht ga je de fifteen opdracht van CS50 maken in Python. Er wordt in tegenstelling tot CS50 geen code aangeleverd, je moet alles zelf schrijven.


## Gebruik

	python fifteen.py
	usage: python fifteen.py size

	python fifteen.py 10
	usage: python fifteen.py size

	python fifteen.py 4
	15 14 13 12
	11 10 09 08
	07 06 05 04
	03 01 02 __
	Tile to move: 2

	python fifteen.py 3
	08 07 06
	05 04 03
	02 01 __
	Tile to move:


## Voorbeeld spelverloop

	python fifteen.py 3
	08 07 06
	05 04 03
	02 01 __
	Tile to move: 1

	08 07 06
	05 04 03
	02 __ 01
	Tile to move: 7
	Tile to move: 4

	08 07 06
	05 __ 03
	02 04 01
	Tile to move:

	...

	01 02 03
	04 05 06
	07 08 __
	You have won!

## Specificatie

* Schrijf een programma genaamd `fifteen.py` dat je aanroept met één integer command line argument, de grootte van het bord.
* Worden er meer of minder command line argumenten gegeven, dan moet het programma precies het volgende bericht printen: `usage: python fifteen.py size`.
* Is het command line argument groter dan 9 of kleiner dan 0, dan moet het programma precies het volgende bericht printen: `usage: python fifteen.py size`.
* Laat de gebruiker het spel fifteen spelen, op dezelfde manier als de CS50 fifteen.
* Elke ronde kan de gebruiker een getal invullen om te wisselen met het lege vakje. Ligt dit vakje niet naast het lege vakje, dan geef je de gebruiker een nieuwe kans.
* Zodra de gebruiker een negatief getal invult moet het spel stoppen. Doe dit **niet** met `sys.exit`.
* Zodra de winnende bord situatie is bereikt, dat is in optellende volgorde met het lege vakje als laatste vakje, print je precies de volgende felicitatie: `You have won!` en stopt het programma.
* Na elke zet print je de bordsituatie naar de gebruiker.
* Je mag aannemen dat de gebruiker alleen integers invult als zet.
* Je mag de bordsituaties onder elkaar printen. Je hoeft er niet voor te zorgen dat het scherm leeg is voordat je de nieuwe situatie print, zoals dit wel het geval was in de CS50 opdracht.
* Let erop dat de getallen en de lege tegel precies zo worden uitgeprint als in het voorbeeld hierboven!
* Let ook op dat je geen extra berichten uitprint, dus geen welkomsbericht! :)

## Tips

* Schrijf functies! Spiek ook even bij jouw ingeleverde fifteen.c opdracht.
* Bouw het programma in stapjes op, en lees de specificatie goed!
* Je kan zorgen dat een integer altijd als twee cijfers wordt geprint d.m.v. `print("{:0=2d}".format(5))`


## Testen

	check50 minprog/cs50x/2019/py/fifteen
