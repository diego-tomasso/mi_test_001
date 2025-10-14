#!/usr/bin/python
from pathlib import Path
import sys

# Procesar argumentos de línea de comandos
# sys.argv es una lista (list[str]) que contiene todos los argumentos.
# sys.argv[0] es siempre el nombre del script.
# sys.argv[1] es el primer argumento que pasa el usuario.
argumentos: list[str] = sys.argv

# Verificación de argumento.
# Si la lista solo tiene 1 elemento, significa que solo está el nombre del script.
if len(argumentos) < 2:
    # Lo Pythonista: Usar sys.exit() para salir de forma limpia y
    # devolver un código de error (1 en este caso) al os.
    print("<!> Error de uso: python script.py <nombre_carpeta>")
    sys.exit(1)

# El nombre de la carpeta es el primer argumento después del nombre del script.
nombre_carpeta: str = argumentos[1]
ruta_a_crear: Path = Path(nombre_carpeta)

# 2. Creación de la carpeta
try:
    # exist_ok=True evita el error si la carpeta ya existe
    ruta_a_crear.mkdir(exist_ok=True)
except OSError as e:
    # Capturamos errores de permisos o del sistema de archivos.
    print(f"Error al crear la carpeta: {e}")
    sys.exit(1)
