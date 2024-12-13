MENUS: dict = {
    "auth": {
        "1": "Iniciar sesión",
        "2": "Registrarse",
        "q": "Salir"
    },
    "admin": {
        "1": "Gestionar Destinos",
        "2": "Gestionar Paquetes Turísticos",
        "q": "Salir"
    },
    "admin.destinos": {
        "1": "Listar destinos",
        "2": "Crear destino",
        "3": "Actualizar destino",
        "4": "Eliminar destino",
        "q": "Salir"
    },
    "admin.destinos.actualizar": {
        "1": "Actualizar Destino",
        "2": "Actualizar Actividades",
        "q": "Salir"
    },
    "admin.destinos.actividades": {
        "1": "Agregar actividades",
        "2": "Eliminar actividad",
        "3": "Modificar actividad",
        "q": "Salir"
    },
    "admin.paquetes": {
        "1": "Listar paquetes",
        "2": "Crear paquete",
        "3": "Actualizar paquete",
        "4": "Eliminar paquete",
        "q": "Salir"
    },
    "admin.paquetes.actualizar": {
        "1": "Actualizar Paquete",
        "2": "Actualizar Destinos",
        "q": "Salir"
    },
    "admin.paquetes.destinos": {
        "1": "Agregar destino",
        "2": "Eliminar destino",
        "q": "Salir"
    },
    "admin.usuario": {
        "1": "Listar usuarios",
        "2": "Crear usuario",
        "3": "Actualizar usuario",
        "4": "Eliminar usuario",
        "q": "Salir"
    },
    "user": {
        "1": "Ver Paquetes Turísticos",
        "2": "Ver mis Reservas",
        "3": "Eliminar Reserva",
        "q": "Salir"
    },
    "user.paquetes": {
        "1": "Ver Todos los Paquetes Turísticos",
        "2": "Ver Paquete Turístico por rango de fechas",
        "3": "Reservar Paquete Turístico",
        "q": "Salir"
    }
}


def print_menu(menu: dict, title: str = "MENÚ"):
    print(f"{title:=^50}")
    print()
    for key, value in menu.items():
        print(f"{f"{str(key)}.":<3} {str(value):<30}")
    print()
    print("="*50)


def clear_screen():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def sleep(secs: int):
    import time
    time.sleep(secs)
