# Dict

## Definitie
Een in Python ingebouwde datastructuur is een `dict`, kort voor dictionary. Een dict is een muteerbare verzameling van key-value paren. Laten we even goed kijken naar wat dat precies inhoud.

Allereerst, een dict is een verzameling van key-value paren. Op basis van een key kun je een value ophalen. Klinkt misschien een beetje cryptisch, maar kijk even naar het volgende voorbeeld:

    some_dict = {1:3, "hello":"world"}
    print(some_dict[1])
    print(some_dict["hello"])

`some_dict` in het stukje code hierboven is zo'n dict. Hiervoor gebruik je in Python de accolades (`{}`), en de `:` om keys en values te scheiden. Links van de `:` staat de key, recht de value. Op basis van de key kan je de bijbehorende value ophalen. Zo print het bovenstaande stukje code eerst `3` en vervolgens `"world"`.

Een dict kent de volgende eigenschappen:
- Een dict is muteerbaar, dat betekent dat je de verzameling kan aanpassen (muteren). Ofwel, we kunnen er elementen uit verwijderen en aan toevoegen.
- Een dict bestaat uit key-value paren, op basis van een key haal je de bijbehorende value op. Dat betekent dat keys dus uniek zijn, je kan niet twee keer dezelfde key in een dictionary hebben. Daar zorgt de datastructuur zelf voor.

## Waarvoor / wanneer
Ben je geïntereseerd in het opslaan van data op een relationele manier (bijv. voornaam -> achternaam), dan is een dict een heel handige datastructuur!

Ook zijn dicts ontzettend snel O(1) in verschillende operaties zoals:

- Het toevoegen van elementen (voeg key-value paar K:V aan dict D toe)
- Het updaten (vervangen) van values (update value V van key K uit dict D)
- Het verwijderen van elementen (verwijder key-value paar K:V uit dict D)
- Het opzoeken van keys (zit key K in dict D?)

## Code
Een dict maak je zo aan:

    numbers = {1:3, 4:5}
    print(numbers)

Hiervoor gebruik je in Python de accolades (`{}`), en de `:` om keys en values te scheiden. Links van de `:` staat de key, recht de value. Op basis van de key kan je de bijbehorende value ophalen. Wil je een lege dict aanmaken, dan kan dat zo:

    numbers = {}
    numbers[1] = 3
    numbers[4] = 5
    print(numbers)

Bovenstaande stukje code maakt een lege dict en voegt de key-value paren 1:3 en 4:5 toe. Behalve toevoegen kunnen we natuurlijk ook verwijderen:

    numbers = {1:3, 4:5}
    del numbers[1]
    print(numbers)

Zit een key-value paar al in de dict, dan kun je de value ook updaten of vervangen. Bijvoorbeeld:

    numbers = {1:3, 4:5}
    numbers[1] = 2
    numbers[4] += 1
    print(numbers)

Tot slot, alle keys in een dict zijn uniek. Altijd. Je kan geen dubbele keys hebben. Kijk maar:

    numbers = {}
    numbers[1] = 2
    numbers[1] = 3
    print(numbers)

De syntax voor het toevoegen van keys is hetzelfde als die voor het updaten van keys. Zou je dus dezelfde key willen toevoegen, dan update je eigenlijk de oude value!
