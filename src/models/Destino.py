from models.Actividad import Actividad


class Destino:
    def __init__(self, id: int = None, nombre: str = "", descripcion: str = "", costo: float = 0.0):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._actividades = []
        self._costo = costo

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_costo(self) -> float:
        return self._costo

    def get_actividades(self) -> list:
        return self._actividades

    def set_id(self, id: int):
        self._id = id

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_descripcion(self, descripcion: str):
        self._descripcion = descripcion

    def set_costo(self, costo: float):
        self._costo = costo

    def add_actividad(self, actividad: Actividad):
        self._actividades.append(actividad)
