from database.database import Database
from models.Actividad import Actividad
from models.PaqueteTuristico import PaqueteTuristico, Destino
from datetime import date


class PaqueteTuristicoController():
    def __init__(self):
        self.db = Database()

    def obtener_paquete(self, column: str = "id", value: int | str = None) -> Destino:
        query = f"SELECT * FROM PaqueteTuristico WHERE {column} = %s"
        try:
            paquete = self.db.fetch_one(query, (value,))
            return PaqueteTuristico(*paquete) if paquete else None
        except Exception as e:
            print(e)
            return None

    def obtener_paquetes(self) -> list[PaqueteTuristico]:
        query = """SELECT
                pt.id AS paquete_id, pt.nombre AS paquete_nombre, pt.fechaInicio, pt.fechaFin,
                d.id AS destino_id, d.nombre AS destino_nombre, d.descripcion AS destino_descripcion, d.costo
            FROM
                PaqueteTuristico pt
            LEFT JOIN
                PaqueteXDestino pxd ON pt.id = pxd.paqueteId
            LEFT JOIN
                Destino d ON pxd.destinoId = d.id
            ORDER BY paquete_id;"""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            filas = cursor.fetchall()
            if not filas:
                return None
            paquetes_dict = {}
            for fila in filas:
                paquete_id = fila['paquete_id']
                if paquete_id not in paquetes_dict:
                    paquete = PaqueteTuristico(id=paquete_id, nombre=fila['paquete_nombre'],
                                               fechaInicio=fila['fechaInicio'], fechaFin=fila['fechaFin'])
                    paquetes_dict[paquete_id] = paquete
                destino_id = fila['destino_id']
                if destino_id:
                    if destino_id not in paquetes_dict[paquete_id].get_destinos():
                        destino = Destino(id=destino_id, nombre=fila['destino_nombre'],
                                          descripcion=fila['destino_descripcion'], costo=fila['costo'])
                        paquetes_dict[paquete_id].add_destino(destino)

                # if fila['actividad_id']:
                #     actividad = Actividad(
                #         id=fila['actividad_id'], nombre=fila['actividad_nombre'], descripcion=fila['actividad_descripcion'])
                #     paquetes_dict[paquete_id].destinos[destino_id].add_actividad(
                #         actividad)
            cursor.close()
            conn.close()
            return list(paquetes_dict.values())
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar listar los paquetes y destinos: {e}")
            return []

    def costo_total(self, paquete_id: int) -> float:
        query = """ SELECT d.costo 
            FROM destino d 
        JOIN 
            PaqueteXDestino pxd ON d.id = pxd.destinoId
        WHERE 
            pxd.paqueteId = %s;"""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (paquete_id,))
            destinos = cursor.fetchall()
            if not destinos:
                return 0.0
            costo_total = sum(destino['costo'] for destino in destinos)
            return costo_total
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar obtener el costo: {e}")
            return 0.0

    def crear(self, paquete: PaqueteTuristico):
        query = "INSERT INTO PaqueteTuristico (nombre, fechaInicio, fechaFin) VALUES (%s, %s, %s)"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (paquete.get_nombre(),
                                   paquete.get_fechaInicio(), paquete.get_fechaFin()))
            paqueteId = cursor.lastrowid
            if paquete.get_destinos():
                for destino in paquete.get_destinos():
                    query = "INSERT INTO PaqueteXDestino (paqueteId, destinoId) VALUES (%s, %s)"
                    cursor.execute(query, (paqueteId, destino.get_id()))

            conn.commit()
            cursor.close()
            conn.close()

            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar crear el paquete: {e}")
            return False

    def eliminar(self, id: int):
        query = "DELETE FROM PaqueteTuristico WHERE id = %s"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar eliminar el paquete: {e}")
            return False

    def actualizar(self, paquete: PaqueteTuristico):
        query = "UPDATE PaqueteTuristico SET nombre = %s, fechaInicio = %s, fechaFin = %s WHERE id = %s"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (paquete.get_nombre(), paquete.get_fechaInicio(
            ), paquete.get_fechaFin(), paquete.get_id()))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar actualizar el paquete: {e}")
            return False

    def agregar_destino(self, paquete_id: int, destino_id: int):
        query = "INSERT INTO PaqueteXDestino (paqueteId, destinoId) VALUES (%s, %s)"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (paquete_id, destino_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar agregar el destino: {e}")
            return False

    def eliminar_destino(self, paquete_id: int, destino_id: int):
        query = "DELETE FROM PaqueteXDestino WHERE paqueteId = %s AND destinoId = %s"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (paquete_id, destino_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar eliminar el destino: {e}")
            return False

    def existe_paquete_destino(self, paquete_id: int, destino_id: int):
        query = "SELECT * FROM PaqueteXDestino WHERE paqueteId = %s AND destinoId = %s"
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, (paquete_id, destino_id))
            paquete = cursor.fetchone()
            cursor.close()
            conn.close()
            return True if paquete else False
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar verificar la existencia del paquete: {e}")
            return False

    def obtener_paquetes_x_fechas(self, fecha_rango_inicial: date, fecha_rango_fin: date) -> list[PaqueteTuristico]:
        query = """SELECT
                pt.id AS paquete_id, pt.nombre AS paquete_nombre, pt.fechaInicio, pt.fechaFin,
                d.id AS destino_id, d.nombre AS destino_nombre, d.descripcion AS destino_descripcion, d.costo
            FROM
                PaqueteTuristico pt
            LEFT JOIN
                PaqueteXDestino pxd ON pt.id = pxd.paqueteId
            LEFT JOIN
                Destino d ON pxd.destinoId = d.id
            WHERE
                pt.fechaInicio BETWEEN %s AND %s
            ORDER BY paquete_id;"""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (fecha_rango_inicial, fecha_rango_fin))
            filas = cursor.fetchall()
            if not filas:
                return None
            paquetes_dict = {}
            for fila in filas:
                paquete_id = fila['paquete_id']
                if paquete_id not in paquetes_dict:
                    paquete = PaqueteTuristico(id=paquete_id, nombre=fila['paquete_nombre'],
                                               fechaInicio=fila['fechaInicio'], fechaFin=fila['fechaFin'])
                    paquetes_dict[paquete_id] = paquete
                destino_id = fila['destino_id']
                if destino_id:
                    if destino_id not in paquetes_dict[paquete_id].get_destinos():
                        destino = Destino(id=destino_id, nombre=fila['destino_nombre'],
                                          descripcion=fila['destino_descripcion'], costo=fila['costo'])
                        paquetes_dict[paquete_id].add_destino(destino)

                # if fila['actividad_id']:
                #     actividad = Actividad(
                #         id=fila['actividad_id'], nombre=fila['actividad_nombre'], descripcion=fila['actividad_descripcion'])
                #     paquetes_dict[paquete_id].destinos[destino_id].add_actividad(
                #         actividad)
            cursor.close()
            conn.close()
            return list(paquetes_dict.values())
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar listar los paquetes y destinos por fecha: {e}")
            return []

    def obtener_paquete_x_id(self, paqueteId: int) -> PaqueteTuristico:
        query = """SELECT
                pt.id AS paquete_id, pt.nombre AS paquete_nombre, pt.fechaInicio, pt.fechaFin,
                d.id AS destino_id, d.nombre AS destino_nombre, d.descripcion AS destino_descripcion, d.costo
            FROM
                PaqueteTuristico pt
            LEFT JOIN
                PaqueteXDestino pxd ON pt.id = pxd.paqueteId
            LEFT JOIN
                Destino d ON pxd.destinoId = d.id
            WHERE pt.id = %s
            ORDER BY paquete_id;"""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (paqueteId,))
            filas = cursor.fetchall()
            if not filas:
                return None
            paquetes_dict = {}
            for fila in filas:
                paquete_id = fila['paquete_id']
                if paquete_id not in paquetes_dict:
                    paquete = PaqueteTuristico(id=paquete_id, nombre=fila['paquete_nombre'],
                                               fechaInicio=fila['fechaInicio'], fechaFin=fila['fechaFin'])
                    paquetes_dict[paquete_id] = paquete
                destino_id = fila['destino_id']
                if destino_id:
                    if destino_id not in paquetes_dict[paquete_id].get_destinos():
                        destino = Destino(id=destino_id, nombre=fila['destino_nombre'],
                                          descripcion=fila['destino_descripcion'], costo=fila['costo'])
                        paquetes_dict[paquete_id].add_destino(destino)

                # if fila['actividad_id']:
                #     actividad = Actividad(
                #         id=fila['actividad_id'], nombre=fila['actividad_nombre'], descripcion=fila['actividad_descripcion'])
                #     paquetes_dict[paquete_id].destinos[destino_id].add_actividad(
                #         actividad)
            cursor.close()
            conn.close()
            return list(paquetes_dict.values())
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar listar los paquetes y destinos: {e}")
            return []
