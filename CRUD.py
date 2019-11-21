"""
Nombre: CRUD.py
Objetivo: Menú CRUD con operaciones
Autor: Lucio David Morán B
Fecha: 13 de noviembre de 2019
"""
import mysql.connector

mydb = ""

#---------------------------------------
# abre la conexión con la base de datos
#---------------------------------------
def abrirConexionDB():
    global mydb = mysql.connector.connect(
        host="localhost",
        user="mibase",
        passwd=""
    )
    # Imprime la versión de la SBD mysql
    print(mydb)


#---------------------------------------------------
# Función para insertar registros a la base de datos
#----------------------------------------------------
def insertarRegistro():
    print(" --- Módulo para Insertar Registros ---")
    # solicitamos los tres campos
    clave1 = input("Introduce clave del trabajador:")
    nombre1 = input("Introduce nombre del trabajador:")
    sueldo1 = input("Introduce sueldo del trabajador:")

    mycursor = mydb.cursor()

    sql = "INSERT INTO trabajadores(clave, nombre, sueldo) VALUES (clave1, nombre1, sueldo1)"
    # ejecutamos sentencia sql
    mycursor.execute(sql)
    # Operación de vaciar el buffer del servidor
    mydb.commit()
    print(mycursor.rowcount, "Trabajador insertado ..")


def buscarRegistro():
    print(" --- Módulo para buscar un registro ---")
    # solicitamos el campo de clave
    clave1 = input("Ingresa una clave a buscar: ")
    
    mycursor = mydb.cursor()

    sql = "SELECT from trabajadores where clave = clave1"
    mycursor.execute(sql)
    mydb.commit()
    print(sql)


def cambiarRegistros():
    print(" --- Módulo para cambiar un registro ---")
    # solicitamos el campo de clave
    clave1 = input("Ingrese la clave de un trabajador: ")
    sueldo1 = input("Ingrese el nuevo sueldo: ")
    
    mycursor = mydb.cursor()

    sql = "UPDATE trabajadores set sueldo = sueldo1 where clave = clave1"
    mycursor.execute(sql)
    mydb.commit()
    print(sql)
    print("Sueldo modificado!")


def borrarRegistros():
    print(" --- Módulo para borrar un registro ---")
    # solicitamos el campo de clave
    clave1 = input("Ingrese la clave de un trabajador: ")
    
    mycursor = mydb.cursor()

    sql = "DELETE from trabajadores where clave = clave1"
    mycursor.execute(sql)
    mydb.commit()
    print(sql)
    print("Registro borrado...")


def listarRegistros():
    print("Listado de todos los regitros")
    mycursor = mydb.cursor()

    sql = "SELECT * from trabajadores"
    mycursor.execute(sql)
    mydb.commit()
    print(sql)


# Imprime menu de opciones
#---------------------------------------
def dashboard():
    ciclo = "S"
    while ciclo == "S" or ciclo == "s":
        print(" --- CRUD  con MYSQL ---")
        print("1. Insertar registros ")
        print("2. Buscar registros ")
        print("3. Cambiar registros")
        print("4. Borrar registros")
        print("5. Lista de registros ")
        print("6. Salir")
        print("\n")
        ciclo = input("Seleccione una opción entre 1 y 6")

        if ciclo == 1:
            insertarRegistro()
        elif ciclo == 2:
            buscarRegistro()
        elif ciclo == 3:
            cambiarRegistros()
        elif ciclo == 4:
            borrarRegistros()
        elif ciclo == 5:
            listarRegistros()
        elif ciclo == 6:
            ciclo = "n"
    # else del while
    else:
        print("Por favor introduce un número entero entre 1 y 6")




# función main
def main():
    # abrimos conexion a la BD
    abrirConexionDB()
    # corremos el dashboard de opciones
    dashboard()


if __name__ == "__main__":
    main()