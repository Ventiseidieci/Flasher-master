# Flasher-master

la branch che funziona è: 'release'

## Nota Bene

Una volta flashato, va riavviato altrimenti non viene trovato con il filtro

## Descrizione

Flasher è un tool per gestire il flashing di firmware — basato su uno script Python e su componenti aggiuntivi inclusi nella repo.
Questa repo contiene vari script/utility (es. `cli.py`, `creatorEXEWin.py`, etc.) e file di packaging (spec per PyInstaller).
Lo scopo è fornire un modo semplice e replicabile di distribuire l’app come eseguibile standalone, senza che l’utente debba installare manualmente Python o le dipendenze.

## Struttura del progetto

Alcune delle principali cartelle/file nella branch `release`:

- `cli.py` — script principale da linea di comando.
- `creatorEXEWin.py`, `creatorAPPmacOS.py` — script ausiliari per la generazione di eseguibili su Windows/macOS.
- Vari file `.spec` (es. `cli.spec`, `Vbite_Flasher.spec`, `esptool.spec`, `nvs_gen.spec`) usati da PyInstaller per creare eseguibili.
- `esp_idf/`, `esp_idf_win/`, `Flasher/` — cartelle relative a componenti o librerie aggiuntive incluse (es. eventuali wrapper, script, risorse).

## Dipendenze

Poiché il progetto è in parte Python, potresti avere dipendenze esterne da includere nel packaging.
Per gestire le dipendenze Python, si consiglia di usare un ambiente virtuale e un file `requirements.txt` (o analoghi).
