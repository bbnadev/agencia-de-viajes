from database.database import Database
from models.Actividad import Actividad


class ActividadController:
    def __init__(self):
        self.db = Database()

    def obtener_actividad(self, column: str = "id", value: int | str = None):
        query = f"SELECT * FROM actividad WHERE {column} = %s"
        try:
            actividad = self.db.fetch_one(query, (value,))
            if actividad:
                return Actividad(id=actividad[0], nombre=actividad[1], descripcion=actividad[2])
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def obtener(self, destinoId: int) -> list[Actividad]:
        query = "SELECT * FROM Actividad WHERE destinoId = %s"
        try:
            actividades = self.db.fetch(query, (destinoId,))
            if actividades:
                return [Actividad(id=actividad[0], nombre=actividad[1], descripcion=actividad[2]) for actividad in actividades]
            return None
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar listar las actividades: {e}")
            return None

    def crear(self, actividad: Actividad, destinoId: int):
        query = "INSERT INTO Actividad (nombre, descripcion, destinoId) VALUES (%s, %s, %s)"
        try:
            self.db.query(query, (actividad.get_nombre(),
                                  actividad.get_descripcion(), destinoId))
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar crear la actividad: {e}")
            return False

    def eliminar(self, id: int):
        query = "DELETE FROM Actividad WHERE id = %s"
        try:
            self.db.query(query, (id,))
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar eliminar la actividad: {e}")
            return False

    def actualizar(self, actividad: Actividad):
        query = "UPDATE Actividad SET nombre = %s, descripcion = %s WHERE id = %s"
        try:
            self.db.query(query, (actividad.get_nombre(),
                                  actividad.get_descripcion(), actividad.get_id()))
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar actualizar la actividad: {e}")
            return False
