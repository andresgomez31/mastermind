# Mastermind

Una versión interactiva del clásico juego Mastermind, desarrollada en Python con `tkinter`.

## Características

- Interfaz gráfica sencilla y funcional.
- Selección de colores mediante paleta.
- Validación de intentos con pistas visuales 2x2.
- Finalización automática al adivinar la combinación correcta.

## Requisitos

- Python 3 (recomendado Python 3.10 o superior)
- Módulo `tkinter` instalado (incluido en la mayoría de distribuciones de Python, pero puede requerir instalación manual)

## Instalación

```bash
git clone https://github.com/andresgomez31/mastermind
cd mastermind
python3 gui.py
Solución de errores comunes
Si al ejecutar gui.py aparece el siguiente error:

vbnet
Copiar
Editar
Traceback (most recent call last):
  File "/Users/andresgomez/git/mastermind/gui.py", line 1, in <module>
    import tkinter as tk
  ...
ModuleNotFoundError: No module named '_tkinter'
En macOS (Homebrew):
bash
Copiar
Editar
brew install python-tk
En Ubuntu/Debian:
bash
Copiar
Editar
sudo apt-get install python3-tk
En Arch Linux:
bash
Copiar
Editar
sudo pacman -S tk
En Windows:
Asegúrate de haber descargado Python desde python.org y activado la opción "tcl/tk and IDLE" durante la instalación.