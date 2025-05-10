# Mastermind

Una versión interactiva del clásico juego Mastermind, desarrollada en Python con `tkinter`.

## Características

- Interfaz gráfica sencilla y funcional.
- Selección de colores mediante paleta.
- Validación de intentos con pistas visuales 2x2.
- Finalización automática al adivinar la combinación correcta.

## Requisitos

- Python 3 (recomendado Python 3.10 o superior).
- Módulo `tkinter` instalado (incluido en la mayoría de distribuciones de Python, pero puede requerir instalación manual).

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/andresgomez31/mastermind
    cd mastermind
    ```

2. Ejecuta el programa:

    ```bash
    python3 gui.py
    ```

## Solución de errores comunes

### Error: `ModuleNotFoundError: No module named '_tkinter'`

Si al ejecutar `gui.py` aparece este error, sigue las instrucciones según tu sistema operativo:

- **macOS (Homebrew):**

  ```bash
  brew install python-tk
  ```

- **Ubuntu/Debian:**

  ```bash
  sudo apt-get install python3-tk
  ```

- **Arch Linux:**

  ```bash
  sudo pacman -S tk
  ```

- **Windows:**

  Asegúrate de haber descargado Python desde [python.org](https://www.python.org) y activado la opción "tcl/tk and IDLE" durante la instalación.  
  