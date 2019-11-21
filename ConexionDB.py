"""
Nombre: ConexionBD.py
Objetivo: Conexion de la BDD con mysql
Autor: Lucio David Morán B
Fecha: 13 de noviembre de 2019
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="mibase",
    passwd=""
)

print(mydb)
