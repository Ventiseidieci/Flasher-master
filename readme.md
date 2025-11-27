# Vbite Flasher (Flasher-master)

Tool GUI/CLI in Python per eseguire il flashing di dispositivi ESP32 usando `esptool`.

## Installazione

### Windows

[windows release](https://github.com/Ventiseidieci/Flasher-master/releases/tag/v1.0.1)

### macOS

[macOS release](https://github.com/Ventiseidieci/Flasher-master/releases/tag/v1.0.1-macOS)

## Nota Bene

**Questo README fornisce**: come avviare il codice sorgente, architettura dei componenti, dipendenze principali e note per packaging.

Una volta flashato, vbite va riavviato altrimenti non viene trovato con il filtro del ble

## Prerequisiti

- **Python**: 3.10+ consigliato.
- **Dipendenze Python**: `PySide6`, `pyserial`.
- **Strumenti esterni**: i tool contenuti in `esp_idf/` o `esp_idf_win/` (es. `esptool`, `nvs_gen`) sono usati dalla app.

## Installazione rapida (consigliata)

1. Crea e attiva un ambiente virtuale:

     ```zsh
     python -m venv .venv
     source .venv/bin/activate
     ```

2. Installa le dipendenze minime:

     ```zsh
     pip install PySide6 pyserial
     ```

3. Avvia l'app GUI:

     ```zsh
     python cli.py
     # oppure
     python -m Flasher
     ```

## Struttura del progetto (sintesi)

- **`cli.py`**: entrypoint che avvia l'app.

- **`Flasher/__main__.py`**: crea `Model`, `Controller` e `View` (QML).
- **`Flasher/GUI/`**: interfaccia QML (`mainUI.qml`) e binding Python (`view.py`).
- **`Flasher/controller/`**: `controller.py` coordina Model ↔ Backend.
- **`Flasher/backend/`**: `model.py`, `backend.py`, driver seriali (`serialMACOS.py`, `serialWINDOWS.py`, `serialLINUX.py`) e generatori CSV/NVS.
- **`esp_idf/` e `esp_idf_win/`**: risorse e script usati per il flashing e la generazione NVS (inclusi nei pacchetti costruiti).

## Architettura e flusso (breve)

- **Pattern**: una semplice architettura tipo MVC/MVVM.
  - `Model` (`Flasher/backend/model.py`): mantiene stato minimale (es. `boardName`, `sku`, `data`) e fornisce il `Backend`.
  - `Controller` (`Flasher/controller/controller.py`): coordina le azioni; es. `getBoardList()`, `setBoard(board)`, `flash(choice)`.
  - `View` (`Flasher/GUI/view.py` + `Flasher/GUI/mainUI.qml`): QML per UI; espone oggetti Python al QML tramite `engine.rootContext().setContextProperty(...)`.

Esempio di flusso quando si preme `Flash`:

- La `ComboBox` QML imposta `comboBoxHandler.selectedItem`, che chiama `controller.setBoard(...)`.
- Il click sul pulsante chiama `flashButtonHandler.handleButtonClicked()` → `controller.flash(model.getBoardName())`.
- `Controller.flash` chiama `Backend.flashSku()` (genera NVS, assegna SKU) e poi `Backend.flashProgram(choice)` che restituisce una lista di comandi.
- `CommandRunner` (`view.py`) riceve la lista, costruisce comandi shell e li esegue uno per volta con `QProcess`, aggiornando la `TextArea` con l'output.

## Formato dei comandi

- `Backend.flashProgram(choice)` restituisce `List[List[str]]` (ogni inner-list è una lista di token/argomenti per il tool `esptool`).
- `CommandRunner.setCommands(...)` trasforma ogni inner-list in una stringa (`' '.join(...)`) e passa i comandi alla shell tramite `QProcess`.

## Eseguibili / Packaging

- La repo contiene i file  `creatorAPPmacOS.py` e `creatorEXEWin.py` per PyInstaller, servono a crerare i precompilati per fare le release.
- Quando l'app è impacchettata con PyInstaller, il codice rileva lo stato `frozen` e usa `sys._MEIPASS` per localizzare risorse incluse.

Non sono sicuro di questo:

- Se intendi creare un eseguibile, usa i `.spec` forniti o gli script helper al root.

## Note pratiche e suggerimenti

- Su macOS e Linux assicurati di avere i permessi per accedere alla porta seriale (potrebbe servire concedere permessi o usare sudo per testare).
- `serialInterface.setBoard(...)` apre la porta con `serial.Serial(board, 115200, timeout=5)`.
- `CommandRunner` usa la shell (`bash`/`cmd.exe`) per eseguire i comandi: questo semplifica l'uso degli strumenti ma implica escaping/shell quoting.
- Il metodo `flashNVS()` nei driver (`serialMACOS.py` / `serialWINDOWS.py`) esegue `nvs_gen` tramite `subprocess.run(...)` in modo sincrono (genera il file `.bin` prima dello step di flashing).
- Piccola incongruenza: `CommandRunner.setCommands` è decorata con `@Slot(str)` ma riceve una lista; funziona in pratica, ma si potrebbe aggiornare la firma (es. `@Slot('QVariant')`) per essere più corretti.

## Risoluzione problemi comuni

- Se la `ComboBox` non mostra porte: verifica che i dispositivi seriali siano collegati e riavviare il software.
- Una volta flashato, vbite va riavviato altrimenti non viene trovato con il filtro del ble
