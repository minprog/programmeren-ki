# Trump & Twitter
Zoals je waarschijnlijk wel weet is Donald Trump een zeer actieve Twitter gebruiker. Met 2500 tweets in zijn eerste jaar als president zit hij bepaald niet stil. In deze opdracht ga jij een analyse doen van Trump's tweets. Hoe great is America?

## Twitter API
Om tweets op te halen moeten we naar twitter. Het goede nieuws is, twitter stelt tweets beschikbaar via een zogenaamde Application Programming Interface (API), zodat applicaties ook toegang hebben tot delen van twitter. Via deze API hebben wij een heel hoop van trump's tweets gedownload en opgeslagen in een bestand genaamd `trump.txt`.

## Tweet analyse
Twitter is voor sociologen al jaren een interessant platform. Zo wordt er onder andere onderzoek gedaan en is er veel commerciële interesse in het sentiment van Tweets. Advertentie platformen kunnen op basis hiervan kiezen welke advertentie ze laten zien op welk moment, of juist niet. Big business dus.

Een sentiment analyse kan je op veel verschillende manieren doen. Eén zo'n manier is te kijken naar het gebruik van woorden. Zo is er onderzoek gedaan naar Engelse woorden die worden gebruikt in positieve en negatieve zin in social media. Bijvoorbeeld `great` en `good` zijn woorden die vaak in positieve context worden gebruikt.

Op basis van het woordgebruik kunnen we dus een inschatting maken van het sentiment van een Tweet.

# What to do

* Analyseer al de tweets in `trump.txt`.
* Hoeveel tweets zijn positief, hoeveel negatief?
* Welke positieve woorden gebruikt Trump het meest?
* Hoeveel dagen van het jaar tweet Trump overwegend positief?

## Om te beginnen
Bij deze opdracht leveren we code & data mee. Deze kun je [hier downloaden](https://github.com/Jelleas/tweets/archive/master.zip)

Je hebt bij deze opdracht drie data bestanden: `trump.txt`, `negative_words.txt` en `positive_words.txt`. In `trump.txt` vind je 997 tweets van Donald Trump. In `negative_words.txt` en `positive_words.txt` een collectie aan negatieve en positieve woorden in sociale media.

Wij hebben al wat stappen genomen zodat jij je geen zorgen hoeft te maken over hoe je deze bestanden inleest, en de data kan gebruiken in jouw programma. Werp allereerst een blik op `helpers.py`. Hier zijn 3 functies gedefineerd die het "echte" programma `tweet.py` helpen. Allereerst heb je `read_tweets()`, een functie die alle tweets inleest en een lijst van datums en een lijst van tweets (gesplit in woorden, ge-"tokenized") teruggeeft. Dan heb je de functie `read_words()`, een functie die alle positieve/negatieve woorden inleest en in een lijst teruggeeft. Tot slot de functie tokenize() die een tweet opsplit in woorden. Probeer goed te begrijpen wat de functies doen.

Dan heb je tot slot `tweet.py`, dat is het bestand waar jij in gaat programmeren. Hier vind je 3 functies, en 3 TODO's. Onderaan staat een stukje code dat de 3 functies aanroept met de tweets en lijsten van woorden. Om nou snel een beetje fingerspitzengefühl op te bouwen, kan je bijvoorbeeld even de waarden van `tweets` en `positive_words` tussentijds uitprinten.

## Positief en negatief
Om een inschatting te maken van het sentiment van een tweet kijken we naar het aantal positieve woorden en het aantal negatieve woorden in een tweet. Op basis hiervan kunnen we een sentiment score berekenen. Gebruik voor deze opdracht de volgende formule:

    sentiment_score = n_positives - n_negatives

Waar `n_positives` het aantal positieve woorden in de tweet is, en `n_negatives` het aantal negatieve woorden. Is de score kleiner dan 0, dan rekenen we de tweet als negatief, is de score groter dan 0, dan rekenen we de tweet als positief. Is de score precies 0, dan rekenen we de tweet als neutraal.

Maak de implementatie van `classify` in `tweet.py` af.

Dit is een deelopdracht waar je heel handig `set`s bij kan gebruiken. Je hebt namelijk straks de vraag, welke woorden zitten in zowel de tweet als in de positieve/negatieve woorden. Dat kan heel snel en makkelijk met `set`s!

> Let op! We nemen aan dat meerdere malen dezelfde woorden gebruiken in een tweet, geen effect heeft op de score.

> Mocht je de error krijgen: `no module named dateutil` voer dan deze regel uit in de terminal: `pip install python-dateutil`

## Wat zijn Trump's favoriete positieve woorden?
Behalve sentiment kunnen we ook kijken naar het woordgebruik in een tweet. Is "the border wall" nog steeds een onderwerp, en hoeveel fake news is er nou eigenlijk? Voor deze opdracht ga je onderzoeken wat Trump's favoriete positieve woorden zijn.

Maak de implementatie van `positive_word` in `tweet.py` af.

Dit is een deelopdracht waar je goed een `dict` bij kan gebruiken. Je moet straks gaan tellen hoe vaak een woord wordt gebruikt. Dat tellen kun je goed met een `dict`.

Daarnaast moet je straks de top 5 laten zien, je zult daarvoor moeten sorteren. Kijk eens goed naar de `sorted` functie in Python. Deze kun je aanroepen met een heel hoop optionele argumenten. Zo sorteer je bijvoorbeeld de keys van een dictionary op basis van de bijbehorende values:

    my_dict = {"foo" : 3, "bar" : 1, "baz" : 2}
    keys = my_dict.keys()
    sorted_keys = sorted(keys, key = lambda key : my_dict[key])
    print(sorted_keys)

Hier komt een nieuw concept voorbij: `lambda` functies. Dat zijn anonieme functies in Python (functies zonder naam) die 0 of meer argumenten accepteren, en de uitkomst van de functie is de statement na de `:`. Ofwel, de lambda functie `lambda key : my_dict[key]` is een functie die 1 argument accepteert en deze `key` noemt, de uitkomst (hetgeen wat ge-`return`ed wordt) is `my_dict[key]`. Ofwel de bijbehorende `value` uit `my_dict`.

Sommige functies in Python, zoals `sorted`, accepteren argumenten welke ook functies zijn. `sorted` accepteert een `key` argument, dat is een functie die moet teruggeven op basis waarvan gesorteerd wordt. Zo kan je een verzameling van elementen sorteren op basis van iets anders!

## Met het verkeerde been uit bed
Uitspraken van bekende personen hebben invloed op bijvoorbeeld de beursgang. Daarom ga jij onderzoeken op welke dagen van het jaar Trump overwegend negatief heeft getweet. Dat is, de dagen dat er meer negatieve tweets zijn gepost dan positieve.

Maak de implementatie van `bad_days` in `tweet.py` af.

Ook hier kun je handig gebruik maken van `set`s en `dict`s!

> Let op! We nemen aan dat meerdere malen dezelfde woorden gebruiken in een tweet, geen effect heeft op de score.

## Testen

check50 uva/progki/2018/tweet
