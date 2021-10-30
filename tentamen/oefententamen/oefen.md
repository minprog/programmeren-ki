# Oefententamen

> Regels voor het tentamen:
> 
> - Ga naar de zaal die in jouw persoonlijke rooster op Datanose staat.
> - Je mag tot uiterlijk 30 minuten na de begintijd starten.
> - Je moet minimaal tot 30 minuten na de begintijd in de zaal blijven.
> - Leg je collegekaart klaar op tafel (of een andere ID met foto).
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

In je uitwerking mag je alleen gebruik maken van de library-functies die ook in de CS50 Manual staan.

Programmeren moet in de CS50 IDE. Je hebt dus alleen je webbrowser geopend met daarin enkele tabs: de CS50 IDE, de CS50 Manual, en deze cursuswebsite. Je mag geen andere programma's open hebben.

Vanwege het doel van het tentamen heeft het geen zin om alleen het juiste antwoord uit te printen zodat `check50` tevreden is (het zogenaamde "hardcoden").

De input van gebruikers hoeft alleen gecontroleerd te worden als dit duidelijk in de opdracht vermeld staat.

(Ook) voor het oefententamen is het essentieel dat je dit eerst doet zonder gebruik van internet of hulp van anderen. Alleen zo begrijp je waar je zelf nog vastloopt.

Succes!


## Vakantie

Je wil in je eentje op vakantie naar een mooie accommodatie in Frankrijk. De kosten van de reis naar het verblijf zijn afhankelijk van het gebruikte vervoersmiddel. Met het vliegtuig kost het je 250 euro, met de trein kost het 100 euro, en met de auto kost het 150 euro. Het verblijf zelf kost 60 euro per nacht. Bovendien betaal je nog 3% servicekosten over de totale kosten (dus vermenigvuldig totaal met 0.03), afhankelijk dus van hoeveel nachten je verblijft. De servicekosten worden wel naar **beneden** afgerond op hele euro's vóórdat ze bij het totaalbedrag worden opgeteld!

Schrijf een programma dat berekent hoeveel je vakantie kost op basis van het aantal dagen dat je op vakantie gaat en met welk vervoersmiddel je gaat. Controle op (on)geldige invoer is niet nodig.

    $ ./vakantie
    Hoe ga je reizen (v)liegtuig/(t)rein/(a)uto? v
    Hoeveel nachten ga je verblijven? 1
    Jouw vakantie kost: 319

    $ ./vakantie
    Hoe ga je reizen (v)liegtuig/(t)rein/(a)uto? t
    Hoeveel nachten ga je verblijven? 10
    Jouw vakantie kost: 721

    $ ./vakantie
    Hoe ga je reizen (v)liegtuig/(t)rein/(a)uto? a
    Hoeveel nachten ga je verblijven? 7
    Jouw vakantie kost: 587

Tip: begin altijd met het maken van een programma voor het **eerste** voorbeeld. Dit is het meest eenvoudig. Hiermee voorkom je dat je vastloopt in allerlei uitzonderingen. Zodra je programma werkt voor het eerste voorbeeld kun je gaan checken of het ook werkt voor de volgende voorbeelden, en je programma dan aanpassen.


## Caffeïne

Het internationale advies voor de maximale dagelijkse caffeïne-intake is 400mg voor een gezonde volwassene, 100mg voor iemand tussen 12 en 18 jaar oud, en helemaal geen caffeïne voor kinderen onder 12 jaar oud.

Hierbij een lijst met de hoeveelheid caffeïne voor één portie van verschillende dranken.

* Coffee - 90 mg
* Thee - 45 mg
* Energiedrankjes - 80 mg
* Cola - 40 mg

Schrijf een programma dat de caffeïne-inname van de gebruiker berekent en een waarschuwing print als deze te hoog is. Controle op (on)geldige invoer is niet nodig.

    $ ./caffeine 
    Hoeveel koppen koffie? 2
    Hoeveel koppen thee? 1
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 0
    Hoeveel jaar oud ben je? 22
    Je krijgt 225 mg caffeïne binnen.
    Dat is een veilige hoeveelheid caffeïne.

    $ ./caffeine 
    Hoeveel koppen koffie? 2
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 2
    Hoeveel glazen cola? 0
    Hoeveel jaar oud ben je? 17
    Je krijgt 340 mg caffeïne binnen.
    Kijk uit, dat is te veel caffeïne!

    $ ./caffeine 
    Hoeveel koppen koffie? 0
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 1
    Hoeveel jaar oud ben je? 10
    Je krijgt 40 mg caffeïne binnen.
    Kijk uit, dat is te veel caffeïne!

    $ ./caffeine 
    Hoeveel koppen koffie? 5
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 0
    Hoeveel jaar oud ben je? 38
    Je krijgt 450 mg caffeïne binnen.
    Kijk uit, dat is te veel caffeïne!


