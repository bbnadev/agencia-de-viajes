from datetime import datetime, date
from controllers.PaqueteTuristicoController import PaqueteTuristicoController, PaqueteTuristico, Destino, Actividad

from controllers.DestinoController import DestinoController
from views.menus import clear_screen, sleep, print_menu, MENUS
from views.admin.AdmDestinosView import AdmDestinosView
import locale
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')


class UserPaquetesView:
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
            if paquete.get_destinos():
                print("*"*30)
                print(f"{'Destinos':^30}")
                for destino in paquete.get_destinos():
                    print(f"{"":<3}> {'Destino:':<8} {destino.get_nombre()}")
                    print(f"{"":<3}> {'Costo:':<8} {locale.currency(
                        destino.get_costo(), grouping=True)}")
                print("*"*30)
            print(f"{'Costo Total':<13} {
                  locale.currency(self.controller.costo_total(paquete.get_id()), grouping=True)}")
            print("-"*50)

    def listar_por_fecha(self):
        while True:
            try:
                fechaMin = input(
                    "Fecha de inicio minima del paquete turístico (YYYY-MM-DD): ")

                fechaMin = datetime.strptime(
                    fechaMin, '%Y-%m-%d').date() if fechaMin else datetime.strptime(date.today().strftime("%Y-%m-%d"), '%Y-%m-%d').date()

            except ValueError as err:
                print(f'[!] debes introducir una fecha válida')
                continue

            if fechaMin < date.today():
                print(
                    "[!] La fecha de inicio minima no puede ser menor a la fecha actual")
                continue

            try:
                fechaMax = input(
                    "Fecha de inicio maxima del paquete turístico (YYYY-MM-DD): ")

                if not fechaMax:
                    print("[!] Debes ingresar una fecha de término")
                    continue

                fechaMax = datetime.strptime(
                    fechaMax, '%Y-%m-%d').date()
            except ValueError as err:
                print(f'[!] debes introducir una fecha válida')
                continue

            if fechaMax < fechaMin:
                print(
                    "[!] La fecha de inicio maxima no puede ser menor a la fecha de inicio minima")
                continue

            paquetes: list[PaqueteTuristico] = self.controller.obtener_paquetes_x_fechas(
                fechaMin, fechaMax)

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
                if paquete.get_destinos():
                    print("*"*30)
                    print(f"{'Destinos':^30}")
                    for destino in paquete.get_destinos():
                        print(f"{"":<3}> {'Destino:':<8} {
                              destino.get_nombre()}")
                        print(f"{"":<3}> {'Costo:':<8} {locale.currency(
                            destino.get_costo(), grouping=True)}")
                    print("*"*30)
                print(f"{'Costo Total':<13} {
                    locale.currency(self.controller.costo_total(paquete.get_id()), grouping=True)}")
                print("-"*50)
            return
