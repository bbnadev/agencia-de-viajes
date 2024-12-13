from database.database import Database
from models.Rol import Rol


class RolController:
    def __init__(self):
        self.db = Database()

    def listar(self) -> list[Rol]:
        query = "SELECT * FROM rol"
        try:
            roles = self.db.fetch(query)
            return [Rol(*rol) for rol in roles]
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar obtener los roles: {e}")
            return []

    def obtener_rol(self, id: int) -> Rol:
        query = "SELECT * FROM rol WHERE id = %s"
        try:
            rol = self.db.fetch_one(query, (id,))
            return Rol(*rol) if rol else None
        except Exception as e:
            print(
                f"(Controller) Ocurrio un error al intentar obtener el rol: {e}")
            return None
