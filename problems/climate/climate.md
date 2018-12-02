# Climate

## Jupyter Notebook

Om je voor te bereiden op verschillende andere vervolgvakken, maak je nu alvast kennis met Jupyter Notebook. Dat is een omgeving waarin je kan programmeren als wel tekst kan schrijven. Een ideale omgeving om de resultaten van jouw programma te presenteren, maar ook een ideaal formaat voor vakken (zoals dit vak) om hun opdrachten in te verspreiden.

Je runt jupyter notebook in de cs50 IDE d.m.v.

    jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser

Vervolgens zie je een link staan in de terminal, open deze in je browser. 

### workaround

Krijg je de volgende error? 

	Error executing Jupyter command 'notebook': [Errno 2] No such file or directory

Dan om het notebook te runnen is er op dit moment alleen deze work-around:

  jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser

Vervolgens ga je in jouw browser naar:

  http://ide50-JOUW_USERNAAM_HIER.cs50.io:8080/tree

Waar je JOUW_USERNAAM_HIER vervangt door jouw Edx usernaam. Jouw usernaam zie je ook uitgeprint in de terminal na het uitvoeren van het jupyter commando.

Vervolgens krijg je een scherm dat je vraagt om een token. Dit token kun je vinden in de terminal, daar staat ook een URL met een stukje token=XXXXXX. Kopieer alle tekens na token=, en vul deze in. Nu ben je klaar om te beginnen!

Deze oplossing verdient geen schoonheidsprijs, maar het zou moeten werken. Stuur zeker een mail als je er niet uit komt!

### Notebook

Zodra je de notebook open hebt staan in jouw webbrowser, zie je hier drie tabjes: Files, Running, en Clusters. We hebben nu enkel de eerste nodig. Navigeer binnen Files naar een plek waar je jouw werk wilt opslaan. Dit zijn simpelweg de mappen op jouw computer (in dit geval IDE50), dus je kan altijd een nieuwe map aanmaken voor jouw werk. Zodra je bent aangekomen, klik je rechtsboven op het dropdown-menu `new`. Kies hier voor een Python3 notebook. Dan opent er een nieuw tabblad met daarin een nieuwe notebook.

Voor we beginnen, ga linksboven naar het dropdown-menu file en klik rename. Noem je nieuwe notebook: auto. In jouw notebook heb je zogenaamde cells. Dat zijn vakken waar je zowel code als tekst kan schrijven. Aangezien we een Python 3 notebook hebben, kunnen we Python3 code schrijven. Probeer maar eens: `print(3 * 4)`. Voer je dit in de cell, en druk je vervolgens op shift+enter (zo run je een cell), dan zie je direct onder de cell de uitkomst! Druk je enkel op enter, dan krijg je een extra regel binnen de cell.

Nieuwe cells kun je aanmaken met de knoppen bovenin het scherm, en je kan ze ook verplaatsen. Uitkomsten van cells zijn beschikbaar in andere cells, zo kun je verder werken met eerdere berekeningen. Let wel, cells updaten niet automatisch als je een andere cell runt. Je zal de cells of handmatig opnieuw moeten runnen of meerdere tegelijk via het dropdown menu Cell.

Behalve code, kunnen we ook tekst schrijven. Dit gaat in Markdown. Dat is een simpel mark-up taaltje (vandaar ook de naam). Zo kun je kopjes aanmaken met hekjes. Bijvoorbeeld # Klimaat creeërt een grote kop met de tekst Klimaat. Voeg je meer hekjes toe, dan krijg je een steeds kleiner kopje. Er zijn meer dingen die je kan doen, zoals links toevoegen, dikgedrukte tekst etc. Spiek maar even in de opdrachten straks!

## What to do

Hier ga je data analyseren door bestanden in te lezen, te verwerken en weg te schrijven. Zie [/theory/file-io](/theory/file-io).

De opdracht download je zo:

    wget https://github.com/Jelleas/climate/archive/master.zip
    unzip master.zip
    rm master.zip
    mv climate-master climate
    cd climate

Je start jupyter notebook in de CS50 IDE door middel van:

    jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser

## Testen

### check50

    check50 uva/progki/2018/climate