## RNA

Eiwitsynthese is het proces waarbij eiwitten worden gemaakt op basis van de informatie in het DNA. Simpel gezegd is eiwitsynthese het maken van een eiwit in een menselijke cel. De eerste stap van eiwitsynthese is de transcriptie van DNA naar RNA. (Je hoeft voorgaande niet te begrijpen.)

DNA bestaat uit verschillende moleculen, waaronder 4 nucleotiden die de DNA-code vormen: Adenine (A), Guanine (G), Cytosine (C) en Thymine (T). RNA is een zogenaamde *complementaire* transcriptie van DNA. De complementaire nucleotide van Adenine is Uracil (U), van Guanine is Cytosine, van Cysotine is Guanine en van Thymine is Adenine.

Een complementaire RNA-keten kan dus volgens een vast patroon beredeneerd worden uit de DNA-keten. Zo geeft een DNA-keten `ATGC` altijd de RNA-keten `UACG` als je bovenstaande regels toepast.

Schrijf een programma dat een keten van DNA aanneemt en de complementaire RNA-keten print. Je mag aannemen dat de DNA-keten altijd in hoofdletters wordt ingevuld. Het programma print een error message als deze een ongeldige nucleotide bevat (dus een andere letter dan A, G, C of T).

    $ ./rna
    DNA-keten: ATGC
    Dit is de bijbehorende RNA-keten: UACG

    $ ./rna
    DNA-keten: AAF
    Ongeldige DNA-keten

    $ ./rna
    DNA-keten: AAGGTTCCAA
    Dit is de bijbehorende RNA-keten: UUCCAAGGUU


## Driehoek

Schrijf een programma dat een driehoek uitprint. De gebruiker mag een hoogte opgeven. Deze hoogte mag niet kleiner dan 5 zijn en niet hoger dan 20, maar je hoeft dit **niet** te controleren!

    $ ./driehoek
    Hoe hoog moet de driehoek zijn? 5
        ##
       #  #
      #    #
     #      #
    ##########

    $ ./driehoek
    Hoe hoog moet de driehoek zijn? 15
                  ##
                 #  #
                #    #
               #      #
              #        #
             #          #
            #            #
           #              #
          #                #
         #                  #
        #                    #
       #                      #
      #                        #
     #                          #
    ##############################


## Temperaturen

Graden Celsius C en graden Fahrenheit F staan met elkaar in verband via `F = (18C + 320) / 10` en andersom `C = (10F - 320) / 18`. Schrijf een programma dat de gebruiker vraagt om de eenheid van temperatuur, of C van Celsius of F van Fahrenheit. Vervolgens vraagt het programma om de begintemperatuur, de eindtemperatuur en de stapsgrootte. Waarna een nette tabel wordt uitgeprint met op iedere rij de gekozen temperatuur en de temperatuur in de andere eenheid.

Vraag de gebruiker opnieuw om input als er iets anders dan C of F wordt gekozen voor de eenheid van temperatuur. Vraag de gebruiker ook opnieuw om input als er een stapgrootte kleiner dan 1 wordt ingevuld. 

    $ ./temperaturen
    Welke eenheid van temperatuur (C of F)? C
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 20
    Wat is de stapgrootte? 5
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68

    $ ./temperaturen
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 10
    Wat is de stapgrootte? 2
      F |   C
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12

    $ ./temperaturen 
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 100
    Wat is de eindtemperatuur? 0
    Wat is de stapgrootte? 3
      F |   C

     $ ./temperaturen 
    Welke eenheid van temperatuur (C of F)? c
    Welke eenheid van temperatuur (C of F)? v
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 9
    Wat is de stapgrootte? -3
    Wat is de stapgrootte? 0
    Wat is de stapgrootte? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12

> Tip: zo print je een waarde uit met een vaste lengte `printf("%3d", getal)`. Is `getal` hier bijvoorbeeld `9`, dan worden er twee spaties uitgeprint voor de `9` om zo toch de opgegeven lengte 3 te krijgen.



## Inleveren

Heb je één van de opdrachten niet gedaan? Maak dan een leeg bestand aan met de juiste naam, en gebruik dit om hieronder in te leveren.

Let op dat de website een automatische check doet (exact op de input/output die ook hierboven in de voorbeelden staat), maar deze kan nog geen Python-uitwerkingen checken. 

