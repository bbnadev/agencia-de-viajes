from controllers.ReservaController import ReservaController, Reserva
from controllers.PaqueteTuristicoController import PaqueteTuristicoController, PaqueteTuristico
from controllers.DestinoController import DestinoController
import locale
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')


class UserReservasView:
    def __init__(self):
        self.controller = ReservaController()
        self.paqueteController = PaqueteTuristicoController()

    def listar(self, userId: int):
        reservas = self.controller.listar(userId)
        if not reservas:
            print("[!] No tienes reservas registrados.")
            return
        print(f"{"RESERVAS":-^50}")
        for reserva in reservas:
            paquetes = self.paqueteController.obtener_paquete_x_id(
                reserva.get_paqueteId())
            for paquete in paquetes:
                print(f"{'ID:':<13} {paquete.get_id()}")
                print(f"{'Paquete:':<13} {paquete.get_nombre()}")
                print(f"{'Fecha Inicio:':<13} {paquete.get_fechaInicio()}")
                print(f"{'Fecha Fin:':<13} {paquete.get_fechaFin()}")
                print(f"{'Destinos':<13} {len(paquete.get_destinos())}")
                print(f"{'Costo Total':<13} {
                    locale.currency(self.paqueteController.costo_total(paquete.get_id()), grouping=True)}")
            print("-"*50)

    def reservar(self, userId: int):
        while True:
            paquetes = input(
                "Ingrese los ID de los Paquetes separados por coma: ").replace(" ", "").split(",")
            try:
                paquetes = [int(paquete) for paquete in paquetes]
            except ValueError as err:
                print(f'[!] debes introducir un número')
                continue
            try:
                for paquete in paquetes:
                    if not self.paqueteController.obtener_paquete(value=paquete):
                        print(f'[!] El paquete con ID {paquete} no existe')
                        continue

                    if self.controller.existe_reserva(userId, paquete):
                        print(
                            f'[!] Ya tienes reservado el paquete con ID {paquete}')
                        continue

                    self.controller.crear(Reserva(userId, paquete))
                print("[*] Reserva creada exitosamente.")
                return True
            except Exception as err:
                print(f'[!] Ocurrió un error: {err}')
                return False

    def eliminar_reserva(self, userId: int):
        while True:
            paquetes = input(
                "Ingrese los ID de las Reservas separados por coma: ").replace(" ", "").split(",")
            try:
                paquetes = [int(paquete) for paquete in paquetes]
            except ValueError as err:
                print(f'[!] debes introducir un número')
                continue
            try:
                for paquete in paquetes:
                    if not self.paqueteController.obtener_paquete(value=paquete):
                        print(f'[!] El paquete con ID {paquete} no existe')
                        continue

                    if not self.controller.existe_reserva(userId, paquete):
                        print(
                            f'[!] No tienes reservado el paquete con ID {paquete}')
                        continue

                    self.controller.eliminar(userId, paquete)
                print("[*] Reserva eliminada exitosamente.")
                return True
            except Exception as err:
                print(f'[!] Ocurrió un error: {err}')
                return False
