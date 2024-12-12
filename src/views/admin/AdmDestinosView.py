from controllers.DestinoController import DestinoController, Destino, Actividad
from views.menus import clear_screen, sleep, print_menu, MENUS
from views.admin.AdmActividadView import AdmActividadView
import locale
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')


class AdmDestinosView():
    def __init__(self):
        self.controller = DestinoController()
        self.actView = AdmActividadView()

    def listar(self):
        destinos: list[Destino] = self.controller.obtener()
        print("-"*50)
        if not destinos:
            print("[!] No hay destinos registrados.")
            return
        for destino in destinos:
            print(f"{"ID:":<13} {destino.get_id()}")
            print(f"{"Destino:":<13} {destino.get_nombre()}")
            print(f"{"Descripción:":<13} {destino.get_descripcion()}")
            print(f"{"Costo:":<13} {locale.currency(
                destino.get_costo(), grouping=True)}")
            if destino.get_actividades():
                print(f"{'Actividades':*^50}")
                counter = 1
                for actividad in destino.get_actividades():
                    print(f"{counter} > {actividad.get_nombre()}: {
                        actividad.get_descripcion()}")
                    counter += 1
                print("-"*50)
            else:
                print(f"{'No cuenta con actividades':*^50}")
                print("-"*50)

    def crear(self):
        while True:
            nombre = input("Nombre del destino: ")
            if len(nombre) < 1 or len(nombre) > 50:
                print("[!] El nombre debe estar entre 1 y 50 caracteres")
                continue

            descripcion = input("Descripción del destino: ")

            try:
                costo = input("Costo del destino: ")
                if len(costo) < 1:
                    print("[!] El costo no puede estar vacío")
                    continue
                costo = float(costo)
                if costo < 0:
                    print("[!] El costo no puede ser negativo")
                    continue
            except ValueError as err:
                print(f'[!] debes introducir un número')
                continue

            destino = Destino(
                nombre=nombre, descripcion=descripcion, costo=costo)

            continuar = input("¿Quieres agregar actividades? (s/n): ").lower()
            while continuar == 's':
                nombre_actividad = input("Nombre actividad: ")
                if len(nombre_actividad) < 1 or len(nombre_actividad) > 50:
                    print(
                        "[!] El nombre de la actividad debe estar entre 1 y 50 caracteres")
                    continue
                descripcion_actividad = input("Descripción de la actividad: ")
                actividad = Actividad(
                    nombre=nombre_actividad, descripcion=descripcion_actividad)
                destino.add_actividad(actividad)

                continuar = input(
                    "¿Quieres agregar otra actividad? (s/n): ").lower()
                if continuar != 's':
                    break

            if self.controller.crear(destino, destino.get_actividades()):
                print("[*] Destino creado exitosamente.")
                return True
            else:
                print("[!] Ocurrió un error al intentar crear el destino.")
                return False

    def actualizar(self):
        while True:
            print_menu(MENUS.get('admin.destinos.actualizar'),
                       "ACTUALIZAR DESTINO")
            match input("> "):
                case "1":
                    while True:
                        id = input("ID del destino a actualizar: ")
                        if not id:
                            print("[!] Debes ingresar un ID")
                            continue
                        try:
                            id = int(id)
                        except ValueError as err:
                            print("[!] El ID debe ser un número")
                            continue

                        destino = self.controller.obtener_destino(value=id)
                        if not destino:
                            print("[!] No se encontró el destino.")
                            break

                        nombre = input(
                            f"Nombre del destino ({destino.get_nombre()}): ")
                        nombre = nombre if nombre else destino.get_nombre()

                        descripcion = input(f"Descripción del destino: ")
                        descripcion = descripcion if descripcion else destino.get_descripcion()

                        costo = input(
                            f"Costo del destino ({locale.currency(destino.get_costo(), grouping=True)}): ")
                        try:
                            costo = float(
                                costo) if costo else destino.get_costo()
                        except ValueError as err:
                            print(f'[!] debes introducir un número')
                            continue

                        destino.set_nombre(nombre)
                        destino.set_descripcion(descripcion)
                        destino.set_costo(costo)

                        if self.controller.actualizar(destino):
                            print("[*] Destino actualizado exitosamente.")
                            return True
                        else:
                            print(
                                "[!] Ocurrió un error al intentar actualizar el destino.")
                case "2":
                    while True:
                        id = input("ID del destino a actualizar: ")
                        if not id:
                            print("[!] Debes ingresar un ID")
                            continue
                        try:
                            id = int(id)
                        except ValueError as err:
                            print("[!] El ID debe ser un número")
                            continue

                        destino = self.controller.obtener_destino(value=id)
                        if not destino:
                            print("[!] No se encontró el destino.")
                            break

                        self.actView.listar(destino.get_id())
                        print_menu(MENUS.get('admin.destinos.actividades'),
                                   f'ACTIVIDADES \"{destino.get_nombre()}\"')
                        match input("> "):
                            case "1":
                                return self.actView.crear(destino.get_id())
                            case "2":
                                return self.actView.eliminar()
                            case "3":
                                return self.actView.actualizar()
                            case "q":
                                break
                case "q":
                    clear_screen()
                    print(
                        "[*] Volviendo al menú...")
                    break

    def eliminar(self):
        while True:
            id = input("ID del destino a eliminar: ")
            if not id:
                print("[!] Debes ingresar un ID")
                continue
            try:
                id = int(id)
            except ValueError as err:
                print("[!] El ID debe ser un número")
                continue

            if self.controller.obtener_destino(value=id):
                if self.controller.eliminar(id):
                    print("[*] Destino eliminado exitosamente.")
                    return True
                else:
                    print("[!] Ocurrió un error al intentar eliminar el destino.")
                    return False
            else:
                print("[!] No se encontró el destino.")
                break
