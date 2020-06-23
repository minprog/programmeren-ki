# vigenere.py

In deze opdracht ga je de vigenere opdracht van CS50 maken in Python.

## Gebruik

	python vigenere.py
	usage: python vigenere.py keyword

	python vigenere.py bacon
	plaintext: Meet me at the park at eleven am
	ciphertext: Negh zf av huf pcfx bt gzrwep oz

## Specificatie

* Schrijf een programma genaamd `vigenere.py` dat je aanroept met een string command line argument, het keyword.
* Als het keyword niet gegeven wordt, of als er meerdere keys gegeven worden, dan moet het programma precies het volgende bericht printen: `usage: python vigenere.py keyword`
* Je mag aannemen dat de gebruiker een keyword intvoert bestaande enkel uit alfabetische karakters.
* De gebruiker mag een string invoeren wat ge-encrypt wordt met het keyword.
* De letter `a` representeerd een verschuiving van 0, de letter `b` van 1, enzovoort.
* Enkel letters moeten worden ge-encrypt, alle andere tekens blijven hetzelfde. Deze tekens tellen niet mee voor het encoderen. Dus met het keyword `"ab"` wordt `"c.d"` de string `"c.e"`
* Vergeet de loop around niet, dus de letter `z` met een key van `b` wordt de letter `a`.

## Tips

* In tegenstelling tot C zijn er in Python geen characters, maar enkel strings. Deze strings zijn meer dan een collectie van bytes, en je kan er dus niet meteen mee rekenen. Gelukkig heb je de functies `ord()` en `chr()` tot je beschikking. Zo is `ord("a")` 97, en `chr(97)` de string `"a"`, oftewel `chr(ord("a")) == "a"`.

## Testen

	check50 minprog/cs50x/2019/py/vigenere
