from database.database import Database
from models.Reserva import Reserva


class ReservaController:
    def __init__(self):
        self.db = Database()

    def listar(self, userId: int) -> list[Reserva]:
        query = "SELECT * FROM Reserva WHERE userId = %s"
        try:
            reservas = self.db.fetch(query, (userId,))
            return [Reserva(*reserva) for reserva in reservas]
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar obtener las reservas: {e}")
            return []

    def crear(self, reserva: Reserva):
        query = "INSERT INTO Reserva (userId, paqueteId) VALUES (%s, %s)"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(
                query, (reserva.get_userId(), reserva.get_paqueteId()))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar crear la reserva: {e}")
            return False

    def eliminar(self, userId: int, paqueteId: int):
        query = "DELETE FROM Reserva WHERE userId = %s AND paqueteId = %s"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (userId, paqueteId))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar eliminar la reserva: {e}")
            return False

    def existe_reserva(self, userId: int, paqueteId: int) -> bool:
        query = "SELECT * FROM Reserva WHERE userId = %s AND paqueteId = %s"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (userId, paqueteId))
            reserva = cursor.fetchone()
            cursor.close()
            conn.close()
            return True if reserva else False
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar verificar la existencia de la reserva: {e}")
            return False
