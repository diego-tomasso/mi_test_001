import pickle
from typing import BinaryIO
from usuario import Usuario


def guardar_usuarios(usuarios: list[Usuario], file_obj: BinaryIO) -> None:
    """
    Guarda una lista de objetos Usuario en un archivo binario (puede estar
    en memoria o en disco).
    """
    pickle.dump(usuarios, file_obj)


def leer_usuarios(file_obj: BinaryIO) -> list[Usuario]:
    """
    Lee una lista de objetos Usuario desde un archivo binario.
    """
    return pickle.load(file_obj)
