# Ontwerpprincipes

> **Individuele opdracht.**
>
> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.
>
> **Je gebruikt deze opdracht om dit te leren:**
>
> - Hoe je ontwerpprincipes kunt gebruiken om een programma te schrijven, en
> - hoe je deze ontwerpprincipes tot het uiterste kunt gebruiken om iets van te leren.
>
> Na maken van de opdracht kun je extra bestuderen hoe je bovenstaande dingen hebt aangepakt.


Deze opdracht bouwt voort op je eigen implementie van de Calendar-opdracht. Deze is al flink opgedeeld in verschillende functies. Maar het opsplitsen van een programma in functies kun je nog véél verder doorvoeren. Daar ga je hier mee experimenteren.

Onderdeel van deze opdracht is het schrijven van een verslag over jouw aanpak. Hieronder vind je meer instructies.

## Ontwerpprincipes

Je opdracht is om je programma **zo veel mogelijk** te laten voldoen aan de volgende ontwerpprincipes:

- *Zo weinig mogelijk variabelen* --- Gebruik alleen variabelen wanneer strikt noodzakelijk, bijvoorbeeld als je een loop nodig hebt om een statistiek te berekenen. Gebruik wel *parameters* om informatie aan andere functies door te geven.

- *Functies met maar één regel* --- Maak je functies zo kort mogelijk. Heb je twee regels nodig, dan kun je waarschijnlijk een deel afsplitsen naar een nieuwe functie.

- *Functie met maar één taak* --- Deze regel is een alternatieve manier om naar de aanpassingen te kijken. Zorg dat functies maar één taak uitoefenen: een beslissing nemen (if/else), iets printen, iets analyseren.

- *Zo weinig mogelijk argumenten/parameters* --- Geef je functies zo weinig mogelijk argumenten. Heel vaak kun je af met een enkel argument.

Hou daar bij ook de volgende richtlijnen in de gaten. De code die je eerder hebt geschreven voldoet hier al grotendeels aan.

- *Command/query separation* [[link](https://martinfowler.com/bliki/CommandQuerySeparation.html)]. Zorg dat je functies zo veel mogelijk één doel hebben: ofwel iets uitrekenen (een query), ofwel iets doen (een command). Printen is een typisch voorbeeld van iets *doen*.

- *Namen die de rol van de functie aangeven* --- Geef functies namen die expliciet duidelijk maken of de functie een "command" of een "query" is. De functienamen in de oorspronkelijke opdracht geven hiervan al een aantal voorbeelden (maar `days_in_month` en `days_in_year` zijn niet expliciet genoeg).

- *Geen gedeelde variabelen* --- Gebruik geen globale variabelen om informatie tussen functies te delen, en gebruik geen pointers om variabelen door te geven aan andere functies.

That's it!

Om aan de opdracht te voldoen is het nodig om deze principes echt uit te proberen en te exploreren. Je moet hierin heel ver gaan, dus echt blijven kijken of het technisch lukt om functies nog een keer te splitsen, variabelen te elimineren enz.

## Testen

Zorg dat je uiteindelijke programma nog steeds correct werkt met de checks van Calendar:

    check50 -l minprog/programmeren-ki/2021/other/calendar

## Verslag

Analyseer in ongeveer 500 woorden hoe je uiteindelijke programma is geworden. Denk aan de volgende punten:

- Voor alle functies: welke functies heb je kunnen opsplitsen, en welke onderdelen heb je dan in aparte functies gezet.
- Waar was het moeilijk om een oplossing te verzinnen, binnen de ontwerpprincipes, en waarom?
- Bij welke functies/onderdelen had je ook een alternatieve oplossing in gedachten?
- Welke principes zou je goed kunnen toepassen bij het schrijven van programma's en waarom? Welke voordelen en nadelen kun je bedenken?

Schrijf je verslag in een bestand `analyse.txt`.
