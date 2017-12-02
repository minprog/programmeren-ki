# Virus: Geneesmiddel

![](medicine.png){:.inline}{: style="width:100%"}

In dit deel van de module gaan we een geneesmiddel introduceren dat de virussen bestrijdt.
Maar virussen kunnen resistent zijn, en hun kinderen kunnen het worden.
Een resistent virus is een virus dat `AAA` in zijn DNA string heeft.
Zodra het geneesmiddel wordt geintroduceerd, kunnen alle virussen behalve resistente virussen niet meer reproduceren.


## Getting started
Schrijf alle code voor deze opdracht in een file genaamd `medicine.py`.
Je kan de code van de vorige opdracht importeren. Je hoeft geen code te copy pasten!


## Tussenstap 1: Resistentie
Allereerst gaan we kijken of een virusgenoom resistent is.

* Schrijf een functie `isResistent(virus)`.
	* Deze functie accepteert één argument, `virus`, dit is een virusgenoom.
	* De functie moet een boolean returnen welke aangeeft of het virus resistent is (`True`) of niet (`False`).
* Een virus is enkel resistent als `AAA` achterelkaar voorkomt.

### Tip

* Kijk eens naar de functie `string.find()`!


## Tussenstap 2: Simuleren met een geneesmiddel
Nu kunnen we het effect gaan bestuderen van de introductie van een geneesmiddel.
We dienen het geneesmiddel toe zodra de diagnose is gesteld, bij de 100ste tijdstap.
Laat per tijdstap eerst virussen afsterven, daarna bereken je pas de reproductie kans en laat je ze reproduceren.

* Schrijf een functie genaamd `simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, maxPopulation, timesteps = 500)`.
	* Deze functie accepteert vijf argumenten, en één optioneel argument:
		* `viruses` is een lijst van virusgenomen.
		* `mortalityProb` is een float tussen 0 en 1 (inclusief) die de kans op het afsterven per virusdeeltje representeert.
		* `reproductionProb` is een float tussen 0 en 1 (inclusief) die de kans op reproductie per virusdeeltje representeert.
		* `maxPopulation` is een integer voor de maximale populatiegrootte.
		* `mutationProb` is een float tussen 0 en 1 (inclusief) die de kans op mutatie bij reproductie representeert.
		* `timesteps` is een integer en een optioneel argument die het aantal tijdstappen in de simulatie aangeeft.
	* De functie moet een lijst returnen met daarin de populatiegrootte (een integer) op elke tijdstap.
* In tegenstelling tot `simulate()` van `infection.py` mag een virus enkel reproduceren als het resistent is na de 100ste tijdstap.

### Tips
* Test deze functie goed!
* Maak eventueel een plot, gebeurt er wat je verwacht?


## Tussenstap 3: Genezing?
Met de volgende parameters:

* tijdstappen = 500
* genoomlengte = 16
* start virus populatie grootte = 10
* maximale virus populatie grootte = 1000
* maximale reproductie kans = 7%
* sterfte kans = 5%
* mutatie kans = 10%

Hoeveel van percent van de patienten is volledig genezen? Een patient is volledig genezen als er geen virusdeeltjes aanwezig zijn in de laatste tijdstap.

* Schrijf hiervoor een functie `experiment(numberOfPatients)`.
	* Deze functie accepteert één argument, `numberOfPatients`, dit is het aantal patienten in het experiment.
	* De functie moet een integer returnen dat het aantal compleet genezen patienten teruggeeft.


## Testen

	checkpy medicine
