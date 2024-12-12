from database.database import Database
from models.Usuario import Usuario
from bcrypt import checkpw, hashpw, gensalt


class UsuarioController:
    def __init__(self):
        self.db = Database()

    # AUTHENTICATION

    def autenticar(self, email: str, password: str):
        try:
            query = "SELECT * FROM Usuario WHERE email = %s"
            usuario = self.db.fetch_one(query, (email,))
            if usuario:
                return Usuario(*usuario) if checkpw(password.encode('utf-8'), usuario[4].encode('utf-8')) else False
            return False
        except Exception as err:
            print(
                f"(Controller) Ocurrio un error al intentar autenticar: {err}")
            return False

    def crear(self, usuario: Usuario):
        try:
            query = "INSERT INTO Usuario (nombre, apellido, email, password_hash) VALUES (%s, %s, %s, %s)"
            hashed_psswrd = hashpw(
                usuario.get_password_hash().encode('utf-8'), gensalt())
            self.db.query(query, (usuario.get_nombre(
            ), usuario.get_apellido(), usuario.get_email(), hashed_psswrd))
        except Exception as err:
            print(
                f"(Controller) Ocurrio un error al intentar crear el usuario: {err}")
            return False

    def listar_usuarios(self):
        query = "SELECT * FROM Usuario"
        try:
            usuarios = self.db.fetch(query)
            if usuarios:
                return [Usuario(*usuario) for usuario in usuarios]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    def obtener_usuario(self, column: str = "id", value: int | str = None):
        query = f"SELECT * FROM Usuario WHERE {column} = %s"
        try:
            usuario = self.db.fetch_one(query, (value,))
            if usuario:
                return Usuario(*usuario)
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def actualizar_usuario(self, usuario: Usuario):
        query = "UPDATE Usuario SET nombre = %s, apellido = %s, email = %s, password_hash = %s, rolId = %s WHERE id = %s"
        self.db.query(query, (usuario.get_nombre(), usuario.get_apellido(
        ), usuario.get_email(), usuario.get_password_hash(), usuario.get_rol(), usuario.get_id()))

    def eliminar_usuario(self, id: int):
        query = "DELETE FROM Usuario WHERE id = %s"
        self.db.query(query, (id,))
