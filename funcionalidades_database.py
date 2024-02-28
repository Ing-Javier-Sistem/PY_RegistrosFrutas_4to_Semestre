# funcionalidades_database.py

import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="tu_host",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_de_datos"
        )
        self.cursor = self.conn.cursor()

    def guardar_fruta(self, fruta):
        try:
            # Insertar una nueva fruta en la base de datos
            query = "INSERT INTO frutas (id_fruta, tipo_fruta, valor_fruta) VALUES (%s, %s, %s)"
            values = (fruta.id_fruta, fruta.tipo_fruta, fruta.valor_fruta)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Fruta guardada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al guardar la fruta: {err}")

    def editar_fruta(self, fruta):
        try:
            # Actualizar una fruta en la base de datos por su ID
            query = "UPDATE frutas SET tipo_fruta = %s, valor_fruta = %s WHERE id_fruta = %s"
            values = (fruta.tipo_fruta, fruta.valor_fruta, fruta.id_fruta)
            self.cursor.execute(query, values)
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Fruta editada exitosamente.")
            else:
                print("No se encontró ninguna fruta con el ID especificado.")
        except mysql.connector.Error as err:
            print(f"Error al editar la fruta: {err}")

    def eliminar_fruta(self, id_fruta):
        try:
            # Eliminar una fruta de la base de datos por su ID
            query = "DELETE FROM frutas WHERE id_fruta = %s"
            value = (id_fruta,)
            self.cursor.execute(query, value)
            self conn.commit()
            if self.cursor.rowcount > 0:
                print("Fruta eliminada exitosamente.")
            else:
                print("No se encontró ninguna fruta con el ID especificado.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar la fruta: {err}")

    def mostrar_frutas(self):
        try:
            # Mostrar todas las frutas en la base de datos
            query = "SELECT * FROM frutas"
            self.cursor.execute(query)
            frutas = self.cursor.fetchall()
            if frutas:
                print("Lista de frutas:")
                for fruta in frutas:
                    print(f"ID: {fruta[0]}, Tipo: {fruta[1]}, Valor: {fruta[2]}")
            else:
                print("No hay frutas en la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error al mostrar las frutas: {err}")
