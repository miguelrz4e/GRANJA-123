
def main():
    opcion = input("Por favor, ingrese la opción deseada (cultivo/ganado): ")
    if opcion.lower() == "cultivo":
        from consolagranja import consultar_cultivos
        consultar_cultivos()
    elif opcion.lower() == "ganado":
        from consolaganado import consultar_ganado
        consultar_ganado()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
