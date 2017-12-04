# Monopoly: Trump

![](MonopolyBordInternationaal.jpg){:.inline}{: style="width:50%"}

Bij banken, verzekeraars en het centraal planbureau worden modellen opgesteld die
onze economie beschrijven. Alle facetten die een rol spelen krijgen een plek en met
behulp van een computer worden verschillende scenario's doorgerekend (gesimuleerd)
om zo risico's in te schatten bij bepaalde gebeurtenissen of om het effect van
nieuwe maatregelen te onderzoeken.

Door de onderlinge afhankelijkheid van de parameters in dat soort modellen wordt het
al snel ondoenlijk om het met de hand door te rekenen. Zeker als het effect van
maatregelen een random component heeft. Met behulp van een computer gaat dat snel en
kan je zelfs de settings vinden waarin je dingen kan optimaliseren: dat kan het
maximaliseren van je winstkansen zijn, maar ook het minimaliseren van de kans dat
je failliet gaat. Of een mix van die scenario's.

In deze module gaan we een voorbeeld doorrekenen: Monopoly met twee spelers,
waarbij we stap voor stap meer complexiteit toevoegen. Voor degene die de smaak te
pakken heeft en nu al droomt van een baan op de Risk-Analysis divisie van JP Morgan
hebben we nog wat suggesties voor extra opgaves gemaakt.

## Getting started

