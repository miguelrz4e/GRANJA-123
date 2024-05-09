import pyodbc


conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-Q2SVJUH\\SQLEXPRESS;'
    'DATABASE=granja;'
    'Trusted_Connection=yes;'
)

try:
    cursor = conn.cursor()

   
    cursor.execute("SELECT * FROM cultivos")
    resultado = cursor.fetchone()
    while resultado:
        print(resultado)
        resultado = cursor.fetchone() 

   
    while True:
        actualizar = input("\n¿Quieres actualizar un registro? (s/n): ")
        if actualizar.lower() == "s":
            idl = input("Ingresa el ID del registro que deseas modificar: ")
            consultaverificacion = "SELECT idcultivos FROM cultivos WHERE idcultivos = ?;"
            cursor.execute(consultaverificacion, (idl,))
            resultado = cursor.fetchone()
            if resultado:
                nombre = input("Ingresa el nuevo nombre del cultivo: ")
                tipo = input("Ingresa el nuevo tipo de cultivo: ")
                consultau = "UPDATE cultivos SET Nombrecultivo = ?, tipocultivo = ? WHERE idcultivos = ?;"
                cursor.execute(consultau, (nombre, tipo, idl))
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
            consultaverificacion = "SELECT id FROM login WHERE id = ?;"
            cursor.execute(consultaverificacion, (idl,))
            resultado = cursor.fetchone()
            if resultado:
                consultad = "DELETE FROM login WHERE id = ?;"
                cursor.execute(consultad, (idl,))
                conn.commit()
                print("¡El registro se eliminó correctamente!")
            else:
                print("¡El ID ingresado es incorrecto!")
        else:
            print("Saliendo de la eliminación de registros.")
            break

   
    mostrar_produccion = input("\n¿Quieres ver la producción total de cultivos? (s/n): ")
    if mostrar_produccion.lower() == "s":
        cursor.execute("SELECT SUM(Rendimiento) FROM cultivos")
        total_produccion = cursor.fetchone()[0]
        print(f"\nProducción total de cultivos: {total_produccion}")

except Exception as e:
    print("Ocurrió un error:", e)
finally:
    conn.close()


                



