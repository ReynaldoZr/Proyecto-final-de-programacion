# RegistroDeAuditorias.py
# Funciones para agendar y ver tutorías

import os
import GuardadoDeAuditorias  # Guardar en archivo CSV

# Lista de materias disponibles
materias = ["matemáticas I", "programación I", "algoritmos I", "comunicación y lenguaje I", "cálculo I"]

# Horarios (dos por materia)
horarios = [
    ["Lunes 3pm", "Miércoles 3pm"],
    ["Martes 2pm", "Jueves 2pm"],
    ["Lunes 10am", "Miércoles 10am"],
    ["Martes 9am", "Jueves 9am"],
    ["Lunes 1pm", "Miércoles 1pm"]
]

# Cupos disponibles (3 por horario)
cupos_disponibles = [[3, 3] for _ in range(len(materias))]

# Lista de tutorías guardadas
tutorias_guardadas = []

# Cargar tutorías desde archivo CSV
def cargar_tutorias_desde_csv(nombre_archivo="tutorias.csv"):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            next(archivo)  # Saltar encabezado
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    tutorias_guardadas.append(datos)

        total = len(tutorias_guardadas)
        if total == 1:
            print(" Se cargó 1 tutoría anterior.\n")
        elif total > 1:
            print(f" Se cargaron {total} tutorías anteriores.\n")

# Agendar tutoría
def agendar_tutoria(nombre):
    print("\n--- Agendar nueva tutoría ---")

    # Mostrar materias
    print("\nElige una materia:")
    for i, materia in enumerate(materias, start=1):
        print(f"{i}. {materia}")

    try:
        opcion_materia = int(input("Número de materia: "))

        if 1 <= opcion_materia <= len(materias):
            materia_elegida = materias[opcion_materia - 1]

            # Mostrar horarios y cupos
            print(f"\nHorarios para {materia_elegida}:")
            for j in range(2):
                print(f"{j+1}. {horarios[opcion_materia - 1][j]} (Cupos: {cupos_disponibles[opcion_materia - 1][j]})")

            opcion_horario = int(input("Elige horario (1 o 2): "))

            if 1 <= opcion_horario <= 2:
                if cupos_disponibles[opcion_materia - 1][opcion_horario - 1] > 0:
                    horario_elegido = horarios[opcion_materia - 1][opcion_horario - 1]

                    # Guardar tutoría
                    tutorias_guardadas.append([nombre, materia_elegida, horario_elegido])
                    cupos_disponibles[opcion_materia - 1][opcion_horario - 1] -= 1

                    # Guardar en archivo CSV
                    GuardadoDeAuditorias.guardar_en_csv(tutorias_guardadas)

                    print(" Tutoría agendada y guardada correctamente.")
                else:
                    print(" No hay cupos disponibles para ese horario.")
            else:
                print(" Horario no válido.")
        else:
            print(" Materia no válida.")
    except ValueError:
        print(" Entrada inválida. Solo se permiten números.")
    except Exception as e:
        print(" Ha ocurrido un error al intentar agendar la tutoría.")
        print(f"Detalles del error: {e}")

# Ver tutorías guardadas
def ver_tutorias():
    print("\n--- Tutorías agendadas ---")

    total = len(tutorias_guardadas)

    if total == 0:
        print("No hay tutorías agendadas aún.")
    else:
        if total == 1:
            print("Tienes 1 tutoría guardada:\n")
        else:
            print(f"Tienes {total} tutorías guardadas:\n")

        for i, tutoria in enumerate(tutorias_guardadas, start=1):
            print(f"{i}. {tutoria[0]} - {tutoria[1]} - {tutoria[2]}")
