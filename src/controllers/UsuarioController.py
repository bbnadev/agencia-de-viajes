from database.database import Database
from models.Usuario import Usuario
import bcrypt


class UsuarioController:
    def __init__(self):
        self.db = Database()

    def autenticar_usuario(self, email: str, password: str):
        query = "SELECT password_hash FROM Usuario WHERE email = %s"
        usuario = self.db.fetch_one(query, (email,))
        if usuario:
            return bcrypt.checkpw(password.encode('utf-8'), usuario[0].encode('utf-8'))
        return False

    def listar_usuarios(self):
        query = "SELECT * FROM Usuario"
        try:
            usuarios = self.db.fetch(query)
            # return [Usuario(*usuario) for usuario in usuarios]
            return usuarios
        except Exception as e:
            print(e)
            return []

    def obtener_usuario(self, id: int):
        query = "SELECT * FROM Usuario WHERE id = %s"
        usuario = self.db.fetch_one(query, (id,))
        return Usuario(*usuario) if usuario else None

    def crear_usuario(self, usuario: Usuario):
        query = "INSERT INTO Usuario (nombre, apellido, email, password_hash, rolId) VALUES (%s, %s, %s, %s, %s)"
        self.db.query(query, (usuario.get_nombre(), usuario.get_apellido(
        ), usuario.get_email(), usuario.get_password_hash(), usuario.get_rol()))

    def actualizar_usuario(self, usuario: Usuario):
        query = "UPDATE Usuario SET nombre = %s, apellido = %s, email = %s, password_hash = %s, rolId = %s WHERE id = %s"
        self.db.query(query, (usuario.get_nombre(), usuario.get_apellido(
        ), usuario.get_email(), usuario.get_password_hash(), usuario.get_rol(), usuario.get_id()))

    def eliminar_usuario(self, id: int):
        query = "DELETE FROM Usuario WHERE id = %s"
        self.db.query(query, (id,))
