# GuardadoDeAuditorias.py
# Aquí guardamos las tutorías en un archivo CSV para que no se pierdan cuando se cierre el programa

# Función que guarda las tutorías en un archivo CSV
def guardar_en_csv(lista_tutorias, nombre_archivo="tutorias.csv"):
    # Si la lista está vacía, no guardamos nada
    if len(lista_tutorias) == 0:
        print(" No hay tutorías para guardar.")
        return

    try:
        # Abrimos o creamos el archivo en modo escritura (sobrescribe lo anterior)
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            # Escribimos el encabezado del archivo
            archivo.write("Nombre,Materia,Horario\n")

            # Escribimos cada tutoría en una línea del archivo
            for tutoria in lista_tutorias:
                # Cada tutoria es una lista con: [nombre, materia, horario]
                linea = f"{tutoria[0]},{tutoria[1]},{tutoria[2]}\n"
                archivo.write(linea)

        # Confirmación de guardado
        print(" Las tutorías han sido guardadas correctamente.\n")

    except Exception as e:
        # Si hay error al guardar
        print(" Error al guardar archivo:", e)





