# Auto

Een mobiele telefoon bevat veel delicate sensoren die informatie verzamelen over de positie, snelheid, versnelling. Een stel natuurkundigen hebben gedurende een korte auto-rit de data opgeslagen en in een bestand weggeschreven met een frequentie van 1[Hz]. Het verzamelen van de data begon toen de auto zich bevond op de plek waar de snelweg A4 op de ringweg A10 aansluit. Het verzamelen van de data stopte toen de auto op het Nikhef was aangekomen.

![](kaartamsterdam.png)

We gaan de data van de rit analyseren en visueel maken door deze over een map van amsterdam te leggen. Zo kan je precies zien waar de auto heeft gereden. Ook gaan we onderzoeken waar de auto meer dan 50 km/uur heeft gereden.

De sensordata is beschikbaar in het bestand `autorit.data`, deze kan je [hier](autorit.data) downloaden.

### Tussenstap 1: Jupyter Notebook intro
**Jupyter notebook** is een handige tool voor het creeëren van verslagen met 'live' code. Zie ook wat marketing van jupyter.org:
"*The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.*". Om deze redenen is dit een steeds populairder wordende tool. Ongetwijfeld zul je Jupyter Notebook bij andere vakken tegenkomen en gebruiken. Daarom gaan we Jupyter Notebook introduceren in deze opdracht.

Eerst zul je de notebook moeten installeren. Ook dit kunnen we weer doen dankzij pip. Voer simpelweg het volgende commando in de terminal:

    python -m pip install jupyter

> Let op! Type python3 als jij op jouw computer zo python 3 aanroept.

Heb even geduld na het uitvoeren hiervan. Zodra alles geïnstalleerd is, kun je Jupyter Notebook starten door het volgende commando in de terminal in te voeren:

    jupyter notebook

Je ziet nu een nieuwe webpagina openen. Er zijn drie tabjes: `Files`, `Running`, en `Clusters`. We hebben nu enkel de eerste nodig. Navigeer binnen `Files` naar een plek waar je jouw werk wilt opslaan. Dit zijn simpelweg de mappen op jouw computer, dus je kan altijd een nieuwe map aanmaken voor jouw werk. Zodra je bent aangekomen, klik je rechtsboven op het dropdown-menu `new`. Kies hier voor een Python 3 notebook. Dan opent er een nieuw tabblad met daarin een nieuwe notebook.

Voor we beginnen, ga linksboven naar het dropdown-menu `file` en klik `rename`. Noem je nieuwe notebook: `auto`. In jouw notebook heb je zogenaamde cells. Dat zijn vakken waar je zowel code als tekst kan schrijven. Aangezien we een Python 3 notebook hebben, kunnen we Python3 code schrijven. Probeer maar eens: `print(3 * 4)`. Voer je dit in de cell, en druk je vervolgens op shift+enter (zo run je een cell), dan zie je direct onder de cell de uitkomst! Druk je enkel op enter, dan krijg je een extra regel binnen de cell.

Nieuwe cells kun je aanmaken met de knoppen bovenin het scherm, en je kan ze ook verplaatsen. Uitkomsten van cells zijn beschikbaar in andere cells, zo kun je verder werken met eerdere berekeningen. Let wel, cells updaten niet automatisch als je een andere cell runt. Je zal de cells of handmatig opnieuw moeten runnen of meerdere tegelijk via het dropdown menu `Cell`.

Je hebt binnen jouw Python 3 notebook toegang tot je gehele Python 3 installatie. Dus ook de modules die je hebt geïnstalleerd zoals `matplotlib`. Vergeet ze niet te importeren, net zoals je normaal ook zou doen. Maak eens een cell aan, plak daarin de volgende code, en druk op shift+enter.

    import matplotlib.pyplot as plt
    plt.plot(range(10))
    plt.show()

Zo heb je meteen de grafiek onder jouw code! (Maakt het nakijken ook een stuk makkelijker ;)

Behalve code, kunnen we ook tekst schrijven. Dit gaat in Markdown. Dat is een simpel mark-up taaltje (vandaar ook de naam). Zo kun je kopjes aanmaken met hekjes. Bijvoorbeeld `# Klimaat` creeërt een grote kop met de tekst Klimaat. Voeg je meer hekjes toe, dan krijg je een steeds kleiner kopje. Er zijn meer dingen die je kan doen, zoals links toevoegen, dikgedrukte tekst etc. Wil je meer weten over Markdown, google even!

> Little fun fact, alle tekst op deze website is geschreven in Markdown.

### Tussenstap 2: Preprocessing

Helaas steekt het data bestand op een orginele, niet standaard manier in elkaar. Dat betekent dat we niet direct gebruik kunnen maken van modules om data in te lezen en te verwerken. We zullen eerst een beetje moeten preprocessen, de data zo wegschrijven dat we er makkelijk mee kunnen werken.

Het data bestand begint met de namen van de 36 kolommen, elk op één regel. Dan zijn er 761 datapunten met elke 36 waardes. Deze datapunten staan elk op twee regels, gevolgd door een witregel. De waardes zijn gescheiden door een `;`. Open het bestand maar eens met een tekst editor om een beeld te krijgen van het formaat.

We willen dit in het `.csv` (Comma,Seperated,Values) formaat krijgen. Dat is een fijn formaat voor o.a. Excel, maar ook voor de module pandas die we zo gaan gebruiken. De naam zegt het al, alle waardes in dit formaat zijn gescheiden door een komma. De eerste regel van het nieuwe `.csv` bestand, genaamd `autorit.csv`, moet bestaan uit alle kolomnamen, gescheiden door een komma. De volgende 761 regels moeten alle datapunten zijn, elk op één regel, waar alle waardes gescheiden zijn door een komma.

