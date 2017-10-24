# Monopoly: Startgeld

In een normaal potje Monopoly krijg je 1500 euro startgeld en verdien je 200 euro elke keer dat je start passeert. Zo'n eindige hoeveelheid startgeld heeft invloed op de snelheid waarmee je nieuwe straten kan kopen. In deze opdracht zoeken we uit welk effect dit precies heeft.


## Gebruik

	python money.py
	0 euro, 2197 worpen
	500 euro, 1997 worpen
	1000 euro, 1888 worpen
	1500 euro, 1750 worpen
	2000 euro, 1560 worpen
	2500 euro, 1424 worpen

> Natuurlijk zijn ook de antwoorden hierboven fout. Het goede antwoord mag je zelf simuleren.


## Specificatie

* Schrijf een programma genaamd `money.py` voor elke hoeveelheid startgeld van 0 t/m 2500 in stappen van 500 het aantal worpen dat nodig is om alle straten te kopen onder elkaar uitprint.
* Elke keer dat de pion start passeert krijgt de speler 200 euro extra.
* Je mag en moet een vakje kopen als de pion erop komt met genoeg geld.
* Als een vakje wordt gekocht verliest de speler de waarde van het vakje aan geld.
* Simuleer elke hoeveelheid een goed aantal keer, zodat het antwoord niet te veel varieert. Houd hierbij rekening met de maximaal 10 seconden die checkpy je geeft.
* Laat jouw programma ook een [grafiek maken](/theory/plotting) met op de x-as de verschillende hoeveelheden startgeld, en op de y-as het aantal worpen wanneer alles is opgekocht.
* Vergeet geen labels langs de assen van de grafiek te plaatsen.


## Tips:

* Gebruik en importeer `trump.py` d.m.v. `import trump` (hopelijk ben je daar `if __name__ == "__main__":` niet vergeten)


## Testen

	checkpy money
	