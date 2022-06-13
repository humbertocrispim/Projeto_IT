import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='S@xa2115',
    database='teste'
)

mycursor = con.cursor()

sql = "INSERT INTO teste"

# Create database

def CriarBase():
    mycursor.execute("CREATE DATABASE testconect")


# isert tables

def Criartabela():
    mycursor.execute("CREATE TABLE  (nome TEXT, senha TEXT)")



def Altertable():
    mycursor.execute("ALTER TABLE clientes ADD Rua varchar(11) NULL;")
    


# insert dados

def InserirDados():
    input_nome = input("Digite seu nome: ")
    input_endereco = input("digite ser endereço: ")
    input_idade = input("digite a idade do paciente: ")
    input_cpf = input("digite o CPF do paciente: ")
    input_rg = input("igite o RG do paciente: ")
    input_sexo = input("igite o sexo do paciente: ")
    input_cep = input("igite o CEP do paciente: ")
    input_bairro = input("igite o bairro do paciente: ")
    input_cidade = input("igite o cidade do paciente: ")
    input_estado = input("igite o estado do paciente: ")
    input_telefone = input("igite o telefone do paciente: ")
    input_altura = input("igite o altura do paciente: ")
    input_peso = input("igite o peso do paciente: ")


    comando_sql = "INSERT INTO Paciente (nome,endereco,idade,cpf,rg,sexo,cep,bairro,cidade,estado,telefone,altura,peso) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (input_nome, input_endereco,input_idade,input_cpf,input_rg,input_sexo,input_cep,input_bairro,input_cidade,input_estado,input_telefone,input_altura,input_peso)

    mycursor.execute(comando_sql, valores)
    con.commit()



InserirDados()
#   INSERT INTO teste.Paciente (nome,endereco,idade,cpf,rg,sexo,mae,cep,bairro,cidade,estado,telefone_fixo,celular,altura)