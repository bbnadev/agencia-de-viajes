from views.admin.AdmDestinosView import AdmDestinosView
from views.admin.AdmPaquetesView import AdmPaquetesView
from views.menus import MENUS, print_menu, clear_screen, sleep
from database.database import Database

from views.user.UserPaquetesView import UserPaquetesView
from views.user.UserReservasView import UserReservasView


def main():
    user = None
    while True:
        if user is None:
            from views.AuthView import AuthView
            authView = AuthView()
            print_menu(MENUS.get("auth"), 'MENÚ AUTENTICACIÓN')
            try:
                match input("> "):
                    case "1":
                        user = authView.autenticar()
                    case "2":
                        authView.registrar()
                    case "q":
                        clear_screen()
                        print("[*] Saliendo...")
                        break
                    case _:
                        clear_screen()
            except KeyboardInterrupt:
                clear_screen()
                print("[*] Saliendo...")
                break
        else:
            match user.get_rol():
                case 1:
                    print_menu(MENUS.get("admin"), 'MENÚ ADMINISTRADOR')
                    try:
                        match input("> "):
                            case "1":
                                admDestinosView = AdmDestinosView()
                                while True:
                                    print_menu(MENUS.get("admin.destinos"),
                                               'MENÚ DESTINOS')
                                    match input("> "):
                                        case "1":
                                            admDestinosView.listar()
                                        case "2":
                                            admDestinosView.crear()
                                        case "3":
                                            admDestinosView.actualizar()
                                        case "4":
                                            admDestinosView.eliminar()
                                        case "q":
                                            clear_screen()
                                            print(
                                                "[*] Volviendo al menú principal...")
                                            break
                                        case _:
                                            clear_screen()
                            case "2":
                                admPaquetesView = AdmPaquetesView()
                                while True:
                                    print_menu(MENUS.get("admin.paquetes"),
                                               'MENÚ PAQUETES TURÍSTICOS')
                                    match input("> "):
                                        case "1":
                                            admPaquetesView.listar()
                                        case "2":
                                            admPaquetesView.crear()
                                        case "3":
                                            admPaquetesView.actualizar()
                                        case "4":
                                            admPaquetesView.eliminar()
                                        case "q":
                                            clear_screen()
                                            print(
                                                "[*] Volviendo al menú principal...")
                                            break
                                        case _:
                                            clear_screen()
                            case "q":
                                clear_screen()
                                print("[*] Saliendo...")
                                break
                            case _:
                                clear_screen()
                    except Exception as err:
                        print(f'[!] Ocurrió un error: {err}')
                        continue
                    except KeyboardInterrupt:
                        clear_screen()
                        print("[*] Saliendo...")
                        break
                case 2:
                    print_menu(MENUS.get("user"), 'MENÚ CLIENTE')
                    try:
                        match input("> "):
                            case "1":
                                userPaquetesView = UserPaquetesView()
                                userReservasView = UserReservasView()
                                while True:
                                    print_menu(MENUS.get("user.paquetes"),
                                               'MENÚ PAQUETES TURÍSTICOS')
                                    match input("> "):
                                        case "1":
                                            userPaquetesView.listar()
                                        case "2":
                                            userPaquetesView.listar_por_fecha()
                                        case "3":
                                            userReservasView.reservar(
                                                user.get_id())
                                        case "q":
                                            clear_screen()
                                            print(
                                                "[*] Volviendo al menú principal...")
                                            break
                                        case _:
                                            clear_screen()
                            case "2":
                                userReservasView = UserReservasView()
                                userReservasView.listar(user.get_id())
                            case "3":
                                userReservasView = UserReservasView()
                                userReservasView.eliminar_reserva(
                                    user.get_id())
                            case "q":
                                clear_screen()
                                print("[*] Saliendo...")
                                break
                            case _:
                                clear_screen()
                    except Exception as err:
                        print(f'[!] Ocurrió un error: {err}')
                        continue
                    except KeyboardInterrupt:
                        clear_screen()
                        print("[*] Saliendo...")
                        break


if __name__ == "__main__":
    db = Database()
    db.checkDB()
    main()