Schrijf een cell (code) dat `autorit.data` omzet naar `autorit.csv`. Houd het simpel, en kijk goed naar de uitkomst.

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.

### Tussenstap 3: Pandas intro

Nu we `autorit.csv` hebben kunnen we gebruik maken van bestaande modules om de data in te lezen en te verwerken. Scheelt een hoop werk! Wij gaan werken met **pandas**, een populaire dataverwerking module voor Python. Pandas wordt echter niet meegeleverd met Python. We zullen deze moeten downloaden en installeren. Geen paniek! Python modules zijn tegenwoordig makkelijk te downloaden en installeren, namelijk door middel van **pip** (Pip Installs Python). Het enige wat we hoeven te doen om pandas te installeren is de volgende regel uit te voeren in de terminal:

    python -m pip install pandas

> Let op! Type python3 als jij op jouw computer zo python 3 aanroept.

Bovenstaande regel voert Python uit en vertelt Python om de module pip uit te voeren d.m.v. de `-m` (module) flag. Dan wordt aan pip de argumenten `install` en `pandas` meegegeven, wat pip pandas laat installeren. Dat is alles, je hebt nu de module pandas tot je beschikking!

Laten we beginnen met een voorbeeld. Maak een cell aan en zet daarin de volgende code:


    import pandas as pd
    import matplotlib.pyplot as plt

    # read data
    data = pd.read_csv("autorit.csv")

    # plot long and lat data
    plt.plot(data["long"], data["lat"])

    # show plot
    plt.show()

Deze code begint met pandas te importeren door middel van `import pandas as pd`. We kunnen nu `autorit.csv` inladen d.m.v. `data = pd.read_csv("autorit.csv")`. De functie `read_csv` van pandas creëert een `Dataframe`. Dat is een datastructuur van pandas waar we straks heel makkelijk berekeningen mee kunnen doen, en waardes uit kunnen halen. Zo kun je kolommen uit dit `Dataframe` ophalen als volgt: `data["speed"]`. Vervolgens kun je individuele waardes ophalen als volgt: `data["speed"][0]`. Ook kun je bepaalde berekeningen in één keer loslaten op een hele serie aan data, bijvoorbeeld: `data["speed"].mean()` geeft je de gemiddelde snelheid (in m/s want `autorit.data` is van natuurkundigen ;). Behalve al dit kunnen we ook gemakkelijk dingen plotten met `matplotlib`. Run de cell maar eens, je ziet dan de gereden route. Om het wat interessanter te maken kunnen we ook een kaart van Amsterdam als achtergrond gebruiken. Om je een hoop zoekwerk te besparen hebben we dat alvast voor je gedaan met de code hieronder:


    import pandas as pd
    import matplotlib.pyplot as plt

    # read data
    data = pd.read_csv("autorit.csv")

    # create figure
    fig = plt.figure()

    # create subplot
    ax = fig.add_subplot(111)

    # plot long and lat data
    ax.plot(data["long"], data["lat"], zorder = 1)

    # set background img
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    img = plt.imread("kaart.png")
    ax.imshow(img, extent = [x0, x1, y0, y1], aspect = "auto", zorder = 0)

    # show plot
    plt.show()

> Download [hier](kaart.png) het achtergrond plaatje.

De code ziet er al meteen wat ingewikkelder uit, maar het is niks meer dan een plaatje toevoegen op de achtergrond. Enkel gebruiken we nu een subplot, en de grootte van deze subplot om het plaatje te schalen. Verwijder de oude code, copy-paste bovenstaande code in de cell, en run het nogmaals. Je ziet dan als het goed is het volgende plaatje:

![](kaartmetroute.png)


### Tussenstap 4: Afgelegde afstand

Maak een nieuwe cell dat op uitprint wat de geschatte afgelegde afstand in kilometers van de auto is. Gebruik hiervoor de snelheid op elke tijdstap, en neem aan dat er één meetpunt per seconde is gedaan (we negeren de kleine schommelingen even).

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.

### Tussenstap 5: Sneller dan 50 km/u

Maak een nieuwe cell dat de afgelegde route van de auto laat zien. Kleur de stukken waar de auto 50 km/u of sneller rijdt rood, en de stukken waar de auto langzamer dan 50km/u rijdt blauw. Print op de eerste regel uit hoeveel seconden de auto sneller heeft gereden dan 50 km/u. Let op, de snelheid in `autorit.csv` is in m/s.

Zet boven de cell met code een markdown cell met daarin tenminste een kopje en kort toegelicht wat de code eronder doet.

Om de lijnen te kleuren is het het makkelijkst om meerdere kleine lijn segmenten te plotten. Ga door de data heen, en verzamel telkens de longitude en latitude data in bijvoorbeeld een lijst. Doe dit totdat de snelheid ineens onder of boven de 50 km/u komt. Plot vervolgens de verzamelde longitudes en latitudes d.m.v. `ax.plot(longitudes, latitudes, zorder=1, color="red")`, of `color="blue"` voor een blauwe lijn.

## Testen

Er zijn geen checkpy tests voor deze opdracht. Je zult daarom zelf nauwkeurig moeten nagaan of alle antwoorden kloppen! Vergeet niet voordat je deze opdracht inlevert even alle cells opnieuw te runnen, zo weet je zeker dat ze allemaal nog werken.
