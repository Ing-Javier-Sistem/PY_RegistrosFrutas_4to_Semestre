# main.py

from funcionalidades_database import Database
from clases_objeto_frutas import Fruta


def main():
    db = Database()

    while True:
        print("\nMenú:")
        print("1. Agregar fruta")
        print("2. Editar fruta")
        print("3. Eliminar fruta")
        print("4. Mostrar frutas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_fruta = input("ID de la fruta: ")
            tipo_fruta = input("Tipo de fruta: ")
            valor_fruta = input("Valor de fruta: ")
            fruta = Fruta(id_fruta, tipo_fruta, valor_fruta)
            db.guardar_fruta(fruta)

        elif opcion == "2":
            id_fruta = input("ID de la fruta a editar: ")
            tipo_fruta = input("Nuevo tipo de fruta: ")
            valor_fruta = input("Nuevo valor de fruta: ")
            fruta = Fruta(id_fruta, tipo_fruta, valor_fruta)
            db.editar_fruta(fruta)

        elif opcion == "3":
            id_fruta = input("ID de la fruta a eliminar: ")
            db.eliminar_fruta(id_fruta)

        elif opcion == "4":
            db.mostrar_frutas()

        elif opcion == "5":
            break


if __name__ == "__main__":
    main()
