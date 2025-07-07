# EliminarAuditorias.py
# Función para eliminar tutorías guardadas

from RegistroDeAuditorias import tutorias_guardadas, cupos_disponibles, materias, horarios
import GuardadoDeAuditorias

def eliminar_tutoria():
    print("\n--- Eliminar tutoría ---")

    total = len(tutorias_guardadas)

    if total == 0:
        print("No hay tutorías para eliminar.\n")
        return

    # Mostrar tutorías con número
    for i, tutoria in enumerate(tutorias_guardadas, start=1):
        print(f"{i}. {tutoria[0]} - {tutoria[1]} - {tutoria[2]}")

    try:
        opcion = input("Escribe el número de la tutoría a eliminar (0 para cancelar): ")
        opcion_int = int(opcion)

        if opcion_int == 0:
            print("Operación cancelada.\n")
            return

        if 1 <= opcion_int <= total:
            tutoria_eliminar = tutorias_guardadas[opcion_int - 1]

            materia = tutoria_eliminar[1]
            horario = tutoria_eliminar[2]

            # Buscar índice materia y horario para aumentar cupo
            if materia in materias:
                idx_materia = materias.index(materia)
                if horario in horarios[idx_materia]:
                    idx_horario = horarios[idx_materia].index(horario)
                    cupos_disponibles[idx_materia][idx_horario] += 1

            # Quitar tutoría
            tutorias_guardadas.pop(opcion_int - 1)

            # Guardar cambios en CSV
            GuardadoDeAuditorias.guardar_en_csv(tutorias_guardadas)

            print("Tutoría eliminada.\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Debes escribir un número.\n")
    except Exception as e:
        print(f"Error: {e}\n")
