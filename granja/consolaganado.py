import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-Q2SVJUH\\SQLEXPRESS;'
    'DATABASE=granja;'
    'Trusted_Connection=yes;'
)

try:
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ganado")
    resultado = cursor.fetchone()
    while resultado:
        print(resultado)
        resultado = cursor.fetchone() 

    while True:
        actualizar = input("\n¿Quieres actualizar un registro? (s/n): ")
        if actualizar.lower() == "s":
            idl = input("Ingresa el ID del registro que deseas modificar: ")
            consultaverificacion = "SELECT idganado FROM ganado WHERE idganado = ?;"
            cursor.execute(consultaverificacion, (idl,))
            resultado = cursor.fetchone()
            if resultado:
                especie = input("Ingresa la especie del animal: ")
                edad = input("Ingresa la edad del animal: ")
                raza = input("Ingresa la raza del animal: ")
                consultau = "UPDATE ganado SET especie = ?, edad = ?, raza = ? WHERE idganado = ?;"
                cursor.execute(consultau, (especie, edad, raza, idl))
                conn.commit()
                print("¡El registro se actualizó correctamente!")
            else:
                print("¡El ID ingresado es incorrecto!")
        else:
            print("Saliendo de la actualización o modificación de registros.")
            break

    while True:
        eliminar = input("\n¿Quieres eliminar un registro? (s/n): ")
        if eliminar.lower() == "s":
            idl = input("Ingresa el ID del registro que deseas eliminar: ")
            consultaverificacion = "SELECT idganado FROM ganado WHERE idganado = ?;"
            cursor.execute(consultaverificacion, (idl,))
            resultado = cursor.fetchone()
            if resultado:
                consultad = "DELETE FROM ganado WHERE idganado = ?;"
                cursor.execute(consultad, (idl,))
                conn.commit()
                print("¡El registro se eliminó correctamente!")
            else:
                print("¡El ID ingresado es incorrecto!")
        else:
            print("Saliendo de la eliminación de registros.")
            break

    mostrar_produccion = input("\n¿Quieres ver la producción total de ganado? (s/n): ")
    if mostrar_produccion.lower() == "s":
        cursor.execute("SELECT SUM(Peso) FROM ganado")
        total_produccion = cursor.fetchone()[0]
        if total_produccion is not None:
            print(f"\nProducción total del ganado es: {total_produccion}")
        else:
            print("\nNo hay producción de ganado registrada.")

except Exception as e:
    print("Ocurrió un error:", e)
finally:
    conn.close()
