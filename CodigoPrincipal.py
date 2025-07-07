# CodigoPrincipal.py
# Aquí se ejecuta todo el sistema

from RegistroDeUsuarios import iniciar_sesion, registrar_usuario
from ApartadoDelMenu import mostrar_menu
from RegistroDeAuditorias import agendar_tutoria, ver_tutorias, cargar_tutorias_desde_csv
from EliminarAuditorias import eliminar_tutoria  # Nuevo módulo para eliminar tutorías

# Mostrar bienvenida al sistema
print()
print("  BIENVENIDO AL SISTEMA DE TUTORÍAS ")
print()
print("Este sistema te permite:")
print("- Agendar tutorías académicas.")
print("- Ver las tutorías que ya tienes guardadas.")
print("- Controlar horarios y cupos.")
print()

# Pedir iniciar sesión o registrarse
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
            cargar_tutorias_desde_csv()  # Cargar tutorías guardadas
    elif opcion == "2":
        registrar_usuario()  # Registrar nuevo usuario
    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        exit()  # Salir del programa
    else:
        print(" Opción no válida. Intenta otra vez.")

# Menú principal, se repite hasta salir
while True:
    mostrar_menu()  # Mostrar menú
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agendar_tutoria(usuario_actual)  # Agendar tutoría
    elif opcion == "2":
        ver_tutorias()  # Ver tutorías guardadas
    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break  # Salir del programa
    elif opcion == "4":
        eliminar_tutoria()  # Eliminar tutoría
    else:
        print(" Opción no válida. Intenta otra vez.")

