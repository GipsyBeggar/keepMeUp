# wg-gesucht.de KeepMeUp

Das Tool ändert das Inserat leicht ab (Zeitstempel im Freitext-Bereich "Sonstiges"), um in der Suche immer wieder oben zu stehen.


## Setup

1) `config.json` in einem Text-Editor öffnen und folgende Daten eintragen:
    - "mail": E-Mail-Adresse deines Accounts
    - "passwort": Passwort deines Accounts
    - "offerId": 7-stellige Inserats-Nummer, bspw. zu finden am Ende der Inserats-URL ("...&offer_id=**1234567**")
    - "intervall": Update-Intervall IN SEKUNDEN!

2) [Python3](https://realpython.com/installing-python/) und die [Packages](https://packaging.python.org/tutorials/installing-packages/) aus `req.txt` installieren
3) Ausführen! Bspw. via Terminal mit `cd` zum Zielordner navigieren und mit `python3 run.py` das Programm starten

## Anmerkungen
Intervall ist in Sekunden! Empfehlung: 18000 Sekunden (Aktualisierung alle 6 Stunden)

**Use at your own risk!**