Bij deze opdracht leveren we wat code mee, zodat jij niet al het werk hoeft te doen. De code kun je [hier downloaden](https://github.com/Jelleas/monopoly/archive/master.zip).
Let er even op, het is een .zip bestand. Deze moet je dus uitpakken in de map waarin je wilt gaan werken.

Zodra je dat hebt gedaan zie je drie python bestanden: `monopoly.py` en `monopolyData.py`. De code binnen deze files hoef je niet te begrijpen. We zullen je er geen vragen over stellen, maar werp er wel een korte blik op.
Toch even voor een snelle uitleg: monopolyData een module die de data levert voor de
waardes en namen van de vakjes op het bord. `monopoly.py` geeft jou de mogelijkheid om een pion over het bord te laten lopen.

Hoe werkt dit alles? In monopoly.py geven we je twee nieuwe types. Dat zijn `Board`, en `Piece`. Dit zijn zelfgemaakte (door ons) types waarmee jij zometeen kan werken.
Je kan een `Board` aanmaken met de volgende regel code:

	import monopoly
	board = monopoly.Board()

En een `Piece` als volgt:

	piece = monopoly.Piece()

Let wel, dat wat voor het `=` teken staat is ook maar een naam, dat kan natuurlijk ook anders heten! We moeten als we in een ander bestand dan monopoly.py gaan
programmeren eerst `monopoly` importeren d.m.v. `import monopoly`. In Python zijn losse bestanden zogenaamde modules, welke je d.m.v. `import` kan importeren.
Door de bovenstaande code hebben we een `Board` en een `Piece`. Een `Board` heeft twee attributen: `names`, en `values`. Dit zijn lijsten van 40 lang, met alle
namen en waardes op de vakjes van het bord. Zo is `board.names[0]` de string `"start"`, met bijbehorende waarde `board.values[0]` van 0. Een `Piece` heeft één
attribuut: `location`. `location` is een integer die de plek op het bord aangeeft, alle `Piece`s beginnen op location 0. Ook heeft `Piece` een methode, een functie
behorende bij een Piece, namelijk `move(distance)`. Je kan een `Piece` laten bewegen d.m.v. de methode `move(distance)`, bijvoorbeeld `piece.move(7)` beweegt
de pion 7 vakjes. Door het gebruik van deze methode verandert de waarde van het attribuut location ook.

Met de combinatie van een `Board` en een `Piece` kunnen we het spel simuleren. Je kan namelijk de waarde opvragen van het vakje waar de `Piece` op staat d.m.v.
`board.values[piece.location]` en de naam d.m.v. `board.names[piece.location]`.

## Opdracht: Trump mode

We gaan een groot aantal potjes Monopoly simuleren waarin we 1 speler rond laten lopen en hem
straten laten kopen. We spelen in de zogenaamde Trump-Mode. De speler heeft oneindig veel geld,
en er is geen concurrentie. We houden het spel simpel, er zijn geen huizen of hotels, alleen ongekochte of gekochte straten, stations en nutsbedrijven.
Kanskaarten negeren we even, en niemand gaat direct naar de gevangenis.
Doel van deze opdracht is om te bepalen wat het gemiddeld aantal worpen is waarna alle straten
zijn verkocht.

## Gebruik

	python trump.py
	It took 4000 throws to buy the entire board!

> Let op: het antwoord hierboven is natuurlijk fout. Je mag zelf uitvinden hoeveel keer je de dobbelstenen moet werpen.

## Specificatie
* Schrijf een programma genaamd `trump.py` dat uitprint hoeveel dobbelsteen worpen het heeft geduurd om alles in bezit te hebben.
* Let hierbij op dat je vakjes zonder waarde (kans kaarten etc.) niet kan kopen.
* Een dobbelsteen worp in Monopoly is met 2 dobbelstenen.
* Simuleer meer dan 1 spel gezien het kanselement, anders varieert het antwoord te veel!

## Walkthrough
Hier volgen een serie aan stappen om naar het grote geheel toe te werken.

### Tussenstap 1: Dobbelstenen

Maak een nieuw bestand aan genaamd
`trump.py`. Zorg dat de gedownloade bestanden in dezelfde map staan.
Schrijf een functie `throw()` binnen `trump.py`. Laat de functie geen argumenten accepteren, en de uitkomst van een dobbelstenen worp als integer
returnen. Let op, binnen Monopoly heb je als speler twee dobbelstenen! Zo heb je de meeste
kans om 7 te gooien, en kun je 1 helemaal niet gooien. Om deze functie te implementeren kun je
gebruik maken van de functie `randint()` van de `random` module. Google maar!


### Tussenstap 2: Rondlopen

Nu we dobbelstenen hebben kunnen we rondlopen op het bord. Om het aan jezelf te bewijzen, loop een rondje,
en stop zodra je weer voorbij start bent (positie 0). Print na elke zet (dobbelstenen worp) het naam van het vakje
en de waarde van het vakje waar de pion op staat. Zoiets:

	Na worp 0: brink, 60
	Na worp 1: velperplein, 120
	Na worp 2: neude, 180
	...
	Na worp 7: dorpsstraat, 60


### Tussenstap 3: Bezit

Rondlopen is één ding, maar we willen straks ook straten, stations en nutsbedrijven kunnen kopen. We hebben dus iets
nodig om bezit te onthouden. Simpelweg een lijst zou hiervoor onhandig zijn, want sommige vakjes kun je niet kopen.
Hier kunnen we handig een [dictionary](/theory/dict) gebruiken. Waar we de namen van de vakjes kunnen gebruiken als keys, en daaraan
als value kunnen koppelen of ze al gekocht zijn of niet (een boolean). Als we dan enkel de namen van de vakjes die je
kan kopen in de dictionary stoppen, kunnen we straks heel makkelijk controlleren hoeveel er al is gekocht!

Om te beginnen hebben we een dictionary nodig, en moeten we deze vullen met alle namen van vakjes welke je kan kopen.
Dit zijn de vakjes met een waarde (anders gezegd, alle vakjes met een waarde hoger dan 0). Dit is aan jou: schrijf een
functie genaamd: `possession(board)`. Laat deze functie als argument een `Board` accepteren, en een
dictionary met alle vakjesnamen met een waarde hoger dan 0 als keys en alle values met waarde `False` `return`en.


### Tussenstap 4: Trump

We hebben nu een bord, een pion, dobbelstenen, en een manier om bezit bij te houden. Tijd om voor Trump te gaan spelen.
Onze vraag is, hoe vaak moet je dobbelen voordat je alles in bezit hebt? Hoewel je oneindig veel geld hebt, mag je enkel een vakje kopen als je erop staat!

Zorg dat je dit niet één keer simuleert, maar een gezond aantal keer, zeg 1000, 10000 keer? Mag best een paar seconden
duren, maar niet te lang (`checkpy` kapt je af na X seconden)!

Als output moet je programma het aantal keren dobbelen dat gemiddeld nodig was printen in de eerste regel van de output.

> tip: de functies `all()`, `any()` en `sum()`!

Zet jouw code van tussenstap 4 binnen `if __name__ == "__main__":`, dit zorgt er voor dat jouw code enkel wordt uitgevoerd als `__name__`
gelijkt is aan de string `"__main__"`. Python heeft een aantal verborgen variabelen en functies, deze beginnen en
eindigen allemaal met `__`. Eén daarvan is `__name__` dat is een naam die Python aan de module toekent. Run je de module
direct, dan is die naam `"__main__"` (denk ook terug aan C!). Ofwel `if __name__ == "__main__":` zegt letterlijk, voer de
code hieronder enkel uit als je deze module direct runt, en niet als je deze importeert.

## Testen

	checkpy trump
