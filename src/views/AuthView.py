from controllers.UsuarioController import UsuarioController, Usuario
from views.menus import clear_screen, sleep


class AuthView:
    def __init__(self):
        self.controller = UsuarioController()

    def autenticar(self):
        while True:
            try:

                email = input("Email: ").lower()
                if len(email) < 1 or len(email) > 50:
                    print("[!] El email debe estar entre 1 y 50 caracteres")
                    continue

                if not "@" in email or not "." in email:
                    print("[!] El Email no es válido")
                    continue

                password = input("Contraseña: ")
                if len(password) < 1 or len(password) > 255:
                    print("[!] La contraseña debe estar entre 1 y 255 caracteres")
                    continue

            except Exception as err:
                print(f'[!] {err}')
                break

            except KeyboardInterrupt:
                clear_screen()
                print("[*] Volviendo al menu principal.")
                sleep(1.5)
                break

            usuario = self.controller.autenticar(email, password)
            if usuario:
                print("[*] Inicio de sesión exitoso.")
                return usuario
            else:
                print("[!] Credenciales incorrectas.")
                continue

    def registrar(self):
        while True:
            try:
                nombre = input("Nombre: ")
                if len(nombre) < 1 or len(nombre) > 50:
                    print("[!] El nombre debe estar entre 1 y 50 caracteres")
                    continue

                apellido = input("Apellido: ")  # Puede ser null

                email = input("Email: ").lower()
                if len(email) < 1 or len(email) > 50:
                    print("[!] El email debe estar entre 1 y 50 caracteres")
                    continue

                if not "@" in email or not "." in email:
                    print("[!] El Email no es válido")
                    continue

                if self.controller.obtener_usuario("email", email):
                    print("[!] El Email ya está en uso")
                    continue

                password = input("Contraseña: ")
                if len(password) < 1 or len(password) > 255:
                    print("[!] La contraseña debe estar entre 1 y 255 caracteres")
                    continue

            except Exception as exc_error:
                print(f'[!] {exc_error}')
                break
            except KeyboardInterrupt:
                clear_screen()
                print("[*] Volviendo al menu principal.")
                sleep(1.5)
                break

            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password_hash=password
            )
            try:
                self.controller.crear(usuario)
                print("[+] Usuario creado exitosamente.")
                sleep(1.5)
                clear_screen()
                return
            except Exception as err:
                print(f'[!] {err}')
                break
