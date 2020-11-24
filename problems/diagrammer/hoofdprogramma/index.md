# Integreren in het hoofdprogramma

Dit is de vierde en laatste stap van de opdracht.

In de eerste drie stappen heb je classes gemodelleerd, JSON ingelezen en weggeschreven én verschillende bewerkingen geïmplementeerd: alle puzzelstukjes om de Diagrammer tool af te maken. In deze stap ga je dat doen door een hoofdprogramma te schrijven die gebruik maakt van je eerdere werk. Het hoofdprogramma zal gebruikers in staat stellen om de bewerkingen toe te passen op opgeslagen figuren en deze weer weg te schrijven in één console command.


## Gebruik van het hoofdprogramma

We willen het hoofdprogramma met de volgende vorm als basis kunnen aanroepen:

    diagrammer.py source destination operation [parameter1, parameter2 ...]

Concreet betekent dit dat bijvoorbeeld de volgende opdrachten geldig zouden zijn:

    diagrammer.py complex.fig simple.fig merge-layers
    diagrammer.py large.fig small.fig scale 0.5

Als de gebruiker op een verkeerde manier gebruik maakt van het programma, stellen we de gebruiker daarvan op de hoogte:

    > python3 diagrammer.py sourcefile.fig
    > Usage: diagrammer.py source destination operation [parameter1, parameter2 ...]

    > python3 diagrammer.py large.fig small.fig scale
    > Scale factor is missing!

    > python3 diagrammer.py does-not-exist.fig new.fig merge-layers
    > Source file does not exist!


## Implementeren van het hoofdprogramma

Het hoofdprogramma moet grofweg vijf stappen kunnen uitvoeren, namelijk de volgende:

1. Het laden van de tekst uit het bronbestand;
2. Het omzetten van de platte JSON naar een structuur bestaande uit instanties van onze classes (deserialisatie);
3. Het uitvoeren van de gekozen bewerking;
4. Het omzetten van het bewerkte canvas naar JSON (serialisatie);
5. Het wegschrijven van de JSON naar het doelbestand.

Zoals je weet heb je voor stappen 2, 3 en 4 al functies en classes geschreven die je daarbij helpen.

Zodat andere programmeurs verder kunnen bouwen op de door jouw geschreven classes en functies, moet het hoofdprogramma alleen uitgevoerd worden als we deze rechtstreeks aanroepen. Het programma moet bijvoorbeeld niet draaien als we jouw programma in andere code importeren. Je kan hiervoor het hoofdprogramma in een `if __name__ == '__main__':` blok zetten, zoals je al eerder bent tegengekomen.

Omdat onze classes voor bewerkingen wellicht niet altijd de meest duidelijke namen hebben voor eindgebruikers, gebruiken we wat meer gebruikersvriendelijke namen voor de bewerkingen, zoals 'merge-layers' in plaats van 'MergeLayersOperation'. Bedenk zelf goede namen voor iedere bewerking die je hebt geïmplementeerd. De verschillende bewerkingen en hun vereisten (bijvoorbeeld bepaalde noodzakelijke parameters) kan je 'hard' in het hoofdprogramma programmeren.

Bij gebruikersfouten moet altijd een voor de gebruiker leesbaar bericht naar de console worden geschreven. Geef geen errors op basis van assertions: die zijn echt voor jou en voor andere programmeurs, niet voor eindgebruikers. Uiteraard kan het krijgen van een `AssertionError` wel voor jou een signaal zijn dat je misschien een mogelijke gebruikersfout over het hoofd hebt gezien. Die kan je dan alsnog implementeren.


## Testen

Test je implementatie aan de hand van de voorbeelden uit [stap 3](bewerkingen). Dit maal doe je dit echter door diagrammer.py te gebruiken als een eindgebruiker dat zou doen. Test ook weer aan de hand van een aantal zelfverzonnen figuren. Test ook hoe het hoofdprogramma reageert op onjuiste opdrachten, bijvoorbeeld door parameters weg te laten of onjuiste parameters in te vullen.


## Inleveren

Lever de eindversie van Diagrammer hieronder in. Deze eindversie wordt voorzien van feedback en wordt beoordeeld op de kwaliteitsaspecten. Je kan tot de deadline onbeperkt opnieuw inleveren.

Dit was Diagrammer!
