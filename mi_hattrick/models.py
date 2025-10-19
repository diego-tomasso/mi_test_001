from enum import IntEnum
import json
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List, Dict, Any


# Definición de la entidad Jugador
@dataclass
class Jugador:
    """Modelo de datos de un jugador, con referencias a sus historiales."""

    playerid: str
    nombre: str
    fecha_nacimiento: date

    personalidad: str
    experiencia: int
    liderazgo: int
    lealtad: int
    llegada: date

    tsi: int
    sueldo: int
    especialidad: str
    forma: int
    condicion: int

    arquero: int
    defensa: int
    jugadas: int
    lateral: int
    asistencias: int
    anotacion: int
    parada: int
