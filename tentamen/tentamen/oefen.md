# Tentamen

> Regels voor het tentamen:
> 
> - Je mag tot uiterlijk 30 minuten na de begintijd starten.
> - Je moet minimaal tot 30 minuten na de begintijd in de zaal blijven.
> - Leg je collegekaart klaar op tafel (of een andere ID met foto).
> - Leg je telefoon op tafel (zet 'm uit).
> - Zet whatsapp enzo uit op je laptop.
> - Stilte in de zaal.
> - Er is geen pauze, overdrijf niet met drinken, toiletbezoek op verzoek.
> - Klaar is klaar, dan kun je inleveren en weggaan.
> - Voor inleveren steek je je hand op, de surveillant komt controleren voordat je inlevert.

Hieronder vind je vijf opdrachten. Het doel van het tentamen is te demonstreren dat je zelfstandig een oplossing voor een probleem kunt ontwikkelen, en daarbij gebruik kunt maken van de basistechnieken van programmeren, zoals bijvoorbeeld de verschillende soorten loops, if-else-constructies, enzovoort.

Op dit moment in de cursus zou je alle opdrachten goed moeten kunnen maken zonder begeleiding. Door de tijdsbeperking kan het best zijn dat je een opdracht niet kunt maken! Dat hoeft geen probleem te zijn, als maar overtuigend zichtbaar is dat je het programmeren beheerst.

Als bronnen mag je gebruiken:

1. de lecture notes (en de rest van deze website),
2. de CS50 Manual waarin allerlei nuttige C-functies genoemd staan,
3. en je eigen uitwerkingen van eerdere opdrachten.

Verder gebruik van internet of hulp van anderen is niet toegestaan.

In je uitwerking mag je alleen gebruik maken van de library-functies die ook in de CS50 Manual staan (of soortgelijke functies in Python als je het tentamen per se in Python wil doen).

Programmeren moet in de CS50 IDE. Je hebt dus alleen je webbrowser geopend met daarin enkele tabs: de CS50 IDE, de CS50 Manual, en deze cursuswebsite. Je mag geen andere programma's open hebben.

Vanwege het doel van het tentamen heeft het geen zin om alleen het juiste antwoord uit te printen zodat `check50` tevreden is (het zogenaamde "hardcoden").

De input van gebruikers hoeft alleen gecontroleerd te worden als dit duidelijk in de opdracht vermeld staat.

Succes!

## Rechthoeken

Schrijf een programma dat de afmetingen van twee rechthoeken opvraagt en dan de mogelijkheid geeft om enkele eigenschappen te berekenen. Het gaat om de volgende mogelijkheden:

1. De opppervlakte van de eerste rechthoek (lengte x breedte)
1. De opppervlakte van de tweede rechthoek (lengte x breedte)
1. Het verschil van de oppervlakte van de eerste en tweede rechthoek (opp1 - opp2)
1. De som van de oppervlakte van de eerste en tweede rechthoek (opp1 + opp2)

De lengtes en breedtes moeten ingevoerd worden als een geheel getal.
Controle op (on)geldige invoer is alleen nodig voor de keuze 1, 2, V of S.

    $ ./rechthoeken
    Lengte 1: 45
    Breedte 1: 33
    Lengte 2: 22
    Breedte 2: 12
    Wil je de oppervlakte van rechthoek (1) of (2), of de (S)om of het (V)erschil weten? V
    1221

    $ ./rechthoeken
    Lengte 1: 1
    Breedte 1: 43
    Lengte 2: 39
    Breedte 2: 31
    Wil je de oppervlakte van rechthoek (1) of (2), of de (S)om of het (V)erschil weten? S
    1252

    $ ./rechthoeken
    Lengte 1: 1
    Breedte 1: 43
    Lengte 2: 39
    Breedte 2: 31
    Wil je de oppervlakte van rechthoek (1) of (2), of de (S)om of het (V)erschil weten? 1
    43

    $ ./rechthoeken
    Lengte 1: 1
    Breedte 1: 43
    Lengte 2: 39
    Breedte 2: 31
    Wil je de oppervlakte van rechthoek (1) of (2), of de (S)om of het (V)erschil weten? X
    Dit is geen geldige keuze

    $ ./rechthoeken
    Lengte 1: 1
    Breedte 1: 43
    Lengte 2: 39
    Breedte 2: 31
    Wil je de oppervlakte van rechthoek (1) of (2), of de (S)om of het (V)erschil weten? 0
    Dit is geen geldige keuze

Als geen geldige keuze wordt gemaakt stopt het programma; er wordt niet opnieuw om invoer gevraagd.


## Hoofdletters

Tekstanalyse is een veelgebruikte toepassing. Hoewel dit vaak gebeurt op basis van technieken uit de AI, kunnen eenvoudige statistieken soms heel verhelderend zijn.

Schrijf een programma dat telt hoeveel woorden in een tekst met een hoofdletter beginnen.

    $ ./teller
    Tekst: Er zijn geen goede schrijvers.
    1 woord met een hoofdletter

    $ ./teller
    Tekst: Obi-Wan Kenobi nam zijn taak vrij serieus
    2 woorden met een hoofdletter

    $ ./teller
    Tekst: Het leven op zondag begon zonder Onrust.
    2 woorden met een hoofdletter

    $ ./teller
    Tekst: ergens heeft het ook wel wat
    0 woorden met een hoofdletter


## Regen

Schrijf een programma dat op basis van de invoer de gemiddelde hoeveelheid regen berekent. De gebruiker mag één of meer dagelijkse hoeveelheden regen invullen. Als er geen invoer meer is, dan kan de gebruiker 999 intikken om af te sluiten. Het gemiddelde hoeft geen cijfers achter de komma (punt) te hebben en er mag altijd naar beneden worden afgerond, zoals uit de voorbeelden hieronder blijkt.

Tip: hou geen lijsten/arrays bij maar tel de waarden er steeds bij zodra ze binnenkomen.

Implementeer eerst een programma voor een normale invoer:

    $ ./regen
    Hoeveel: 12
    Hoeveel: 12
    Hoeveel: 999
    Gemiddeld 12 millimeter
    
    $ ./regen
    Hoeveel: 12
    Hoeveel: 6
    Hoeveel: 3
    Hoeveel: 999
    Gemiddeld 7 millimeter

En kijk dan hoe je foutafhandeling kunt inbouwen:

    $ ./regen
    Hoeveel: 999
    Dat kan niet

En tot slot check je of je algoritme ook werkt als het gemiddelde eigenlijk geen geheel getal is:

    $ ./regen
    Hoeveel: 12
    Hoeveel: 11
    Hoeveel: 999
    Gemiddeld 11 millimeter


## Spraaksynthese

Een getal kan worden opgedeeld in cijfers. Het getal 423 bijvoorbeeld, bestaat uit de cijfers 4, 2 en 3. Men wil een spraaksynthesizer gebruiken om getallen uit te spreken, en wel cijfer na cijfer. Het getal 423 moet dus worden uitgesproken als 'vier', 'twee', 'drie'.

Schrijf een programma dat een getal cijfer na cijfer, als woord, naar het scherm schrijft zó dat elk woord op een nieuwe regel komt.

Tip: gebruik de functie `get_string()` om invoer te vragen, zodat je de cijfers stap voor stap kunt doorlopen. Gebruik geen `get_int()` of iets dergelijks, want dat maakt het ingewikkeld.

    $ ./spraaksynthese
    Getal: 123
    een
    twee
    drie

    $ ./spraaksynthese
    Getal: 4210
    vier
    twee
    een
    nul

## Email-validator

Mensen hebben nogal eens de neiging om een niet-bestaande waarde in te voeren in de computer, bijvoorbeeld als om hun mailadres gevraagd wordt. Of ze begrijpen het gewoon niet.

Daarom gebruiken websites vaak een email-validator om te controleren of de invoer **redelijk OK** is. De validator is niet compleet, maar voorkomt een aantal fouten.

Schrijf een email-validator op basis van de volgende regels:

- Er moet een `@` in zitten
- Vóór de `@` moet minstens één letter staan (A-Z of a-z)
- Na de `@` moet tenminste één `.` staan.

Begin simpel:

    $ ./mail
    Adres: mdaks@gmail.com
    Geldig
    
    $ ./mail
    Adres: a@gmail.nl
    Geldig

En dan wat minder goed gaat:

    $ ./mail
    Adres: @
    Ongeldig
    
    $ ./mail
    Adres: me.@com
    Ongeldig

    $ ./mail
    Adres: m.raak@student.uva.nl
    Geldig
