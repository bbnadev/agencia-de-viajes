from datetime import datetime


class Reserva:
    def __init__(self, userId: int = None, paqueteId: int = None, fecha_creacion: datetime = None):
        self._userId = userId
        self._paqueteId = paqueteId
        self._fecha_creacion = fecha_creacion

    def get_userId(self) -> int:
        return self._userId

    def get_paqueteId(self) -> int:
        return self._paqueteId

    def get_fecha_creacion(self) -> datetime:
        return self._fecha_creacion
