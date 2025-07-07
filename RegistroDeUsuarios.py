# RegistroDeUsuarios.py
# Aquí se registran e inician sesión los usuarios con CIF numérico

import os
import getpass  # Para ocultar el CIF al escribirlo

ARCHIVO_USUARIOS = "usuarios.txt"  # Archivo donde guardamos los usuarios

# Función para registrar un nuevo usuario
def registrar_usuario():
    print("\n--- Registrar nuevo usuario ---")
    usuario = input("Ingresa tu nombre de usuario: ")

    while True:
        cif = getpass.getpass("Crea tu CIF (solo números): ")

        if cif.isdigit():
            break
        else:
            print(" El CIF debe contener solo números. Intenta otra vez.")

    # Verificar si el usuario ya existe
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            for linea in archivo:
                if linea.strip().split(",")[0].lower() == usuario.lower():
                    print(" Este usuario ya está registrado.")
                    return

    # Guardar nuevo usuario
    with open(ARCHIVO_USUARIOS, "a") as archivo:
        archivo.write(f"{usuario},{cif}\n")

    print(" Usuario registrado exitosamente.")

# Función para iniciar sesión
def iniciar_sesion():
    print("\n--- Inicio de sesión ---")
    usuario = input("Ingresa tu nombre de usuario: ")
    cif = getpass.getpass("Ingresa tu CIF: ")

    if not os.path.exists(ARCHIVO_USUARIOS):
        print(" No hay usuarios registrados.")
        return None

    with open(ARCHIVO_USUARIOS, "r") as archivo:
        for linea in archivo:
            usuario_guardado, cif_guardado = linea.strip().split(",")

            if usuario_guardado.lower() == usuario.lower() and cif_guardado == cif:
                print(f" Bienvenido/a {usuario_guardado}")
                return usuario_guardado

    print(" Usuario o CIF incorrectos.")
    return None
