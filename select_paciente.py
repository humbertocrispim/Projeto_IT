from re import S
import mysql.connector

conectbd = mysql.connector.connect(
  host="localhost",
  user="root",
  password="teste",
  database="projetoit"
)

def SelectdadosPacientes():

    cursor = conectbd.cursor()

    #input_consulta = input("Coloque aqui o nome ou cpf da consulta")
    comando_sql = "SELECT * FROM pacientes  WHERE nome '%hum%'"

    cursor.execute(comando_sql)

    resultado = cursor.fetchall()
    print(resultado)

SelectdadosPacientes()