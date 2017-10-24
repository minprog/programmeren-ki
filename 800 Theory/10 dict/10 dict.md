# Dictionary

Python heeft een aantal in de taal ingebouwde datastructuren. Eén daarvan is een zogenaamde dictionary, ofwel `dict` in het kort. Een `dict` is een datastructuur die in tegenstelling tot een `list` geen indices kent. In plaats daarvan werkt een `dict` met **key-value pairs**. Je hebt sleutels die bijbehorende waarden kunnen ophalen. Laten we gelijk kijken naar een voorbeeld:

    last_names = {"Jelle" : "van Assema", "Thomas" : "Kamps", "Mike" : "Brink"}

Bovenstaande creeërt een dictionary met de speciale syntax voor dictionaries, namelijk de curly braces (ze worden toch ergens voor gebruikt in Python ;). Dan zie je drie key-value paren. De keys zijn `"Jelle"`, `"Thomas"` en `"Mike"`. De bijbehorende values zijn `"van Assema"`, `"Kamps"` en `"Brink"`. De namen zitten aan elkaar gelinkt, vul je voornaam in (de key), dan krijg je de achternaam terug (de value). In actie:

    >>> last_names["Jelle"]
    van Assema
    >>> last_names["Thomas"]
    Kamps

Dit is een bijzonder handige datastructuur voor het bewaren van bij elkaar horende data. Deze datastructuur is ook nog is bijzonder snel! Zonder teveel in detail te gaan, want daar is tenslotte het vak Datastructuren voor, maakt een dictionary van de ingevulde key een index (integer). Op basis van deze integer wordt de value opgehaald. Deze operatie gaat in O(1)! Ook elementen toevoegen en verwijderen gaan in O(1). Toevoegen en verwijderen doe je als volgt:

    >>> last_names["Jesse"] = "Blom"
    >>> del last_names["Mike"]

Over een `dict` kun je net zoals met een `list` (en vele andere datastructuren) loopen. Zo werkt een for-loop ook op een `dict`, alleen krijg je dan telkens een key uit de `dict`.

    >>> for first_name in last_names:
            print(last_names[first_name])
    Kamps
    Blom
    Brink
    van Assema

Als je nu denkt, huh, wat een vreemde willekeurige volgorde van achternamen? Dan heb je gelijk. Een `dict` kent geen volgorde! Je mag er niet op rekenen dat dezelfde volgorde wordt aangehouden als waarin je de elementen toevoegt. De volgorde is willekeurig. Een dictionary kent dan ook geen indices.

Het keyword `in` werkt ook op een `dict`, zo evalueert `"Thomas" in last_names` naar `True`. De `in` operatie op een `list` gaat in O(n), maar op een dictionary gaat deze zoek operatie in O(1)! Let erop dat je enkel kan vragen of een key voorkomt in een `dict`. Het is éénrichtingsverkeer, je kan enkel waardes ophalen met keys en niet andersom. Daarom kan je ook alleen maar kijken of een key in de dictionary zit. Wil je weten of een value voorkomt? Dan kun je alle values ophalen met de `.values()` functie van een dictionary. Vervolgens kun je dan vragen of de waarde erin zit, bijvoorbeeld: `"Brink" in last_names.values()`. Let wel, deze laatste operatie gaat in O(n), want het is een `list` waardoor je heen zoekt!

Er zitten wel wat haken en ogen aan een `dict`. Zo zijn de keys in een dictionary uniek. Zou je `last_names["Jelle"] = "Heringa"` uitvoeren, dan wordt de achternaam van Jelle ineens Heringa! Ofwel je update het bestaande key-value paar, in plaats van een nieuwe toevoegen. Je kan dus nooit twee van dezelfde keys in een dictionary hebben, maar natuurlijk wel twee dezelfde values.

Niet alle types in Python zijn te gebruiken als keys in een dictionary. Een designkeuze die de maker van Python (Guide van Rossum) heeft gemaakt is om alle **mutable** (veranderbare) types niet toe te staan als key in een `dict`. Dit zijn bijvoorbeeld `list` en `dict`. Het idee hierachter is, als we een key gebruiken om een value op te speuren, dan moet die key hetzelfde blijven anders kunnen we de value nooit meer vinden. Zou je een `list` als key gebruiken, en deze `list` veranderen door elementen te verwijderen of toe te voegen, dan kun je de bijbehorende value in de dictionary nooit meer vinden! Daarom mag je enkel **immutable** (niet veranderbare) types gebruiken als key in een dictionary. Dat zijn de meeste standaard meegeleverde types, zoals `int` en `string`.

> Fun fact, de zogenaamde benevolent dictator for life van Python, Guido van Rossum, heeft Python ontwikkeld op het CWI. Het gebouw net tegenover het Science Park!
