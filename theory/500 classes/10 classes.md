# Classes

Naarmate programma's groter worden neemt de wens voor betere data abstracties toe. Het is makkelijker om na te denken en te praten over concepten in jouw programma zonder het te hebben over de technische details. Zo maakt het niet uit of je een sudoku puzzel representeert met een string, tuple of een list. Wat voor jou en je collega's / medestudenten relevant is is wat je ermee kan.

Object oriented programming geeft jouw het gereedschap om data abstracties te creëeren in jouw programma. Zo kan je data en methodes combineren / bundelen onder één kap. Daarbij krijg je de kans om de interactie te bepalen. Wat kan jouw abstractie en hoe ga je ermee om?

In Python heb je classes, dat zijn beschrijvingen van objecten. Hierin definieer je precies wat een object kan en ook hoe. Zie het als een blauwdruk, waarbij bij elk detail meteen de uitwerking staat. Zie hieronder de class `Coordinate`.


    class Coordinate:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance_to(self, other):
            return (abs(self.x - other.x)**2 + abs(self.y - other.y)**2)** 0.5


Bovenstaande class introduceert een nieuw type in ons programma namelijk `Coordinate`. Vanaf nu kan je instanties ofwel objecten van het type `Coordinate` maken. Dit doe je als volgt:


    coord1 = Coordinate(3, 5)
    coord2 = Coordinate(2, 8)


Hier gebeurt het volgende, zodra je de class `Coordinate` aanroept, roept Python de methode `__init__` voor je aan. Init is kort voor initialize, ofwel de methode die wordt aangeroepen bij het initialiseren van een object. De methode `__init__` accepteert hier 3 argumenten. Dit is waar Python een beetje hacky wordt, want het eerst argument `self` vult Python voor je in. Dat is een referentie/verwijzing naar het object. Dat dit argument `self` heet is conventie, we doen het allemaal, maar het hoeft niet. Naast `self` staan nog 2 argumenten, hier `x` en `y`. Logisch ook want we hebben het over een coordinaat! Omdat er 2 argumenten naast `self` zijn moet je deze bij het aanmaken van een `Coordinate` ook meegeven, zo wordt er voor `coord1` de waarde `3` meegegeven voor `x` en `5` voor `y`. Op de regels daarna wordt er nieuwe zogenaamde "instance variables" aangemaakt voor het `Coordinate`, `.x` en `.y` respectievelijk. Daaraan worden de waardes `3` en `5` bij `coord1` toegekend.

## Instance variables

Een instance variable is een variabele die enkel beschikbaar is voor die instantie. Zo hebben `coord1` en `coord2` allebei een instance variable genaamd `.x`, maar deze heeft een hele andere waarde. Test het volgende maar eens:


    print(coord1.x)
    print(coord2.x)


Dat is ook hoe je bij de waardes van de `instance variable`s komt. Namelijk het object (de instance) en vervolgens een `.` en daarna de variabele naam.

Dit is super handig, want nu kunnen we een naam toekennen aan deze variabelen. Zo hoef je het niet meer te hebben over plek 0 en 1, maar kan je nadenken over een x en y coordinaat. Neemt weer wat cognitive load af en zo kan je collega niet de fout maken om `x` en `y` door elkaar te halen!

## Methods

Naast variabelen kunnen we ook functies toe kennen aan een class. Deze noemen we dan net even anders: `methods`. Dat zijn simpelweg functies behorende bij een class. Beide namen worden vaak door elkaar gebruikt!

Hiermee kunnen we niet alleen data groeperen onder één kap, maar ook de bijbehorende operaties en code. De class `Coordinate` kent dan ook één method genaamd `distance_to`. Elke method accepteert in Python altijd als eerst een verwijzing naar het object, die ene instantie waarvan de afstand willen weten, weer per conventie `self` genoemd. Daarnaast kan een method 0 of meer argumenten accepteren. `distance_to` accepteert er één meer, namelijk `other`. Klinkt logisch, we hebben het coordinaat `self` en een `other`.

Wat de method `distance_to` vervolgens doet is de afstand tussen de twee coordinaten berekenen. Daarom ook de naam `distance_to`! Je kan de method als volgt gebruiken:


    coord1.distance_to(coord2)


Voor Python is dit equivalent aan:


    Coordinate.distance_to(coord1, coord2)


Het eerste is enkel minder typen!

## Class variables

Daarnaast bestaan er class variables. Deze verschillen niet per object/instantie van een class, maar bestaan één keer voor alle objecten van een class.


    class Request:
        count = 0

        def __init__(self, type, message):
            # do something with type and message
            Request.count += 1

Zo heeft de class `Request` hierboven een class variable `count`. Deze wordt elke keer opgehoogd bij het initialiseren van een instantie van Request.


    print(Request.count) # prints 0
    request1 = Request("get", "homepage")
    print(Request.count) # prints 1
    print(request1.count) # prints 1
    request2 = Request("get", "accountpage")
    print(Request.count) # prints 2
    print(request1.count) # prints 2
    print(request2.count) # prints 2


Je kan via de class `Request` zelf bij de class variabele, maar ook via elke instantie/object van de class, in het voorbeeld hierboven `request1` en `request2`. Het zijn verschillende wegen naar Rome, maar de uitkomst is hetzelfde, de waarde van de class variabele `count`!


## Hidden methods

Python is gebouwd op Object Oriented Programming. Bijna alle constructies in een taal vertalen naar een method call. Bijvoorbeeld:


    a = 1
    b = 3
    a = a + b
    print(a)


Is eigenlijk het volgende:


    a = 1
    b = 3
    a = a.__add__(b)
    print(a.__str__())


Wat Python hiermee bereikt is dat jij als programmeur zelf kan bepalen wat er moet gebeuren als je bijvoorbeeld twee `Coordinate`s bij elkaar optelt, of hoe een `Coordinate` eruit moet zien als jij deze uitprint. Je moet alleen even opzoeken wat je precies moet implementeren en vervolgens rest de taak om het te implemteren. Bijvoorbeeld als volgt:


    class Coordinate:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"coord: {x} {y}"

        def __add__(self, other):
            return Coordinate(self.x + other.x, self.y + other.y)

        def distance_to(self, other):
            return (abs(self.x - other.x)**2 + abs(self.y - other.y)**2)** 0.5

Met zowel de `__str__` en `__add__` methodes geïmplementeerd kunnen we vervolgens het `+` teken en de functie `print()` gebruiken voor instanties/objecten van `Coordinate`.


    coord1 = Coordinate(3, 5)
    coord2 = Coordinate(2, 8)
    print(coord1)
    print(coord2)
    print(coord1 + coord2)
