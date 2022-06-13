import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='S@xa2115',
    database='testconect'
)

mycursor = con.cursor()

sql = "INSERT INTO teste"

# Create database

def CriarBase():
    mycursor.execute("CREATE DATABASE testconect")


# isert tables

def Criartabela():
    mycursor.execute("CREATE TABLE clientes (nome TEXT, senha TEXT)")



def Altertable():
    mycursor.execute("ALTER TABLE clientes ADD Rua varchar(11) NULL;")
    


# insert dados

def InserirDados():
    input_nome = input("Digite seu nome: ")
    input_senha = input("digite sua senha: ")

    comando_sql = "INSERT INTO clientes (nome, senha) VALUES(%s,%s)"
    valores = (input_nome, input_senha)

    mycursor.execute(comando_sql, valores)
    con.commit()


Altertable()