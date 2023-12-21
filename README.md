Installation
---

---

### Start PineBoard

- Raspberry Pi via LAN-Kabel mit Internet verbinden
- Strom anschließen
- Lautsprecher via USB & AUX Kabel an Raspberry Pi anschließen

---

### Connect to PineBoard (Unix)

```
$ ssh user@soundpi.local
$ cd SoundBoard
```

---

### Create environment

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

---

### Start main program

`$ python3 SoundBoard.py`

Die Buttons 1-9 sind nun bereit gedrückt zu werden und spielen verschiedenste Sounds ab  :)

(Lautstärkewarnung hiermit gegeben)

Zum stoppen `CTRL + C`