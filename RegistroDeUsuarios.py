# RegistroDeUsuarios.py
# Aquí se registran e inician sesión los usuarios con CIF (contraseña numérica oculta)

import os
import getpass  # Para ocultar la contraseña al escribirla

ARCHIVO_USUARIOS = "usuarios.txt"  # Archivo donde guardamos los usuarios

# Función para registrar un nuevo usuario
def registrar_usuario():
    print("\n--- Registrar nuevo usuario ---")
    cif = input("Ingresa tu CIF (solo números): ")
    nombre = input("Ingresa tu nombre completo: ")

    # Verificamos que el CIF solo tenga números
    if not cif.isdigit():
        print(" El CIF debe contener solo números.")
        return

    # Verificamos si el CIF ya existe
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            for linea in archivo:
                if linea.strip().split(",")[0] == cif:
                    print(" Este CIF ya está registrado.")
                    return

    # Guardamos el nuevo usuario en el archivo
    with open(ARCHIVO_USUARIOS, "a") as archivo:
        archivo.write(f"{cif},{nombre}\n")

    print(" Usuario registrado exitosamente.")

# Función para iniciar sesión
def iniciar_sesion():
    print("\n--- Inicio de sesión ---")
    nombre = input("Ingresa tu nombre completo: ")

    try:
        # getpass oculta lo que escribimos al ingresar la contraseña
        clave = getpass.getpass("Ingresa tu contraseña (CIF): ")

        # Validamos que el CIF sea numérico
        if not clave.isdigit():
            print(" El CIF debe contener solo números.")
            return None

        # Verificamos si hay archivo con usuarios
        if not os.path.exists(ARCHIVO_USUARIOS):
            print(" No hay usuarios registrados.")
            return None

        # Leemos todos los usuarios para buscar coincidencia
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            for linea in archivo:
                cif_guardado, nombre_guardado = linea.strip().split(",")

                # Comparamos nombre ignorando mayúsculas y comprobamos CIF
                if nombre_guardado.lower() == nombre.lower() and cif_guardado == clave:
                    print(f" Bienvenido/a {nombre_guardado}")
                    return nombre_guardado  # Retorna el nombre del usuario para usarlo en el sistema

        # Si no coincide, mostramos error
        print(" Nombre o contraseña incorrectos. Si no tienes cuenta, regístrate.")
        return None

    except Exception as e:
        # Capturamos cualquier error inesperado para evitar que se cierre el programa
        print(" Ocurrió un error al intentar iniciar sesión.")
        print(f"Detalles: {e}")
        return None

