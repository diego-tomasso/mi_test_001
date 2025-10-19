import os
import platform


def limpiar_consola() -> None:
    """Limpia la consola basándose en el sistema operativo."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
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


def mostrar_jugadores(jugadores: list[str]) -> None:
    """Imprime la lista de jugadores agregando un indice.
    Al final también incluye un menú de opciones."""
    if len(jugadores) > 0:
        print("========================")
        for i in range(len(jugadores)):
            print(f"{i:02d} : {jugadores[i]}")
    print("========================")
    print("Menú: Jxx Jugador | Exx Entrenos | Pxx Partidos | Nxx Notas")
    print("Mxx Mejoras | Q salir")
    return
