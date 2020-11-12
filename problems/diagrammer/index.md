# Diagrammer

Het uiteindelijke doel van deze opdracht is het maken van een tool die figuren kan manipuleren. De figuren zijn in dit geval diagrammen waarin allerlei objecten op een canvas geplaatst worden en waarvan allerlei eigenschappen kunnen worden ingesteld. Omnigraffle is bijvoorbeeld een programma waarin zulke diagrammen kunnen worden gemaakt door directe manipulatie met hulp van toetsenbord en muis. Zie hieronder.

![screenshot of the OmniGraffle user interface](omnigraffle.png)

De tool die je hier gaat bouwen werkt niet met directe manipulatie maar kan via de command-line worden aangeroepen om transformaties op een figuur toe te passen. Zo zou je met hulp van die tool bijvoorbeeld een pipeline kunnen bouwen waarmee een hele map aan figuren stuk voor stuk aangepast worden, zoals bijvoorbeeld het verwijderen van het eerste object uit elke figuur. Zo zou de tool als volgt kunnen worden aangeroepen:

    diagrammer.py complex.fig simple.fig merge-layers
    diagrammer.py large.fig small.fig scale 0.5

Deze opdracht bestaat uit een aantal onderdelen waarin we toewerken naar de tool:

1. Bouwen van een verzameling klassen die het canvas, de objecten en eigenschappen modelleren

2. Schrijven van een methode om een figuur uit een string te kunnen inlezen en een figuur en alle objecten naar een string weg te schrijven

3. Bouwen van een verzameling klassen die elk een transformatie kunnen uitvoeren op een figuur en de objecten daarin

4. Schrijven van een hoofdprogramma waarmee een bestand wordt geopend, een transformatie toegepast, en het resultaat weer weggeschreven

Het uiteindelijke doel van de opdracht is het oefenen met objectgeoriënteerd ontwerp, kennis maken met *inheritance*, en verder oefenen met Python en werken met klassen.


## Voorbereiding

Allereerst is het belangrijk om te zorgen dat je weer even goed in Python zit en vooral het objectgeoriënteerd programmeren.

- Kijk voor een terugblik op Python nog eens het [videocollege](/lectures/python-david) van dit jaar.

- Kijk voor een terugblik op object-georiënteerd programmeren nog een keer het [korte college](/problems/objects/lecture).

- Lees vervolgens zorgvuldig over het gebruik van "inheritance" bij het ontwerpen van klassen: [Think Python hoofdstuk 18](http://greenteapress.com/thinkpython/html/thinkpython019.html).

In de eerste stap moet je een UML-diagram maken. In het korte college hierboven zie je voorbeelden hiervan, en ook in de Queue/Cards-oefeningen heb je hiermee kennis gemaakt. In het hoofdstuk uit Think Python staat onderaan een voorbeeld-diagram waarin inheritance is verwerkt (met een "open pijl"). Dit zou genoeg moeten zijn om een basic UML-diagram te kunnen tekenen.
