# Bewerkingen uitvoeren

Dit is stap 3 van de opdracht.

Nu je een manier hebt om bestanden in te lezen en weg te schrijven, is het tijd om ook daadwerkelijk veranderingen aan te brengen in de bestanden. We willen de figuren bijvoorbeeld kunnen schalen of alle lagen kunnen samenvoegen. Om dat uiteindelijk in het hoofdprogramma in te bouwen bij de volgende stap, gaan we nu eerst de verschillende bewerkingen die we willen kunnen uitvoeren implementeren.


## Hoe implementeren we bewerkingen?

Om deze uiteindelijk in het hoofdprogramma te kunnen gebruiken, moet iedere soort bewerking die we gaan implementeren richting het hoofdprogramma hetzelfde werken. In het hoofdprogramma willen we als volgt een bewerking kunnen toepassen:

    operation = MergeLayersOperation()
    diagram = operation.apply(diagram)

De class `MergeLayersOperation` is hierin een door ons gedefiniëerde bewerking (later meer over wat iedere bewerking moet doen). We passen deze bewerking in dit voorbeeld toe op `diagram`, een instantie van de class `Canvas`. Je herkent in dit voorbeeld direct een te implementeren method: `apply()`. Deze method past de bewerking toe op het gegeven figuur en returnt het nieuwe figuur.

Maar wat nu als we een wat ingewikkeldere bewerking willen doen? Bij een bewerking als schalen willen we bijvoorbeeld een factor kunnen meegeven, zodat we een figuur met iedere factor kunnen vergroten of verkleinen. Dat doen we in het hoofdprogramma als volgt:

    operation = ScaleOperation(2)
    diagram = operation.apply(diagram)

Hierin hebben we bij het instantiëren van onze operation direct meegegeven met welke factor we het figuur willen schalen. In dit geval wordt alles in het figuur tweemaal zo groot. Om dit te realiseren moet de constructor van `ScaleOperation` een parameter aannemen en deze in het geheugen bewaren, om deze later bij het uitvoeren van `apply()` te kunnen gebruiken. Dit is natuurlijk alleen nodig als de bewerking daadwerkelijk een parameter nodig heeft.

Door iedere bewerking op dezelfde manier te implementeren kunnen we verschillende bewerkingen gemakkelijk in het hoofdprogramma implementeren. Bovendien maakt dat het eenvoudig om in de toekomst nieuwe bewerkingen toe te voegen.


## De verschillende bewerkingen

Nu duidelijk is hoe een bewerking in de basis werkt, gaan we kijken welke bewerkingen we in Diagrammer gaan implementeren. Implementeer ieder van deze bewerkingen als een eigen class, naar de vorm die hierboven beschreven is. Bij iedere bewerking staat een voorbeeld in JSON ter verduidelijking en zodat je jouw implementatie kan testen. De gebruikte naamgeving van attributen is bedoeld ter illustratie, jouw implementatie van de serializer kan hierin afwijken.


### Schalen

De bewerking `ScaleOperation` schaalt het gehele figuur met een aan te geven factor. Neem bijvoorbeeld het volgende object dat onderdeel uitmaakt van een figuur:

    {
        "type": "square",
        "size": 4,
        "position":
        {
            "x": 4,
            "y": 2
        }
    }

Als we het figuur waar dit object zich in bevindt schalen met een factor 2, verandert deze in het volgende:

    {
        "type": "square",
        "size": 8,
        "position":
        {
            "x": 8,
            "y": 4
        }
    }

Je ziet dat niet alleen de grootte van het object wordt vermenigvuldigd met 2, maar dat ook de coördinaten vermenigvuldigd worden. Dat moet ook wel, immers: alle andere objecten worden ook groter en anders komen ze onderling op andere posities terecht.


### Lagen samenvoegen

