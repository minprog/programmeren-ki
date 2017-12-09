# File Input & Output
Alles op jouw computer is een sequentie van `1`en en `0`en. Bestanden op jouw computer zijn dus ook niet meer dan dat. Echter op basis van het type bestand springen we anders om met de `1`en en `0`en in het bestand. Open je bijvoorbeeld een `.txt` bestand met een teksteditor dan probeert de teksteditor de `1`en en `0`en te ontcijferen alsof het tekst is. Probeer je bijvoorbeeld een `.jpeg` of een `.png` te openen met een teksteditor, dan probeert de teksteditor dat nog steeds en krijg je een heel hoop chaos op jouw scherm. Het is dat die teksteditor het nog steeds kan, maar de `1`en en `0`en van het plaatje slaan nergens op als je ze interpreteert als tekst! 

Om een beetje orde te scheppen en hints te geven wat we precies moeten doen met een bestand hebben we extensies zoals `.txt` en `.jpeg`. Dit zijn enkel hints voor de verschillende programma's op jouw computer om hoe ze met het bestand moeten omspringen. De inhoud van het bestand veranderdt niet afhankelijk van de extensie! Je mag gerust een `.txt` bestand opslaan als een `.jpeg`, maar dan zal je deze vervolgens expliciet moeten openen met een teksteditor de volgende keer als je het bestand wilt openen ;)

Voor deze cursus gebruiken we een niet bestaand (of in ieder geval niet bekend) formaat `.data`. Wat daarin staat is puur tekst, je kan het dus ook openen met een teksteditor. Het vervelende is dat zo'n formaat afwijkt van conventie, en je daarom niet gemakkelijk mainstream tools kan gebruiken. Dit zal je vaker tegenkomen als je met data gaat werken. Het is daarom belangrijk dat je leert hoe je op laag niveau (dichtbij de `1`en en `0`en) leert omgaan met bestanden. Zodat je zelf vervelende formaten kunt omschrijven naar andere bekendere formaten zoals bijvoorbeeld .csv. 

In Python kan je op verschillende manieren werken met bestanden, maar je zal ongetwijfeld de `open()` functie nodig hebben. Deze functie opent een bestand voor lezen of voor schrijven. Zodra je dat hebt gedaan kun je uit het bestand lezen, en eventueel naar het bestand schrijven. Zodra je klaar bent met het bestand moet je dit weer sluiten d.m.v. `close()`. Omdat je dat laatste nog weleens wilt vergeten heeft Python een speciaal construct in het leven geroepen: de `with` statement. Deze statement sluit het geopende bestand nadat je er klaar mee bent meteen, automatisch en voor niks. Zo kan je dit nooit vergeten! Het ziet er als volgt uit:

    with open("myfile.txt") as f:
        # do magic

Laten we beginnen met wat voorbeelden. Zo kan je bijvoorbeeld een regel uit jouw bestand lezen en printen naar het scherm met:

    with open("myfile.txt") as f:
        line = f.readline()
        print(line)

Wil je het woord `"hello"` wegschrijven dan doe je dat zo:

    with open("myotherfile.txt", "w") as f:
        f.write("hello")

Let erop dat je een extra argument meegeeft aan open, in dit geval de letter `"w"` van write. Standaard opent Python een bestand in leesmodus en kun je er dus niet naar schrijven. Allebei tegelijk nu, inlezen vanuit het ene bestand, en schrijven naar de ander:

    with open("inputfile.txt") as fIn, open("outputfile.txt", "w") as fOut:
        line = fIn.readline()
        fOut.write(line)

Er zijn verschillende manieren om meerdere regels uit een bestand te lezen. De makkelijkste en gebruikelijkste is d.m.v. een for-loop. Deze stopt automatisch als je het einde van het bestand bereikt. Zo print je bijvoorbeeld de gehele inhoud van het bestand naar je scherm:

    with open("inputfile.txt") as f:
        for line in f:
            print(line)

Wil je liever handmatig lezen omdat je bijvoorbeeld meerdere regels in één keer nodig hebt. Dan kan dat ook d.m.v. een while-loop. De code hieronder print ook de gehele inhoud van het bestand naar je scherm:

    with open("inputfile.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)

Ziet er wel gelijk een stuk ingewikkelder uit. Je moet namelijk elke keer kijken of je niet al aan het einde van je bestand bent. De if-statement handelt dat geval af, ofwel als er geen regel is ingelezen stop dan met de loop. In plaats van regel voor regel inlezen kan je ook in één keer het hele bestand inlezen. Dit kan, maar is niet aan te raden met hele grote databestanden (in de meerdere gigabytes). De code hieronder leest in één keer het hele bestand in en print het regel voor regel naar het scherm.

    with open("inputfile.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
