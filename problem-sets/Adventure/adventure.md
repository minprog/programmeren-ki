# Adventure Game
Lang geleden waren text-based adventure games bijzonder populair. Dat zijn type spellen waar je tekst te zien krijgt, en door het invoeren van tekst verder komt in het spel. Eén zo'n spel is afkomstig van [William Crowther](https://en.wikipedia.org/wiki/William_Crowther_(programmer)) die in 1975 de basis legde voor text-based adventure games in zijn spel Colossal Cave, of beter bekend als Adventure.

In Adventure bevind je je in verschillende "rooms", en kan je tussen deze rooms navigeren door middel van tekst commando's. Bijvoorbeeld zo:

    You are standing at the end of a road before a small brick
    building. A small stream flows out of the building and
    down a gully to the south. A road runs up a small hill
    to the west.
    > WEST
    You are at the end of a road at the top of a small hill.
    You can see a small building in the valley to the east.
    > EAST
    Outside building.
    >

Door middel van instructies zoals West/East, maar ook bijvoorbeeld In/Out en North/South navigeer je tussen de kamers. In Adventure kan je meer dan enkel navigeren, zo kan je ten alle tijden het `HELP` commando typen voor uitleg over het spel. Het `LOOK` commando om de uitgebreide beschrijving van de kamer te zien. Zo zag je in het voorbeeld hierboven dat wanneer de kamer voor de tweede keer bezocht werd je enkel een korte beschrijving te zien kreeg. Zo je nu `LOOK` gebruiken dan gebeurt het volgende:


    > LOOK
    You are standing at the end of a road before a small brick
    building. A small stream flows out of the building and
    down a gully to the south. A road runs up a small hill
    to the west.
    >

In Adventure heb je ook objecten. Deze objecten bevinden zich in kamers en kun je als speler oppakken (`TAKE <obj>`) en laten vallen (`DROP <obj>`). Ten alle tijden kun je kijken wat je in je bezit hebt d.m.v. `INVENTORY`. Zo kom je de volgende situatie tegen in het spel:

    Inside building
    You are inside a building, a well house for a large spring.
    There is a a set of keys here
    > TAKE keys
    Taken.
    > INVENTORY
    KEYS, a set of keys
    > DROP keys
    Dropped.
    > INVENTORY
    inventory is empty.
    >

Op basis van deze objecten navigeer je op een andere manier door verschillende kamers. Heb je de sleutels in het bezit, dan kan je in de volgende kamer door de "strong steel grate", anders niet.

    You are in a 20-foot depression floored with bare dirt.
    Set into the dirt is a strong steel grate mounted in
    concrete.  A dry streambed leads into the depression from
    the north.
    > DOWN
    Beneath grate
    You are in a small chamber beneath a 3x3 steel grate to
    the surface.  A low crawl over cobbles leads inward to
    the west.
    >

# What to do

* Implementeer Crowther's Adventure
* Laad de data uit de meegeleverde bestanden in
* Start het spel, en laat de speler commando's invoeren
* Voer de commando's van de speler uit

Adventure is een grotere opdracht waarin je stap voor stap het spel opbouwt. Je zult onderweg keuzes moeten maken hoe je delen implementeert, en dat kan op heel veel verschillende manieren! Onderweg zul je merken dat sommige eerder gemaakte keuzes misschien niet helemaal handig waren. Het kan best zijn dat je later in de opdracht jouw programma een beetje moet aanpassen als er nieuwe features in het spel komen. Dit is daarom echt een oefening in programma design!

