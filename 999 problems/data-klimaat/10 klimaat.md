# Klimaat

![](temperatuur.png){:.inline}

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren die door de ECA (European Climate Assessment) [beschikbaar](http://eca.knmi.nl/dailydata/predefinedseries.php) wordt gemaakt in grote data files. We beperken ons tot data die de maximumtemperatuur beschrijft voor elke dag in De Bilt sinds 1901.

Download dit [data bestand](klimaat.data), open het en lees bovenin hoe de data gecodeerd is.
We gaan het data bestand analyseren en op basis van de data een aantal vragen beantwoorden. Dit alles gaan we presenteren in een Jupyter Notebook.

### Tussenstap 1: Jupyter Notebook intro
**Jupyter notebook** is een handige tool voor het creeëren van verslagen met 'live' code. Zie ook wat marketing van jupyter.org:
"*The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.*". Om deze redenen is dit een steeds populairder wordende tool. Ongetwijfeld zul je Jupyter Notebook bij andere vakken tegenkomen en gebruiken. Daarom gaan we Jupyter Notebook introduceren in deze opdracht.

Eerst zul je het notebook moeten installeren. Ook dit kunnen we weer doen dankzij pip. Voer simpelweg het volgende commando in de terminal:

Ubuntu:

    python3 -m pip install jupyter --user

Mac:

	python3 -m pip install jupyter

Windows:

	py -3 -m pip install jupyter

Heb even geduld na het uitvoeren hiervan. Zodra alles geïnstalleerd is, kun je Jupyter Notebook starten door het volgende commando in de terminal in te voeren:

Ubuntu / Mac

    jupyter notebook

Windows:

	py -3 -m jupyter notebook

Je ziet nu een nieuwe webpagina openen. Er zijn drie tabjes: `Files`, `Running`, en `Clusters`. We hebben voor nu enkel de eerste nodig. Navigeer binnen `Files` naar een plek waar je jouw werk wilt opslaan. Dit zijn simpelweg de mappen op jouw computer, dus je kan altijd een nieuwe map aanmaken voor jouw werk. Zodra je bent aangekomen, klik je rechtsboven op het dropdown-menu `new`. Kies hier voor een Python 3 notebook. Dan opent er een nieuw tabblad met daarin een nieuwe notebook.

Voor we beginnen, ga linksboven naar het dropdown-menu `file` en klik `rename`. Noem je nieuwe notebook: `klimaat`. In jouw notebook heb je zogenaamde cells. Dat zijn vakken waar je zowel code als tekst kan schrijven. Aangezien we een Python 3 notebook hebben, kunnen we Python 3 code schrijven. Probeer maar eens: `print(3 * 4)`. Voer je dit in de cell, en druk je vervolgens op shift+enter (zo run je een cell), dan zie je direct onder de cell de uitkomst! Druk je enkel op enter, dan krijg je een extra regel binnen de cell.

Nieuwe cells kun je aanmaken met de knoppen bovenin het scherm, en je kan ze ook verplaatsen. Uitkomsten van cells zijn beschikbaar in andere cells, zo kun je verder werken met eerdere berekeningen. Let wel, cells updaten niet automatisch als je een andere cell runt. Je zal de cells of handmatig opnieuw moeten runnen of meerdere tegelijk via het dropdown menu `Cell`.

Je hebt binnen jouw Python 3 notebook toegang tot je gehele Python 3 installatie. Dus ook de modules die je hebt geïnstalleerd zoals `matplotlib`. Vergeet ze niet te importeren, net zoals je normaal ook zou doen. Maak eens een cell aan, plak daarin de volgende code, en druk op shift+enter.

Ubuntu:

    import matplotlib.pyplot as plt
    %matplotlib inline
    plt.plot(range(10))
    plt.savefig("some_plot.png")

Mac / Windows:

    import matplotlib.pyplot as plt
    plt.plot(range(10))
    plt.savefig("some_plot.png")

Zo heb je meteen de grafiek onder jouw code! (Maakt het nakijken ook een stuk makkelijker ;)

Behalve code, kunnen we ook tekst schrijven. Dit gaat in Markdown. Dat is een simpel mark-up taaltje (vandaar ook de naam). Zo kun je kopjes aanmaken met hekjes. Bijvoorbeeld `# Klimaat` creeërt een grote kop met de tekst Klimaat. Voeg je meer hekjes toe, dan krijg je een steeds kleiner kopje. Er zijn meer dingen die je kan doen, zoals links toevoegen, dikgedrukte tekst etc. Wil je meer weten over Markdown, google even!

> Little fun fact, alle tekst op deze website is geschreven in Markdown.

### Tussenstap 2: Preprocessing

Helaas steekt het data bestand op een orginele, niet standaard manier in elkaar. Dat betekent dat we niet direct gebruik kunnen maken van modules om data in te lezen en te verwerken. We zullen eerst een beetje moeten preprocessen, de data zo wegschrijven dat we er makkelijk mee kunnen werken. Uitleg over hoe je met bestanden omspringt in Python [vind je hier](/theory/file-io).

We willen dit in het `.csv` (Comma,Seperated,Values) formaat krijgen. Dat is een fijn formaat voor o.a. Excel, maar ook voor de module pandas die we zo gaan gebruiken. De naam zegt het al, alle waardes in dit formaat zijn gescheiden door een komma. De eerste regel van het nieuwe `.csv` bestand, genaamd `klimaat.csv`, moet bestaan uit alle kolomnamen, gescheiden door een komma. De volgende 761 regels moeten alle datapunten zijn, elk op één regel, waar alle waardes gescheiden zijn door een komma.

Schrijf een cell (code) dat `klimaat.data` omzet naar `klimaat.csv`. Houd het simpel, en kijk goed naar de uitkomst.

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.


### Tussenstap 3: Pandas Intro

Nu we `klimaat.csv` hebben kunnen we gebruik maken van bestaande modules om de data in te lezen en te verwerken. Scheelt een hoop werk! Wij gaan werken met **pandas**, een populaire dataverwerking module voor Python. Pandas wordt echter niet meegeleverd met Python. We zullen deze moeten downloaden en installeren. Geen paniek! Dit kan weer simpelweg door middel van **pip** (Pip Installs Python). Het enige wat we hoeven te doen om pandas te installeren is de volgende regel uit te voeren in de terminal:


Ubuntu:

    python3 -m pip install pandas --user

Mac:

	python3 -m pip install pandas

Windows:

	py -3 -m pip install pandas

Bovenstaande regel voert Python uit en vertelt Python om de module pip uit te voeren d.m.v. de `-m` (module) flag. Dan wordt aan pip de argumenten `install` en `pandas` meegegeven, wat pip pandas laat installeren. Dat is alles, je hebt nu de module pandas tot je beschikking!

Laten we beginnen met een voorbeeld. Maak een cell aan en zet daarin de volgende code:

Ubuntu:

    import matplotlib.pyplot as plt
    %matplotlib inline
    import pandas as pd

    # read data
    data = pd.read_csv("klimaat.csv")

    # plot long and lat data
    plt.plot(data["DATE"], data["TX"])

    # save plot
    plt.savefig("temp.png")

Mac / Windows:

    import pandas as pd
    import matplotlib.pyplot as plt

    # read data
    data = pd.read_csv("klimaat.csv")

    # plot long and lat data
    plt.plot(data["DATE"], data["TX"])

    # save plot
    plt.savefig("temp.png")

Deze code begint met pandas te importeren door middel van `import pandas as pd`. We kunnen nu `klimaat.csv` inladen d.m.v. `data = pd.read_csv("klimaat.csv")`. De functie `read_csv` van pandas creëert een `Dataframe`. Dat is een datastructuur van pandas waar we straks heel makkelijk berekeningen mee kunnen doen, en waardes uit kunnen halen. Zo kun je kolommen uit dit `Dataframe` ophalen als volgt: `data["DATE"]`. Vervolgens kun je individuele waardes ophalen als volgt: `data["DATE"][0]`. Ook kun je bepaalde berekeningen in één keer loslaten op een hele serie aan data, bijvoorbeeld: `data["TX"].mean()` geeft je de gemiddelde temperatuur. Behalve al dit kunnen we ook gemakkelijk dingen plotten met `matplotlib`. Run de cell maar eens, je ziet dan de temperatuur tegenover de datums.

### Tussenstap 4: Extremen
Tijd voor wat analyse! We gaan onderzoeken wat de maximale en minimale temperatuur gemeten is in De Bilt sinds het begin van de 20e eeuw. We gaan ook kijken op welke dagen dit was.

Maak een nieuwe cell dat het databestand opent en de maximale en minimale temperatuur vind en uitprint. Dit doe je elk op een nieuwe regel, met daarnaast op welke dag deze temperatuur gemeten is. Als volgt:

    De maximale temperatuur was 34.5 graden op 13 mei 1967
    De minimale temperatuur was -1.0 graden op 7 aug 1990

Bovenstaande antwoorden zijn natuurlijk fout, je mag zelf de juiste waarden vinden. Om je wat extra uit te dagen willen we ook de datum in het bovenstaande formaat hebben, met de maanden niet in cijfers, maar in 3 letters. Het is handig om hier een functie voor te schrijven!

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.

### Tussenstap 5: Vriesperiode

Maak een nieuwe cell dat de lengte van de langste periode dat het aaneengesloten heeft gevroren (temperatuur onder de 0 graden Celsius) uitprint. Print daarnaast wat de laatste dag van deze vriesperiode was. Doe dit weer met de maand in 3 letters. Als volgt:

    De langste vriesperiode is 12 dagen en eindigde op 29 jun 1999.

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.


### Tussenstap 6: Zomerse dagen

We spreken van een zomerse dag als de temperatuur tenminste 25 graden Celcius was. Maak een nieuwe cell dat een grafiek maakt waarin voor elk jaar het aantal zomerse dagen weergegeven wordt. Zorg dat de jaartallen op de x-as staan, en het aantal zomerse dagen op de y-as. Vergeet geen labels langs de assen te plaatsen!

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.


### Tussenstap 7: Eerste hittegolf

We spreken in Nederland van een hittegolf als de temperatuur ten minste vijf dagen achtereen minstens 25 graden Celsius was (zomerse dagen) waarvan ten minste op drie dagen 30 graden Celsius of meer (tropische dagen). Maak een nieuwe cell dat uitprint wat het *eerste* jaartal is waarin er sprake was van een hittegolf volgens deze regels.

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.


## Testen

	checkpy klimaat
