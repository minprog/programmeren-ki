# Exercises: Loops

Bij deze oefening ga je kleine algoritmes schrijven. De meeste hiervan zullen je bekend voorkomen, want het zijn varianten van de onderdelen van de opdrachten die je afgelopen weken hebt gemaakt. 

> De antwoorden moet je schrijven als C-code. Hierbij hoef je niet op de puntkomma's te letten, maar het moet geen pseudocode zijn. Soms is het nodig om C-specifieke functies te gebruiken zoals `strlen()`. Schrijf dus zo netjes mogelijk C.

Had je de video van Doug nog niet gezien? Hij geeft een overzicht van de verschillende soorten loops in C en waarvoor we ze gebruiken.

![embed](https://www.youtube.com/embed/WgX8e_O7eG8?autoplay=1&rel=0)


## Loops

In elk algoritme zul je loops tegenkomen, bijvoorbeeld om herhaaldelijk iets te vragen aan een gebruiker, of om een berekening te doen met een hele lijst van getallen.

**Voorbereiding**

- Bestudeer de `do`--`while`-loop die je in [Mario](https://prog1.mprog.nl/problems/mario-less#specification) nodig had om te zorgen dat de gebruikersinvoer tussen 0 en 23 bleef.
- Bestudeer hoe je een [blok](https://prog1.mprog.nl/problems/mario-less#block) en een [piramide](https://prog1.mprog.nl/problems/mario-less) heb gemaakt door `for`-loops te combineren.

**Oefeningen**

1.  Schrijf een loop die de variabele `n` vult met invoer van de gebruiker (`get_int()`). De ingevoerde waarde moet negatief zijn.

		int n;

2.  Print een mario-pyramide van hoogte `h`. Let op dat we in dit geval niet specificeren wat de hoogte `h` is: je moet een algoritme schrijven dat werkt voor alle (redelijke) waarden van `h`.

		int h;

In sommige gevallen geven we wel een waarde, bijvoorbeeld `int h = 3;`. Ook dan moet je algoritme werken voor andere waarden dan 3, maar het is vaak fijn om even een voorbeeld te hebben.

## Strings

Loops kun je ook gebruiken om een hele string door te lopen en te verwerken. Hiervan heb je kort geleden al enkele voorbeelden uitgeprogrammeerd.

**Voorbereiding**

* Bestudeer goed het doorlopen en selectief printen van strings zoals in [Initials](https://prog1.mprog.nl/problems/initials-less).
* Bestudeer het manipuleren van ascii-waardes zoals in [Caesar](https://prog1.mprog.nl/problems/caesar).

**Oefeningen**

-   Schrijf een loop die van alle woorden in de string `tale` de laatste letter uitprint.

		string tale = "It was the best of times";

-   Schrijf een loop die van de string `bob` de hoofdletters uitprint.

		string bob = "pRoGgRaMmInG In c";

-   Print de string `knight`, maar vervang daarbij alle letters 'a' door een 'o'.

		string knight = "Batman";

## Arrays

In onze programma's en voorbeelden bevatten arrays vaak getallen van type `integer` of `float`. Met behulp van loops kun je de informatie in zo'n array bijvoorbeeld **samenvatten**. Ook kun je een array **analyseren**, bijvoorbeeld om het kleinste element te vinden.

**Voorbereiding**

In de opdracht **Find** heb je binary search geïmplementeerd. Dat algoritme zal je niet hoeven reproduceren op een toets, maar je kan wel varianten op linear search verwachten (zie het [college](https://prog1.mprog.nl/lectures/algorithms#searching)).

**Oefeningen**

-   Schrijf een loop die in de array `numbers` zoekt of het getal `3` voorkomt. dat in het is besproken (de lengte van de array is gegeven door `length`).

		int numbers[] = {7, 3, 4, 5};
		int length = 4;

-   Schrijf een loop die het gemiddelde berekent van de getallen in array `numbers` en opslaat in de variabele `avg`.

		int numbers[] = {5, 7, 2, 4, 6};
		int length = 5;
		int avg;

Op papier een algoritme uitwerken is echt een andere oefening dan hetzelfde doen op een computer. Je kan niet tussendoor uitproberen of het werkt. Oefen dus goed met de bovenstaande onderwerpen voor je de toets gaat maken.
