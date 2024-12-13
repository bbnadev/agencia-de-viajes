from datetime import datetime, date
from controllers.PaqueteTuristicoController import PaqueteTuristicoController, PaqueteTuristico, Destino, Actividad

from controllers.DestinoController import DestinoController
from views.menus import clear_screen, sleep, print_menu, MENUS
from views.admin.AdmDestinosView import AdmDestinosView
import locale
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')


class AdmPaquetesView:
    def __init__(self):
        self.controller = PaqueteTuristicoController()
        self.destinoController = DestinoController()
        self.destinoView = AdmDestinosView()

    def listar(self):
        paquetes: list[PaqueteTuristico] = self.controller.obtener_paquetes()
        print("-"*50)
        if not paquetes:
            print("[!] No hay paquetes turísticos registrados.")
            return
        for paquete in paquetes:
            if paquete.get_fechaInicio() < date.today():
                continue

            print(f"{'ID:':<13} {paquete.get_id()}")
            print(f"{'Paquete:':<13} {paquete.get_nombre()}")
            print(f"{'Fecha Inicio:':<13} {paquete.get_fechaInicio()}")
            print(f"{'Fecha Fin:':<13} {paquete.get_fechaFin()}")
            print(f"{'Destinos':<13} {len(paquete.get_destinos())}")
            print(f"{'Costo Total':<13} {
                  locale.currency(self.controller.costo_total(paquete.get_id()), grouping=True)}")
            print("-"*50)

    def crear(self):
        while True:
            nombre = input("Nombre del paquete turístico: ")
            if len(nombre) < 1 or len(nombre) > 50:
                print("[!] El nombre debe estar entre 1 y 50 caracteres")
                continue

            try:
                fechaInicio = input(
                    "Fecha de inicio del paquete turístico (YYYY-MM-DD): ")

                fechaInicio = datetime.strptime(
                    fechaInicio, '%Y-%m-%d').date() if fechaInicio else datetime.strptime(date.today().strftime("%Y-%m-%d"), '%Y-%m-%d').date()

            except ValueError as err:
                print(f'[!] debes introducir una fecha válida')
                continue

            if fechaInicio < date.today():
                print(
                    "[!] La fecha de inicio no puede ser menor a la fecha actual")
                continue

            try:
                fechaFin = input(
                    "Fecha de término del paquete turístico (YYYY-MM-DD): ")

                if not fechaFin:
                    print("[!] Debes ingresar una fecha de término")
                    continue

                fechaFin = datetime.strptime(
                    fechaFin, '%Y-%m-%d').date()
            except ValueError as err:
                print(f'[!] debes introducir una fecha válida')
                continue

            if fechaFin < fechaInicio:
                print(
                    "[!] La fecha de término no puede ser menor a la fecha de inicio")
                continue

            self.destinoView.listar()

            paquete = PaqueteTuristico(
                nombre=nombre, fechaInicio=fechaInicio, fechaFin=fechaFin)

            destinos = input(
                "Ingrese los ID de los destinos separados por coma: ").replace(" ", "").split(",")
            try:
                destinos = [int(destino) for destino in destinos]
            except ValueError as err:
                print(f'[!] debes introducir un número')
                continue

            for destino in destinos:
                if not self.destinoController.obtener_destino("id", destino):
                    print(f"[!] No se encontró un destino con el ID {destino}")

                paquete.add_destino(
                    self.destinoController.obtener_destino("id", destino))

            if self.controller.crear(paquete):
                print("[+] Paquete turístico creado exitosamente")
                return True
            else:
                print("[!] Ocurrió un error al intentar crear el paquete")
                return False

    def eliminar(self):
        while True:
            try:
                id = int(input("ID del paquete turístico a eliminar: "))
            except ValueError as err:
                print(f'[!] debes introducir un número')
                continue

            if not self.controller.obtener_paquete(id=id):
                print(f"[!] No se encontró un paquete con el ID {id}")
                continue

            if self.controller.eliminar(id):
                print("[+] Paquete turístico eliminado exitosamente")
                return True
            else:
                print("[!] Ocurrió un error al intentar eliminar el paquete")
                return False

    def actualizar(self):
        while True:
            print_menu(MENUS.get('admin.paquetes.actualizar'),
                       "ACTUALIZAR PAQUETE TURÍSTICO")
            match input("> "):
                case "1":
                    while True:
                        id = input("ID del paquete turístico a modificar: ")
                        if not id:
                            print("[!] Debes ingresar un ID")
                            continue
                        try:
                            id = int(id)
                        except ValueError as err:
                            print("[!] El ID debe ser un número")
                            continue

                        paquete: PaqueteTuristico = self.controller.obtener_paquete(
                            value=id)
                        if not paquete:
                            print(
                                f"[!] No se encontró un paquete")
                            continue

                        nombre = input(
                            f"Nombre del paquete turístico ({paquete.get_nombre()}): ")
                        nombre = paquete.set_nombre(
                            nombre) if nombre else paquete.get_nombre()

                        try:
                            fechaInicio = input(
                                f"Fecha de inicio del paquete turístico ({paquete.get_fechaInicio()}): ")

                            fechaInicio = datetime.strptime(
                                fechaInicio, '%Y-%m-%d').date() if fechaInicio else paquete.get_fechaInicio()

                        except ValueError as err:
                            print(f'[!] debes introducir una fecha válida')
                            continue

                        if fechaInicio < date.today():
                            print(
                                "[!] La fecha de inicio no puede ser menor a la fecha actual")
                            continue

                        paquete.set_fechaInicio(fechaInicio)

                        try:
                            fechaFin = input(
                                f"Fecha de término del paquete turístico ({paquete.get_fechaFin()}): ")

                            fechaFin = datetime.strptime(
                                fechaFin, '%Y-%m-%d').date() if fechaFin else paquete.get_fechaFin()

                        except ValueError as err:
                            print(f'[!] debes introducir una fecha válida')
                            continue

                        if fechaFin < fechaInicio:
                            print(
                                "[!] La fecha de término no puede ser menor a la fecha de inicio")
                            continue

                        paquete.set_fechaFin(fechaFin)

                        if self.controller.actualizar(paquete):
                            print(
                                "[*] Paquete turístico actualizado exitosamente.")
                            return True
                        else:
                            print(
                                "[!] Ocurrió un error al intentar actualizar el paquete.")

                case "2":
                    while True:
                        id = input("ID del paquete a actualizar: ")
                        if not id:
                            print("[!] Debes ingresar un ID")
                            continue
                        try:
                            id = int(id)
                        except ValueError as err:
                            print("[!] El ID debe ser un número")
                            continue

                        paquete = self.controller.obtener_paquete(value=id)
                        if not paquete:
                            print("[!] No se encontró el paquete.")
                            break

                        print_menu(MENUS.get('admin.paquetes.destinos'),
                                   f'destinos \"{paquete.get_nombre()}\"')
                        match input("> "):
                            case "1":
                                destinos = self.destinoController.obtener()
                                print(f"{'ID':<5} {'ACT':<6} {
                                      'Nombre':<20}")
                                print("-"*50)
                                for destino in destinos:
                                    if self.controller.existe_paquete_destino(paquete.get_id(), destino.get_id()):
                                        continue
                                    print(
                                        f"{destino.get_id():<5} {len(destino.get_actividades()):<6} {destino.get_nombre():<20}")
                                print("-"*50)

                                nuevo_destinos = input(
                                    "Ingrese los ID de los destinos separados por coma (q para salir): ").lower()
                                if nuevo_destinos == "q":
                                    break

                                nuevo_destinos = nuevo_destinos.replace(
                                    " ", "").split(",")

                                try:
                                    nuevo_destinos = [int(destino)
                                                      for destino in nuevo_destinos]
                                except ValueError as err:
                                    print(f'[!] debes introducir un número')
                                    continue
                                try:
                                    for n_destino in nuevo_destinos:
                                        if not self.destinoController.obtener_destino("id", n_destino):
                                            print(f"[!] No se encontró un destino con el ID {
                                                n_destino}")
                                            continue
                                        self.controller.agregar_destino(
                                            paquete.get_id(), n_destino)
                                    print(
                                        "[*] Destinos agregados exitosamente.")
                                    return True
                                except Exception as err:
                                    print(f'[!] Ocurrió un error: {err}')
                                    return False

                            case "2":
                                destinos = self.destinoController.obtener()
                                print(f"{'ID':<5} {'ACT':<6} {
                                      'Nombre':<20}")
                                print("-"*50)
                                for destino in destinos:
                                    if not self.controller.existe_paquete_destino(paquete.get_id(), destino.get_id()):
                                        continue
                                    print(
                                        f"{destino.get_id():<5} {len(destino.get_actividades()):<6} {destino.get_nombre():<20}")
                                print("-"*50)

                                eliminar_destinos = input(
                                    "Ingrese los ID de los destinos separados por coma (q para salir): ").lower()
                                if eliminar_destinos == "q":
                                    break

                                eliminar_destinos = eliminar_destinos.replace(
                                    " ", "").split(",")

                                try:
                                    eliminar_destinos = [
                                        int(destino) for destino in eliminar_destinos]
                                except ValueError as err:
                                    print(f'[!] debes introducir un número')
                                    continue
                                try:
                                    for el_destino in eliminar_destinos:
                                        if not self.destinoController.obtener_destino("id", el_destino):
                                            print(f"[!] No se encontró un destino con el ID {
                                                el_destino}")
                                            continue
                                        self.controller.eliminar_destino(
                                            paquete.get_id(), el_destino)
                                    print(
                                        "[*] Destinos eliminados exitosamente.")
                                    return True
                                except Exception as err:
                                    print(f'[!] Ocurrió un error: {err}')
                                    return False
                            case "q":
                                break
                case "q":
                    clear_screen()
                    print(
                        "[*] Volviendo al menú...")
                    break
