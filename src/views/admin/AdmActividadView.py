# from controllers.UsuarioController import UsuarioController, Usuario
from controllers.ActividadController import ActividadController, Actividad
from views.menus import clear_screen, sleep


class AdmActividadView:
    def __init__(self):
        self.controller = ActividadController()

    def listar(self, destinoId: int):
        actividades: list[Actividad] = self.controller.obtener(destinoId)
        if actividades:
            print("-"*50)
            print(f"{'ID':<5} {'Nombre':<20}")
            print("-"*50)
            for actividad in actividades:
                print(
                    f"{actividad.get_id():<5} {actividad.get_nombre():<20}")
            print("-"*50)
        else:
            print("[!] No hay actividades registradas.")

    def crear(self, destinoId: int):
        while True:
            nombre = input("Nombre de la actividad: ")
            if len(nombre) < 1 or len(nombre) > 50:
                print("[!] El nombre debe estar entre 1 y 50 caracteres")
                continue
            descripcion = input("Descripción de la actividad: ")
            actividad = Actividad(nombre=nombre, descripcion=descripcion)
            if self.controller.crear(actividad, destinoId):
                print("[*] Actividad creada exitosamente.")
                return True
            else:
                print("[!] Ocurrió un error al intentar crear la actividad.")
                return False

    def eliminar(self):
        while True:
            id = input("ID de la actividad a eliminar: ")
            if not id:
                print("[!] Debes ingresar un ID")
                continue
            try:
                id = int(id)
            except ValueError as err:
                print("[!] El ID debe ser un número")
                continue
            if self.controller.obtener_actividad(value=id):
                if self.controller.eliminar(id):
                    print("[*] Actividad eliminada exitosamente.")
                    return True
                else:
                    print("[!] Ocurrió un error al intentar eliminar la actividad.")
                    return False
            else:
                print("[!] No se encontró la actividad.")
                break

    def actualizar(self):
        while True:
            id = input("ID de la actividad a actualizar: ")
            if not id:
                print("[!] Debes ingresar un ID")
                continue
            try:
                id = int(id)
            except ValueError as err:
                print("[!] El ID debe ser un número")
                continue
            actividad = self.controller.obtener_actividad(value=id)
            if actividad:
                nombre = input(f"Nombre de la actividad ({
                               actividad.get_nombre()}): ")
                nombre = nombre if nombre else actividad.get_nombre()

                descripcion = input("Nueva descripción de la actividad: ")
                descripcion = descripcion if descripcion else actividad.get_descripcion()
                actividad.set_nombre(nombre)
                actividad.set_descripcion(descripcion)
                if self.controller.actualizar(actividad):
                    print("[*] Actividad actualizada exitosamente.")
                    return True
                else:
                    print(
                        "[!] Ocurrió un error al intentar actualizar la actividad.")
                    return False
            else:
                print("[!] No se encontró la actividad.")
                break
