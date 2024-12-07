class Rol:
    def __init__(self, id: int = None, nombre: str = ""):
        self._id = id
        self._nombre = nombre

    # Getters y setters
    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def set_id(self, id: int):
        self._id = id

    def set_nombre(self, nombre: str):
        self._nombre = nombre
