class Actividad:
    def __init__(self, id: int = None, nombre: str = "", descripcion: str = ""):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_id(self, id: int):
        self._id = id

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_descripcion(self, descripcion: str):
        self._descripcion = descripcion
