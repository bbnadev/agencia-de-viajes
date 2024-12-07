import datetime


class Usuario:
    def __init__(self, id: int = None, nombre: str = "", apellido: str = "", email: str = "", password_hash: str = "", rol: int = 2, fecha_creacion: datetime = datetime.datetime.now(), fecha_modificacion: datetime = None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._password_hash = password_hash
        self._rol = rol
        self._fecha_creacion = fecha_creacion
        self._fecha_modificacion = fecha_modificacion

    # Getters y setters

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_apellido(self) -> str:
        return self._apellido

    def get_nombreCompleto(self) -> str:
        return f"{self._nombre} {self._apellido}"

    def get_email(self) -> str:
        return self._email

    def get_password_hash(self) -> str:
        return self._password_hash

    def get_rol(self) -> int:
        return self._rol

    def get_fecha_creacion(self) -> datetime:
        return self._fecha_creacion

    def get_fecha_modificacion(self) -> datetime:
        return self._fecha_modificacion

    def set_id(self, id: int):
        self._id = id

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_apellido(self, apellido: str):
        self._apellido = apellido

    def set_email(self, email: str):
        self._email = email

    def set_password_hash(self, password_hash: str):
        self._password_hash = password_hash

    def set_rol(self, rol: int):
        self._rol = rol
