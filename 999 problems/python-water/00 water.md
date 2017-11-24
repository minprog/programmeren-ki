# water.py

In deze opdracht ga je de water opdracht van CS50 maken in Python.

## Gebruik

	python3 water.py
	Minutes: 1
	Bottles: 12

	python3 water.py
	Minutes: 10
	Bottles: 120

## Specificatie

* Schrijf een programma genaamd `water.py` dat print hoeveel flessen water er worden verbruikt.
* Op de eerste regel moet er worden gevraagd om het aantal minuten dat de gebruiker doucht.
* Op de tweede regel moet er geprint worden hoeveel flessen water daarbij worden verbruikt.
* Je mag aannemen dat de gebruiker enkel integers invult.

## Tips

* Open visual studio code, en maak een nieuw bestand aan genaamd `water.py`. Let hierbij op de `.py`, dan krijg je ook syntax highlighting ;)
* Schrijf het programma en run het d.m.v. `python water.py` in de terminal (of command prompt / powershell in Windows).
* Python doet een heleboel automatisch voor je, waaronder new lines na elke print. Wil je dat niet? Gebruik dit: `print("Jouw tekst hier", end = "")`. Dit geeft een extra argument mee aan de print functie, welke wordt gebruikt om de regel af te sluiten. Vervang je de `""` met iets anders, dan krijg je dat aan het einde van de print.
* Gebruiker input krijg je door de functie `input()`. Deze geeft je wat de gebruiker heeft ingevoerd als string. Wil je liever een int of float? Gebruik dan de functies `int()` en `float`.
* De functie `input()` kan je ook een argument meegeven, probeer maar eens `input("Hello there!")`.

## Testen

	checkpy water
