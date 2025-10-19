import os
import platform


def limpiar_consola() -> None:
    """Limpia la consola basándose en el sistema operativo."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def cargar_tareas() -> list[str]:
    tareas: list[str]
    try:
        with open("tareas.txt", "r") as archivo:
            tareas = archivo.readlines()
            for i in range(len(tareas)):
                tareas[i] = tareas[i].strip()
    except FileNotFoundError:
        tareas = []
    return tareas


def guardar_tareas(tareas: list[str]) -> None:
    if len(tareas) == 0:
        return
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            tarea += "\n"
            archivo.write(tarea)


def mostrar_tareas(tareas: list[str]) -> None:
    if len(tareas) == 0:
        return
    index: int = 0
    for tarea in tareas:
        valor: str = ""
        valor += f"{index:02d} "
        if tarea[0] == "C":
            valor += "[X] "
        elif tarea[0] == "I":
            valor += "[ ] "
        valor += tarea[1:]
        index += 1
        print(valor)
    return


def mostrar_ayuda() -> None:
    print("\n")
    print("Formato: [comando]Tarea.")
    print("Comandos disponibles:")
    print("    H- Ayuda (imprime esta guía).")
    print("    Q- Salir.")
    print("    A- Agrega una tarea.")
    print("    B- Borra una tarea. Hay que indicar índice.")
    print("    C- Completa una tarea. Hay que indicar índice.")
    print("\n")
    input("Presione [enter] para seguir.")
    return


def borrar_tarea(texto: str, tareas: list[str]) -> None:
    indice: int
    try:
        indice = int(texto[1:3])
    except ValueError:
        print("El formato del índice es incorrecto.")
        input("Presione [enter] para seguir.")
        return
    if indice >= len(tareas) or indice < 0:
        return
    else:
        tarea = tareas.pop(indice)
        print(f"Eliminada: {tarea[1:]}.")
    return


def completa_tarea(texto: str, tareas: list[str]) -> None:
    indice: int
    try:
        indice = int(texto[1:3])
    except ValueError:
        print("El formato del índice es incorrecto.")
        input("Presione [enter] para seguir.")
        return
    if indice >= len(tareas) or indice < 0:
        return
    else:
        tareas[indice] = str("C" + tareas[indice][1:])
    return


def main() -> None:
    loop: bool = True
    tareas: list[str] = cargar_tareas()
    while loop:
        limpiar_consola()
        mostrar_tareas(tareas)
        texto = input("> ")
        if texto[0].upper() == "H":
            mostrar_ayuda()
        elif texto[0].upper() == "Q":
            loop = False
        elif texto[0].upper() == "A":
            print(str("I" + texto[1:]))
            tareas.append(str("I" + texto[1:]))
            print(tareas)
        elif texto[0].upper() == "B":
            borrar_tarea(texto, tareas)
        elif texto[0].upper() == "C":
            completa_tarea(texto, tareas)
    guardar_tareas(tareas)


if __name__ == "__main__":
    main()