De bewerking `MergeLayersOperation` voegt alle lagen van een figuur samen in één laag. Deze bewerking accepteert geen parameters. Neem bijvoorbeeld onderstaande structuur van lagen:

    "layers": [
        {
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                }
            ]
        },
        {
            "objects": [
                {
                    "type": "square",
                    "size": 2,
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Bij het uitvoeren van deze bewerking, onstaat de volgende structuur:

    "layers": [
        {
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                },
                {
                    "type": "square",
                    "size": 2,
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Er is nu nog maar één laag, waarin alle objecten zich bevinden. Als het figuur al maar één laag had, blijft het figuur in principe hetzelfde.


### Lagen splitsen

De bewerking `SplitLayersOperation` is de tegenpool van de `MergeLayersOperation`. Deze bewerking plaatst ieder object in het figuur in een eigen laag. Zie bijvoorbeeld onderstaande structuur:

    "layers": [
        {
            "objects": [
                {
                    "type": "circle",
                    "radius": 2,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                },
                {
                    "type": "square",
                    "size": 4,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                }
            ]
        },
        {
            "objects": [
                {
                    "type": "square",
                    "radius": 2,
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Wanneer de `SplitLayersOperation` wordt uitgevoerd, ontstaat het volgende:

    "layers": [
        {
            "objects": [
                {
                    "type": "circle",
                    "radius": 2,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                }
            ]
        },
        {
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                }
            ]
        },
        {
            "objects": [
                {
                    "type": "square",
                    "radius": 2,
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Het maakt hierbij niet uit in welke laag een object zich bevindt. Ieder object krijgt een eigen laag. Wanneer er geen lagen zijn met twee of meer objecten, verandert het figuur niet.


### Zichtbaarheid van lagen aanpassen

Lagen kunnen zichtbaar en onzichtbaar worden gemaakt. De `ToggleLayerOperation` wisselt een specifieke laag van zichtbaar naar onzichtbaar of andersom. Neem bijvoorbeeld de volgende structuur met lagen:

    "layers": [
        {
            "visible": true
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                }
            ]
        },
        {
            "visible": true
            "objects": [
                {
                    "type": "square",
                    "size": 2,
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Als we hierop `ToggleLayerOperation(1)` toepassen, ontstaat het volgende:

    "layers": [
        {
            "visible": true
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                }
            ]
        },
        {
            "visible": false
            "objects": [
                {
                    "type": "square",
                    "size": 2,
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Zoals te zien is beginnen we met tellen vanaf 0, zoals computers vaak doen. De geselecteerde laag wisselt van zichtbaar naar onzichtbaar. Als de laag al onzichtbaar was, had deze zichtbaar geworden. Mocht de gebruiker een laag proberen te veranderen die niet bestaat, in dit voorbeeld bijvoorbeeld laag nummer 2, mislukt de bewerking en verandert er niets.


### Kleuren vervangen

We kennen vast allemaal het emmertje met verf uit Microsoft Paint nog. De bewerking `ReplaceColorOperation` doet eigenlijk precies dat, maar dan op de hele afbeelding. We kiezen twee kleuren: de oorspronkelijke kleur en een nieuwe kleur. In ieder object waar de oorspronkelijke kleur voorkomt, vervangen we deze door de nieuwe kleur. Neem bijvoorbeeld het voorbeeld hieronder:

    "layers": [
        {
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "color":
                    {
                        "border": "000000",
                        "fill": "FF0000"
                    },
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                },
                {
                    "type": "square",
                    "size": 2,
                    "color":
                    {
                        "border": "FF0000",
                        "fill": "000000"
                    },
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Als we hierop `ReplaceColorOperation("FF0000", "00FF00")` ('vervang de kleur rood met de kleur groen') toepassen, ontstaat het volgende:

    "layers": [
        {
            "objects": [
                {
                    "type": "square",
                    "size": 4,
                    "color":
                    {
                        "border": "000000",
                        "fill": "00FF00"
                    },
                    "position":
                    {
                        "x": 0,
                        "y": 0
                    }
                },
                {
                    "type": "square",
                    "size": 2,
                    "color":
                    {
                        "border": "00FF00",
                        "fill": "000000"
                    },
                    "position":
                    {
                        "x": 4,
                        "y": 4
                    }
                }
            ]
        }
    ]

Zoals te zien maakt het niet uit of het gaat om een kleur van een rand of een vulkleur. Het maakt verder ook niet uit als kleuren anders worden gerepresenteerd dan in dit voorbeeld. Mocht de oorspronkelijke kleur niet voorkomen in het figuur, dan verandert er niets.


### Een eigen bewerking

Verzin ook zelf een bewerking en implementeer deze. Het maakt niet uit wat deze bewerking precies doet, dus wees vooral creatief!


## Omgaan met onverwachte of ontbrekende input

Net als in eerdere opdrachten moeten we ook hier omgaan met onverwachte input in onze classes. Voeg nu zelf assertions toe die controleren of *een class op de juiste manier wordt gebruikt*. Je controleert dus met assertions of alle vereiste input wordt gegeven en of de input redelijk is.

Je kan je misschien wel voorstellen dat het schalen van een figuur met een factor 0.000001 voor problemen zal zorgen, dus dit is een voorbeeld van een assertion die de factor binnen een redelijk bereik houdt:

    assert type(factor) == int
    assert 0 < factor < 100

Assertions hoeven niet compleet te zijn, maar kunnen de meest obvious programmeerfouten voorkomen als de voorwaarden goed gekozen zijn. Edge cases die beschreven zijn bij de specifieke bewerkingen mogen in ieder geval niet resulteren in een error.


## Testen

Naast het testen aan de hand van de gegeven voorbeelden, is het handig om de bewerkingen ook te testen met een aantal zelfverzonnen figuren. Doe dat ook zeker met wat complexere figuren met meerdere lagen en verschillende objecten.


## Inleveren

Lever vóórdat je verder gaat hieronder je uitwerking in voor feedback en advies.


## Volgende stap

In de volgende stap ga je de eerste drie stappen combineren in één hoofdprogramma, zodat we in de console gemakkelijk bewerkingen kunnen uitvoeren op opgeslagen figuren.
