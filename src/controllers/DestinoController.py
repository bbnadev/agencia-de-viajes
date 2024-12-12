from database.database import Database
from models.Destino import Destino
from models.Actividad import Actividad


class DestinoController:
    def __init__(self):
        self.db = Database()

    def obtener(self) -> list[Destino]:
        query = """SELECT
            d.id AS destino_id, d.nombre AS destino_nombre, d.descripcion as destino_descripcion, d.costo,
            a.id AS actividad_id, a.nombre AS actividad_nombre, a.descripcion AS actividad_descripcion
        FROM
            Destino d
        LEFT JOIN
            Actividad a ON d.id = a.destinoId;"""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            filas = cursor.fetchall()
            if not filas:
                return None
            destinos_dict = {}
            for fila in filas:
                destino_id = fila['destino_id']
                if destino_id not in destinos_dict:
                    destino = Destino(id=destino_id, nombre=fila['destino_nombre'],
                                      descripcion=fila['destino_descripcion'], costo=fila['costo'])
                    destinos_dict[destino_id] = destino
                if fila['actividad_id']:
                    actividad = Actividad(
                        fila['actividad_id'], fila['actividad_nombre'], fila['actividad_descripcion'])
                    destinos_dict[destino_id].add_actividad(actividad)
            cursor.close()
            conn.close()
            return list(destinos_dict.values())
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar listar los destinos: {e}")
            return []

    def crear(self, destino: Destino, actividades: list[Actividad]):
        query = "INSERT INTO Destino (nombre, descripcion, costo) VALUES (%s, %s, %s)"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (destino.get_nombre(),
                                   destino.get_descripcion(), destino.get_costo()))
            destinoId = cursor.lastrowid
            if actividades:
                for actividad in actividades:
                    query = "INSERT INTO Actividad (nombre, descripcion, destinoId) VALUES (%s, %s, %s)"
                    cursor.execute(query, (actividad.get_nombre(),
                                           actividad.get_descripcion(), destinoId))

            conn.commit()
            cursor.close()
            conn.close()

            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar crear el destino: {e}")
            return False

    def obtener_destino(self, column: str = "id", value: int | str = None) -> Destino:
        query = f"SELECT * FROM destino WHERE {column} = %s"
        try:
            destino = self.db.fetch_one(query, (value,))
            if destino:
                return Destino(*destino)
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def eliminar(self, id: int):
        query = "DELETE FROM Destino WHERE id = %s"
        try:
            self.db.query(query, (id,))
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar eliminar el destino: {e}")
            return False

    def actualizar(self, destino: Destino):
        query = "UPDATE Destino SET nombre = %s, descripcion = %s, costo = %s WHERE id = %s"
        try:
            self.db.query(query, (destino.get_nombre(),
                                  destino.get_descripcion(), destino.get_costo(), destino.get_id()))
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar actualizar el destino: {e}")
            return False
