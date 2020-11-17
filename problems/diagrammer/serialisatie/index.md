## Inlezen en wegschrijven

Dit is stap 2 van de opdracht.

De `diagrammer`-tool moet straks bestanden kunnen inlezen en wegschrijven. Hiervoor gebruiken we de data-taal JSON, waarmee je precies genoeg uitdrukkingskracht hebt om combinaties van objecten en eigenschappen te omschrijven. Stel, je hebt het volgende diagram als objecten in het geheugen:

![](square.png)

Dan zou de bijbehorende omschrijving in JSON er zo uit kunnen zien:

    {                                                <-- top-level object
        "diagrammer_version": 1.0,                   <-- versie van tool
        
        "canvas":                                    <-- canvas is één vast object
        {
            "layers": [                              <-- layers is een lijst van layers
                {                                    <-- layer-object
                    "objects": [                     <-- objects is een lijst van objecten
                        {                            <-- enkel object met diverse eigenschappen
                            "type": "square",
                            "size": 4,
                            "position":
                            {
                                "x": 0,
                                "y": 0
                            }
                        }
                    ]
                }
            ]
            
        }
    }

In bovenstaande structuur zie je dat er twee lijsten voorkomen: `layers` en `objects`. Elk bestand heeft een lijst met `layers` en elke layer heeft een lijst met `objects`. Zo'n lijst bevat 0 of meer objecten, afhankelijk van de inhoud van het diagram.

Onderstaande code bevat een "minified"-versie van het JSON-bestand om mee te testen.

    import json
    diagram_source = '{"diagrammer_version":1,"canvas":{"layers":[{"objects":[{"type":"square","size":4,"position":{"x":0,"y":0}}]}]}}'
    diagram = json.loads(diagram_source)
    print(diagram)
    print(len(diagram['canvas']['layers']))    <- er zou 1 layer moeten zijn
    print(diagram['canvas']['layers'][0]['objects'][0]['size'])

Zorg dat je goed begrijpt hoe dit werkt voordat je verder gaat. Op [RealPython](https://realpython.com/python-json/) staat een uitleg over JSON in Python. Het is overigens niet nodig om nu de geavanceerde technieken te gebruiken met custom Python encoders, zoals in het tweede deel van die pagina wordt behandeld.


## Inlezen

Met de gegeven code kun je het bestand inlezen en benaderen als Python-dictionaries en -lists. Jouw taak is om een **functie** te schrijven die een JSON-string verwerkt, inleest met `json.loads()` en dan instanties aanmaakt van de door jou in stap 1 gedefinieerde classes. Zo zou je bijvoorbeeld door de layers heen kunnen lopen:

    for json_layer in json_layers:
        layer = Layer()
        verwerk alle objects uit het bestand met een loop
        voeg de nieuwe layer toe aan het Canvas() object

Als je deze functie laat werken op de bovenstaande `diagram_source` zou er een complete set van Python-objecten klaar moeten staan zodat je deze kunt gebruiken om transformaties toe te passen. Het is daarbij niet nodig om bijvoorbeeld het versienummer van het bestandstype over te nemen.


## Wegschrijven

Het omzetten van een objectenstructuur van Diagrammer naar een JSON werkt op dezelfde manier: je schrijft een **functie** die door een interne objectenstructuur loopt en stap voor stap dictionaries en lists aanmaakt en omzet naar een JSON-string met behulp van `json.dumps()`. Deze moet weer precies de benodigde informatie bevatten om het diagram later weer te kunnen inlezen.


## Testen

Je twee functies zouden precies op elkaar moeten passen. Als je een JSON-string hebt, dan inleest naar objecten, en dan de objecten weer wegschrijft naar een JSON-string, dan zou deze precies gelijk moeten zijn (spaties en enters daargelaten). Kortom, er mag geen inhoud verloren gaan. Zorg dus dat je dit uitgebreid test, ook met diagrammen waar meerdere objecten in zitten, of die meerdere layers bevat.


## Volgende stap

In de volgende stap ga je de classes bouwen die transformaties op diagrammen kunnen uitvoeren.
