# CodigoPrincipal.py
# Aquí se ejecuta todo el sistema

from RegistroDeUsuarios import iniciar_sesion, registrar_usuario
from ApartadoDelMenu import mostrar_menu
from RegistroDeAuditorias import agendar_tutoria, ver_tutorias, cargar_tutorias_desde_csv

# Mostrar bienvenida al sistema
print()
print("  BIENVENIDO AL SISTEMA DE TUTORÍAS ")
print("------------------------------------")
print("Este sistema te permite:")
print("- Agendar tutorías académicas.")
print("- Ver las tutorías que ya tienes guardadas.")
print("- Controlar horarios y cupos.")
print("------------------------------------")

# Repetir hasta que el usuario inicie sesión correctamente o elija salir
usuario_actual = None
while not usuario_actual:
    print("\nPara continuar, rellena uno de los siguientes datos:")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        usuario_actual = iniciar_sesion()  # Llama a la función de inicio de sesión
        if usuario_actual:
            print(f"\nBienvenido/a al sistema, {usuario_actual}. ¡Puedes comenzar a usar el menú!")
            cargar_tutorias_desde_csv()  # Cargar tutorías si hay guardadas
    elif opcion == "2":
        registrar_usuario()  # Registra un nuevo usuario
    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        exit()  # El usuario decidió salir del sistema
    else:
        print(" Opción no válida. Intenta otra vez.")

# Menú principal del sistema (se repite hasta que el usuario decida salir)
while True:
    mostrar_menu()  # Mostrar las opciones del menú
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agendar_tutoria(usuario_actual)  # Agendar una nueva tutoría
    elif opcion == "2":
        ver_tutorias()  # Ver todas las tutorías guardadas
    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break  # Sale del bucle y termina el programa
    else:
        print(" Opción no válida. Intenta otra vez.")


