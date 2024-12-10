MENUS: dict = {
    "auth": {
        "1": "Iniciar sesión",
        "2": "Registrarse",
        "q": "Salir"
    },
    "admin": {
        "1": "Gestionar Roles",
        "2": "Gestionar Destinos",
        "3": "Gestionar Paquetes Turísticos",
        "4": "Gestionar Actividades",
        "q": "Salir"
    },
    "admin.roles": {
        "1": "Listar roles",
        "2": "Crear rol",
        "3": "Actualizar rol",
        "4": "Eliminar rol",
        "q": "Salir"
    },
    "admin.destinos": {
        "1": "Listar destinos",
        "2": "Crear destino",
        "3": "Actualizar destino",
        "4": "Eliminar destino",
        "q": "Salir"
    },
    "admin.paquetes": {
        "1": "Listar paquetes",
        "2": "Crear paquete",
        "3": "Actualizar paquete",
        "4": "Eliminar paquete",
        "q": "Salir"
    },
    "admin.actividades": {
        "1": "Listar actividades",
        "2": "Crear actividad",
        "3": "Actualizar actividad",
        "4": "Eliminar actividad",
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
        "1": "Ver destinos",
        "2": "Ver paquetes turísticos",
        "3": "Ver actividades",
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
