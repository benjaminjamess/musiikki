# Musiikkisuositussovellus

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen musiikkisuosituksia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään musiikkisuosituksia.
* Käyttäjä näkee sovellukseen lisätyt musiikkisuosituksia. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät musiikkisuosituksia.
* Käyttäjä pystyy etsimään musiikkisuosituksia hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä musiikkisuosituksia.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät musiikkisuosituksia.
* Musiikkisuosituksille on valittavissa useampia luokitteluja. Valittavissa olevat luokittelut tulee määritellä tietokannassa. Käyttäjä voi käyttää luokituksia, kuten genre: pop, rock. Tai esimerkiksi tunne: surullinen, iloinen.
* Sovelluksessa on pääasiallisen tietokohteen (musiikkisuositksen) lisäksi toissijainen tietokohde, joka täydentää pääasiallista tietokohdetta. Tossijainen tietokohde on kommentti.


## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