## Om te beginnen
Bij deze opdracht leveren we data & code mee. Deze kun je [hier downloaden](https://github.com/Jelleas/adventure/archive/master.zip)

Je vindt hier 5 databestanden voor 3 versies van Adventure. `TinyRooms.txt` is de kleinste versie, dit is een spel met maar 3 kamers. Een goed punt om mee te beginnen! `SmallRooms.txt` en `SmallObjects.txt` is net ietsje groter, hier worden ook objecten bij gebruikt. Het volledige spel, de gehele dataset voor Adventure vind je in `CrowtherRooms.txt` en `CrowtherObjects.txt`.

Ook vind je 1 .py bestand genaamd `adventure.py`. Daarin vind je verschillende classes, functies en meerdere `#TODO`s. Hierin ga jij straks aan de slag!

# Fase 1: Tiny (8 uur)

## Stap 1: Kamers (3 uur)
In `TinyRooms.txt`, de kleinste instantie van het spel, vind je de volgende data:

    1
    Outside building
    You are standing at the end of a road before a small brick
    building.  A small stream flows out of the building and
    down a gully to the south.  A road runs up a small hill
    to the west.
    -----
    WEST     2
    UP       2
    NORTH    3
    IN       3

    2
    End of road
    You are at the end of a road at the top of a small hill.
    You can see a small building in the valley to the east.
    -----
    EAST     1
    DOWN     1

    3
    Inside building
    You are inside a building, a well house for a large spring.
    -----
    SOUTH     1
    OUT       1

Dit zijn de beschrijvingen van alle kamers in het spel, en hoe je van 1 kamer naar een ander komt. Elke kamerbeschrijving bestaat uit 4 delen:

    <id>
    <name>
    <description>
    ----
    <routes>

Nu moeten we deze data inlezen zodat we straks in het spel tussen de verschillende kamers kunnen navigeren. Aangezien een kamer wat ingewikkelder is dan enkel een nummer of een string introduceren we hiervoor een nieuwe class genaamd `Room` in `adventure.py`. Ook introduceren we een functie genaamd `loadRooms` die verantwoordelijk is voor het inlezen van de rooms uit het bestand dat we willen inladen.

Het is aan jou om `Room` en `loadRooms` te implementeren. __Belangrijk__ negeer voor nu de routes, dit tackle je straks in stap 2. Je kan je code testen door onderaan het bestand `stap 1` en de bijbehorende code te uncommenten. Je zou dan bij het runnen van de code het volgende moeten krijgen:

    fase 1, stap 1
    room 1: Outside building
    room 2: End of road
    room 3: Inside building

## Stap 2: Routes (3 uur)
Voeg de volgende methode toe aan `Room`:

    def move(self, command):
        """
        Go to the next room based on command
        Takes in a text based command, i.e. WEST or IN or EAST
        Returns the room (a Room object) connected to said command
        Returns None if the command does not exist
        """
        # TODO

Het is aan jou om deze methode te implementeren. Hiervoor moet je wel allereerst de routes data uit het databestand inlezen en op een handige manier onthouden. Jij kiest zelf hoe je dit aanpakt, maar we geven je wel wat tips.

Zo kan je kiezen om een soort tabel bij te houden, met daarin hoe alle kamers verbonden zijn. Denk bijvoorbeeld aan het gebruik van een dictionary. Dan kun je de combinatie van een kamer (of enkel een kamer id) en een richting gebruiken als key, met de bestemming als value. Zoals bijvoorbeeld hieronder:

    room = {}
    # als je vanuit kamer 1 naar WEST gaat kom je in kamer 2
    room_connections[(1, "WEST")] = 2

Je kan ook kiezen om deze informatie per kamer op te slaan. Dus geen aparte tabel, maar per kamer onthouden hoe je vanuit die kamer in andere kamers komt. Zo kan je een attribuut aan een kamer toevoegen om deze verbindingen te onthouden. Bijvoorbeeld als volgt:

    class Room:
        def __init__(...):
            ...
            self.connections = {}

    def loadRooms(...):
        ...
        room.connections["WEST"] = 1

Je kunt jouw code voor stap 2 testen door onderaan het bestand `fase 1, stap 2` en de bijbehorende code te uncommenten.

## Stap 3: Interactiviteit (1 uur)
Tijd om er een spel van te maken door de speler commando's te laten invoeren. Maak hiervoor de functie `play` af. __Belangrijk__ je hoeft nog geen rekening te houden met extra commando's zoals `LOOK` en `HELP`.

Als de speler een kamer voor de eerste keer bezoekt dan moet hij de volledige descriptie van de kamer te zien krijgen. Gevolgd door een regel met `>`, een prompt. Daarna mag de speler een commando invoeren. Dit ziet er zo uit:

    You are standing at the end of a road before a small brick
    building.  A small stream flows out of the building and
    down a gully to the south.  A road runs up a small hill
    to the west.
    >

Voert de speler een zet in die niet kan, dan doe je het volgende:

    > OUT
    Invalid command.
    >

Voert de speler een zet in naar een kamer die de speler al gezien heeft, dan laat je enkel de naam van de kamer zien:

    You are standing at the end of a road before a small brick
    building. A small stream flows out of the building and
    down a gully to the south. A road runs up a small hill
    to the west.
    > WEST
    You are at the end of a road at the top of a small hill.
    You can see a small building in the valley to the east.
    > EAST
    Outside building.
    >

## Stap 4: Help! (1 uur)
Behalve rondbewegen kan de speler ook nog een paar extra commando's uitvoeren. Implementeer nu de commando's `QUIT`, `HELP` en `LOOK`.

`HELP` print instructies voor het spel. Zorg dat precies deze instructies worden geprint:

    > HELP
    You can move by typing directions such as EAST/WEST/IN/OUT
    QUIT quits the game.
    HELP prints instructions for the game.
    INVENTORY lists the object in your inventory.
    LOOK lists the complete description of the room and its contents.
    TAKE <obj> take obj from the room.
    DROP <obj> drop obj from your inventory.

`QUIT` laat de speler het spel stoppen, print `Thanks for playing!` en eindig vervolgens het spel:

    > QUIT
    Thanks for playing!

`LOOK` print de volledige descriptie van de kamer, ook al heb je deze eerder bezocht:

    Inside building
    > LOOK
    You are inside a building, a well house for a large spring.

# Fase 2: Small & Crowther (10 uur)
De basis staat, je hebt een spel met kamers waartussen de speler kan bewegen, en een paar commando's om de speler te helpen in het spel. Nu ga je werken aan verschillende features in het spel. Zoals het toevoegen van objecten aan het spel, conditionele verplaatsingen, en geforceerde verplaatsingen.

## Stap 1: Objecten (3 uur)
Objecten in Adventure hebben een naam, een beschrijving en bevinden zich in een kamer. Tenminste, zolang de speler de objecten niet heeft opgepakt. Om deze Objecten te introduceren in het spel zul je een aantal stappen moeten ondernemen.
Allereerst staan de objecten net als de kamers in een databestand, `SmallObjects.txt` en `CrowtherObjects.txt` respectievelijk. Je moet deze objecten dus inlezen uit deze bestanden. In `SmallObjects.txt` vind je het volgende:

    KEYS
    a set of keys
    3

    LAMP
    a brightly shining brass lamp
    8

    ROD
    a black rod with a rusty star
    12

Een stuk simpelers dan kamers dus! Het patroon is als volgt:

    name
    description
    room_id

Net zoals bij kamers bestaan objecten uit meerdere eigenschappen, namelijk een naam en een descriptie. Hiervoor kunnen we dus ook goed een class gebruiken. Zowel de class (`Object`) en de functie om de objecten in te lezen (`loadObjects`) hebben we al aangemaakt. Nu is het aan jou om deze te implementeren. __Let op__, begin nog niet met het plaatsen van objecten in kamers. Dit tackelen we bij de volgende stap.

Je kunt jouw code testen door onderaan het bestand fase 2, stap 1 en de bijbehorende code te uncommenten. Je zou dan het volgende op jouw scherm moeten zien:

    fase 2, stap 1
    KEYS: a set of keys
    LAMP: a brightly shining brass lamp
    ROD: a black rod with a rusty star

## Stap 2: Objecten in kamers (3 uur)
Objecten kunnen zich in kamers bevinden, maar ook in het bezit van de speler. Laten we ons nu focussen op objecten in kamers. In eerste instantie liggen alle objecten in kamers zoals gespecificeerd in het objecten data bestand.

Allereerst komt hierbij de vraag: hoe houd je bezit bij in je programma? Een kamer kan één of meerdere objecten bezitten, en de speler later ook. Je kan er ook andersom naar kijken, een object is altijd in het bezit van één kamer of de speler. Jij beslist zelf hoe je dit implementeert in jouw programma. Je zou bijvoorbeeld per kamer een verzameling (bijvoorbeeld een lijst) kunnen bijhouden met alle objecten in die kamer. Of bijvoorbeeld per object in welke kamer deze zich bevindt.

Begin vervolgens met het inladen van objecten in de kamers volgens het databestand. Zorg ervoor dat elk aangemaakt object in de juiste kamer komt te liggen.

Zodra de speler een kamer bezoekt met daarin één of meerdere objecten moeten deze worden uitgeprint als volgt:

    You are inside a building, a well house for a large spring.
    KEYS: a set of keys

In het volgende formaat:

    <description>
    <object_1>
    <object_2>
    etc.

Voeg deze feature, het uitprinten van objecten in een kamer, ook toe aan het `LOOK` commando. Als volgt:

    > LOOK
    You are inside a building, a well house for a large spring.
    KEYS: a set of keys
    >

## Stap 3: Objecten in bezit (2 uur)
Implementeer nu het commando `TAKE <obj>`. Door middel van `TAKE` kan een speler het object oppakken. In andere woorden, bezit gaat van een kamer naar de speler. Er zijn natuurlijk wat randgevallen. Wat nou als de speler een niet bestaand object wil oppakken, of een object dat zich in een andere kamer bevindt? In beide gevallen print je `"No such object."`. Uiteindelijk ziet het spelverloop er zo uit:

    You are inside a building, a well house for a large spring.
    KEYS: a set of keys
    > TAKE KEYS
    KEYS taken.
    > TAKE KEYS
    No such object.
    > TAKE SOMETHING
    No such object.
    >

Je zult om dit te implementeren bezit moeten bijhouden voor de speler. Dat kan bijvoorbeeld door middel van een verzameling, zoals een lijst.

De speler kan objecten laten vallen d.m.v. het DROP <obj> commando. Hier gaat bezit van de speler naar de kamer waar de speler zich in bevindt. Ook hier is er een randgeval, zo kan de speler vragen om iets te droppen wat niet in zijn/haar bezit is. Dan print je ook `"No such object."`. Uiteindelijk ziet het er zo uit:

    You are inside a building, a well house for a large spring.
    KEYS: a set of keys
    > TAKE KEYS
    KEYS taken.
    > DROP KEYS
    KEYS dropped.
    > DROP KEYS
    No such object.
    > TAKE KEYS
    KEYS taken.

Let erop dat het object nadat deze is gedropt weer op te pakken is!

Tot slot ontbreekt nog het `INVENTORY` command, en dit is een goed moment om deze te introduceren. Het `INVENTORY` commando print alle items in het bezit van de speler. Als volgt:

    > INVENTORY
    KEYS: a set of keys
    LAMP: a brightly shining brass lamp
    > DROP KEYS
    KEYS dropped.
    > INVENTORY
    LAMP: a brightly shining brass lamp
    > DROP LAMP
    LAMP dropped.
    > INVENTORY
    Your inventory is empty.
    >

## Stap 3: Conditionele verplaatsingen (4 uur)
Nu je objecten in het spel hebt geïmplementeerd, wordt het spel meteen een stuk interessanter. Zo kan je nu conditionele verplaatsingen implementeren, verplaatsingen die afhangen van het bezit van bepaalde objecten. Zo kun je in kamer 6 via `DOWN` naar kamer 7 of 8, afhankelijk van of je de keys in je bezit hebt. Je zult dus om verder te komen in het spel eerst de keys moeten vinden en oppakken.

In de databestanden met rooms zie je conditionele verplaatsingen als volgt:

    DOWN       8/KEYS
    DOWN       7

Er is altijd maar één conditie, en dat is altijd een object. Als je dat object in je bezit hebt, dan ga je in bovenstaande geval naar 8, anders 7.

Deze feature maakt het bewegen tussen kamers iets ingewikkelder. Je zult behalve enkel de richting en de kamer nu ook moeten bijhouden of er een extra conditionele verplaatsing is. Afhankelijk van jouw gekozen aanpak zul je jouw code misschien moeten aanpassen.

Zo kun je ervoor kiezen om de bestemming van een verplaatsing in een lijst op te slaan. Bijvoorbeeld als volgt:

    connection["DOWN"] = [(8, "KEYS"), (7, None)]

In plaats van:

    connection["DOWN"] = 7

Als je hebt gekozen voor een aanpak om deze extra data te onthouden en deze hebt geïmplementeerd, rest er nog één stap. Dat is bij een verplaatsing nu ook rekening te houden met een mogelijke conditionele verplaatsing. Uiteindelijk zou je het volgende spel verloop moeten hebben:

    You are in a 25-foot depression floored with bare dirt.
    Set into the dirt is a strong steel grate mounted in
    concrete.  A dry streambed leads into the depression from
    the north.
    > DROP KEYS
    KEYS dropped.
    > DOWN
    The grate is locked and you don't have any keys.
    > FORCED
    Outside grate
    KEYS: a set of keys
    > TAKE KEYS
    KEYS taken.
    > DOWN
    You are in a small chamber beneath a 3x3 steel grate to
    the surface.  A low crawl over cobbles leads inward to
    the west.
    LAMP: a brightly shining brass lamp
    >

## Stap 4: Geforceerde verplaatsingen (3 uur)
Zoals je bij de vorige stap al hebt gemerkt bestaat er een FORCED richting voor een verplaatsing. Dit staat voor een geforceerde beweging. Dat is een beweging die meteen automatisch gebeurt, zonder dat de speler iets kan invoeren. Zo wordt er in een kamer met `FORCED` de gehele beschrijving van de kamer uitgeprint, en vervolgens beweeg je meteen naar de kamer waar `FORCED` je heen leidt.

Op deze manier worden er dus een soort status berichten uitgeprint. Bijvoorbeeld in Small om aan te geven dat het hek op slot zit. In Crowther wordt deze truc ook gebruikt voor het einde van het spel. Werp even een blik op kamers 70 t/m 75. Dit zijn kamers met een conditionele `FORCED` beweging. Heb je alle objecten op zak dan bereik je uiteindelijk kamer 77 en heb je het spel gewonnen, anders 76 en moet je nog doorgaan met zoeken naar de `"treasures"`. Het interessante is hier dat kamers 70 t/m 75 geen beschrijving hebben! Zo wordt het mogelijk, door weliswaar 5 extra kamers te introduceren, om een conditionele beweging te introduceren in het spel op basis van 6 objecten.

Nu is het aan jou om deze `FORCED` verplaatsing in het spel te introduceren. Gelukkig heeft een kamer met een `FORCED` beweging geen andere bewegingen. Dus daar hoef je ook geen rekening mee te houden!

Het spel verloop ziet er dan als volgt uit:

    You are in a 25-foot depression floored with bare dirt.
    Set into the dirt is a strong steel grate mounted in
    concrete.  A dry streambed leads into the depression from
    the north.
    > INVENTORY
    Your inventory is empty.
    > DOWN
    The grate is locked and you don't have any keys.
    Outside grate
    > DOWN
    The grate is locked and you don't have any keys.
    Outside grate
    >

Let erop dat je bij een kamer met een FORCED beweging altijd de gehele descriptie uitprint. Je hebt namelijk geen kans om even te `LOOK`en.
