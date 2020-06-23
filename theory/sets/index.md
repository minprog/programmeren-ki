# Set

## Definitie
Een andere in de taal ingebouwde datastructuur is een set. Een set is een muteerbare verzameling van unieke elementen. Laten we even goed kijken naar wat dat precies inhoud:

- Een set is muteerbaar, dat betekent dat je de verzameling kan aanpassen (muteren). Ofwel, we kunnen er elementen uit verwijderen en aan toevoegen.
- Alle elementen in een set zijn uniek. Er zitten dus geen dubbele elementen in de verzameling, en dat kan ook niet.

## Waarvoor / wanneer
Ben je geïntereseerd in het uniek houden van een verzameling, dus geen duplicate elementen. Dan is een set een heel handige datastructuur!

Ook zijn sets ontzettend snel O(1) in verschillende operaties zoals:

- Het toevoegen van elementen (voeg element X aan set S toe)
- Het verwijderen van elementen (verwijder element X uit set S)
- Het opzoeken van elementen (zit element X in set S?)

## Code
Een set maak je zo aan:

    numbers = {3, 4}
    print(numbers)

De accolades worden ook gebruikt voor sets in Python. In tegenstelling tot dicts maken we geen gebruik van `:`. Voor de snelle lezer, hoe maak je dan een lege set aan? Dat kan je het beste doen door de `set` functie aan te roepen. Zoals hieronder:

    numbers = set()
    numbers.add(3)
    numbers.add(4)
    print(numbers)

Bovenstaande stukje code maakt een lege set en voegt er de getallen 3 en 4 aan toe. Behalve toevoegen kunnen we natuurlijk ook verwijderen.

    numbers = {3,4,5}
    numbers.remove(5)
    print(numbers)

Tot slot, alle elementen in een set zijn uniek. Altijd. Maakt niet uit of je duplicaten toevoegt. Probeer maar eens:

    numbers = {3,4}
    numbers.add(3)
    numbers.add(4)
    numbers.add(5)
    print(numbers)

## Operaties op sets
Sets zijn als datastructuur dus erg goed in bepaalde operaties zoals het kijken of een element in een set zit, maar ook het toevoegen van elementen aan een set.

Zou je bijvoorbeeld willen uitvinden welke elementen wel in set A zitten, maar niet in set B, dan kan je dat zo doen:

    set_a = {2,3,7,5}
    set_b = {5,4,7}
    result = set()
    for element in set_a:
        if element not in set_b:
            result.add(element)
    print(result)

Dit is een stukje code dat in O(n) een nieuwe set `result` maakt met daarin alle elementen uit `set_a` die niet in `set_b` zitten. Dit gaat in O(n) omdat er een loop nodig is over `set_a` (`set_a` is van lengte `n`). Alle operaties die binnen de loop worden uitgevoerd kunnen in O(1), want we werken met sets. Zou je dit met lijsten doen, dan heeft de code een complexiteit van O(n^2)! Het opzoeken van een element in een lijst gaat namelijk in O(n) i.p.v. O(1).

Python heeft een heel hoop set op set operaties standaard ingebouwd. Al deze operaties gaan in O(n):

    set_a = {2,1,3}
    set_b = {5,3,4}
    print(set_a - set_b) # alle elementen uit a die niet in b zitten
    print(set_a | set_b) # alle elementen uit a en b
    print(set_a & set_b) # alle elementen die zowel in a als b zitten
    print(set_a ^ set_b) # alle elementen die in a of b zitten, maar niet in zowel a als b

Dat stukje code met de for-loop hierboven kunnen we dus ook zo schrijven:

    set_a = {2,3,7,5}
    set_b = {5,4,7}
    result = set_a - set_b
