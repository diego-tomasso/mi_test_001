from pathlib import Path
import os  # Lo importo solo para hacer énfasis en que NO lo usaremos por ahora ;)

# 1. Definición de la ruta
# Usamos el objeto Path para representar la ruta de la nueva carpeta.
# Lo Pythonista: "Path" maneja las rutas de forma inteligente,
# usando el separador de carpetas correcto ("/" o "\")
# automáticamente según tu sistema operativo (Fedora en tu caso).
nombre_carpeta: str = "practica_pythonista"
ruta_a_crear: Path = Path(nombre_carpeta)

# 2. Creación de la carpeta
# Lo Pythonista: Usamos .mkdir() que es un método de nuestro objeto Path.
# El argumento "exist_ok=True" es la mejor práctica:
# - Si la carpeta YA existe, no lanza un errores
#   (ideal para scripts que se ejecutan varias veces.)
# - Si NO existe, la crea.
try:
    ruta_a_crear.mkdir(exist_ok=True)
    print(f"Carpeta '{nombre_carpeta}' creada con éxito o ya existía.")
except OSError as e:
    # Esto captura errores del sistema operativo (por ejemplo, falta de permisos)
    print(f"Error al crear la carpeta: {e}")

# 3. Confirmación de la ubicación (opcional pero útil)
# Imprimimos la ruta absoluta para que sepas exactamente dónde está.
# 'resolve()' transforma la ruta relativa en una absoluta, eliminando '.' o '..'.
print(f"Ubicación absoluta: {ruta_a_crear.resolve()}")
