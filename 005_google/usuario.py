# Importamos el decorador "dataclass" desde el módulo "dataclasses"
from dataclasses import dataclass


# Usamos el decorador "@dataclass" para que Python genere automáticamente métodos útiles
# como __init__, __repr__, __eq__, etc. basados en los campos que definimos.
@dataclass
class Usuario:
    nombre: str  # nombre completo del usuario
    id: int  # un identificador único (ej: número de cliente)
    telefono: str  # teléfono en formato string (para mantener ceros y símbolos)
    mail: str  # dirección de correo electrónico
