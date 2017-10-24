# find.py

In deze opdracht ga je de find opdracht van CS50 maken in Python. We vragen je binary search te implementeren. Sorteren mag je aan de `sorted()` functie overlaten!

## Gebruik

	python find.py
	usage: python find.py needle haystack

	python find.py 3
	usage: python find.py needle haystack

	python find.py 3 1 2 3
	Found the needle in the haystack

	python find.py 3 1 2
	Did not find the needle in the haystack

	python find.py 3 5 3 4 2 1
	Found the needle in the haystack

## Specificatie

* Schrijf een programma genaamd `find.py` dat je aanroept met twee of meer integer command line arguments: een needle en de overige argumenten vormen de haystack.
* Worden er minder dan 2 command line arguments gegeven, dan moet het programma precies het volgende bericht printen: `usage: python find.py needle haystack`.
* Je mag aannemen dat er enkel integers worden meegegeven als command line arguments.
* Doorzoek de haystack op zoek naar de needle d.m.v. binary search. Afhankelijk van of de needle in de haystack zit print je `Did not find the needle in the haystack` of `Found the needle in the haystack`.


## Tips

* Schrijf functies!
* Een lijst kun je in Python sorteren met de `sorted()` functie. Zo komt er uit `sorted([3,2,1])` de lijst `[1,2,3]`.
* Delen van een lijst kan je in Python makkelijk pakken (slicen). Zo geeft `l[1:3]` een nieuwe lijst met alle elementen van lijst `l` vanaf het eerste element tot het derde. `l[1:]` geeft een lijst van het eerste element t/m het laatste en `l[:2]` tot het tweede element. 
* Test jouw programma grondig, ook zonder `checkpy`. Je kan heel simpel dubbelchecken of de needle in de haystack zit d.m.v. de volgende regel python code `needle in haystack`. Dit laat Python d.m.v. linear search door de haystack gaan (als haystack een lijst is) en geeft `True` of `False` afhankelijk van of de needle in de haystack zit.


## Testen

	checkpy find
