import os
import platform
import json
import persistencia


def limpiar_consola() -> None:
    """Limpia la consola basándose en el sistema operativo."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    return


def mostrar_jugadores(jugadores: list[str]) -> None:
    """Imprime la lista de jugadores agregando un indice.
    Al final también incluye un menú de opciones."""
    if len(jugadores) > 0:
        print("========================")
        for i in range(len(jugadores)):
            print(f"{i:02d} : {jugadores[i]}")
    print("========================")
    print("Menú: Jxx Jugador | Exx Entrenos | Pxx Partidos | Nxx Notas")
    print("Mxx Mejoras | CJ Crear Jugador | Q salir")
    return


def crear_jugador() -> dict[str, str | int]:
    """Permite al usuario crear un jugador nuevo."""
    jugador: dict[str, str | int] = {}

    try:
        nombre: str = input("nombre: ")
        player_id: str = input("player_id: ")
        personalidad: str = input("personalidad: ")
        experiencia: int = int(input("experiencia: "))
        liderazgo: int = int(input("liderazgo: "))
        lealtad: int = int(input("lealtad: "))
        tsi: int = int(input("tsi: "))
        sueldo: int = int(input("sueldo: "))
        especialidad: str = input("especialidad: ")
        forma: int = int(input("forma: "))
        condicion: int = int(input("condicion: "))
        arquero: int = int(input("arquero: "))
        defensa: int = int(input("defensa: "))
        jugadas: int = int(input("jugadas: "))
        lateral: int = int(input("lateral: "))
        asistencias: int = int(input("asistencias: "))
        anotacion: int = int(input("anotacion: "))
        parada: int = int(input("parada: "))
    except ValueError:
        print("Formato ingresado incorrecto. Deberá empezar nuevamente.")
        return jugador

    print("\n")
    confirmacion: str = input("Datos correctos? [Ss|Nn] ")
    if confirmacion[0].upper() == "N":
        return jugador

    jugador["nombre"] = nombre
    jugador["player_id"] = player_id
    jugador["personalidad"] = personalidad
    jugador["experiencia"] = experiencia
    jugador["liderazgo"] = liderazgo
    jugador["lealtad"] = lealtad
    jugador["tsi"] = tsi
    jugador["sueldo"] = sueldo
    jugador["especialidad"] = especialidad
    jugador["forma"] = forma
    jugador["condicion"] = condicion
    jugador["arquero"] = arquero
    jugador["defensa"] = defensa
    jugador["jugadas"] = jugadas
    jugador["lateral"] = lateral
    jugador["asistencias"] = asistencias
    jugador["anotacion"] = anotacion
    jugador["parada"] = parada
    return jugador


def main() -> None:
    while True:
        limpiar_consola()
        jugadores = persistencia.cargar_jugadores()
        mostrar_jugadores(jugadores)
        opcion: str = input("> ")
        if opcion[0].upper() == "Q":
            break
        if opcion[0:2].upper() == "CJ":
            jugador = crear_jugador()
            persistencia.guardar_jugador(jugador)
    return


if __name__ == "__main__":
    main()
