import json


def guardar_jugador(jugador: dict[str, str | int]) -> None:
    """Guarda un diccionario de datos de jugador en un archivo JSON."""
    if len(jugador) == 0 or jugador is None:
        return
    archivo_nombre: str = f"./data/jugadores/{jugador['player_id']}_datos.json"
    try:
        with open(archivo_nombre, "w", encoding="utf-8") as archivo:
            if agrega_jugador(jugador):
                json.dump(jugador, archivo, indent=4)
            else:
                print("\nUn jugador con este id ya existe.\n")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")
    return


def cargar_jugadores() -> list[str]:
    """Carga los jugadores guardados en el archivo jugadores.txt"""
    jugadores: list[str]
    try:
        with open("jugadores.txt", "r") as archivo:
            jugadores = archivo.readlines()
            for i in range(len(jugadores)):
                jugadores[i] = jugadores[i].strip()
    except FileNotFoundError:
        jugadores = []
    return jugadores


def cargar_jugador(player_id: str) -> dict[str, str | int]:
    """Carga los datos de un jugador desde un archivo JSON y devuelve un diccionario."""
    archivo_nombre: str = f"./data/jugadores/{player_id}_datos.json"
    jugador: dict[str, str | int] = {}
    try:
        with open(archivo_nombre, "r", encoding="utf-8") as archivo:
            jugador = json.load(archivo)
            return jugador
    except FileNotFoundError:
        print(f"<!> Archivo no encontrado para {player_id}.")
        return jugador
    except json.JSONDecodeError:
        print(f"<!> El archivo {archivo_nombre} no tiene formato JSON válido.")
        return jugador


def agrega_jugador(jugador: dict[str, str | int]) -> bool:
    """Agrega jugador a la lista de jugadores para el archivo jugadores.txt"""
    jugadores: list[str] = cargar_jugadores()
    respuesta: bool = True
    for linea in jugadores:
        if str(jugador["player_id"]) in linea:
            respuesta = False
            return respuesta
    jugadores.append(f"{jugador['nombre']} ({jugador['player_id']})")
    with open("jugadores.txt", "w") as archivo:
        for linea in jugadores:
            linea += "\n"
            archivo.write(linea)
    return respuesta
