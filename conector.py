
import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='S@xa2115',
    database='teste'
)

mycursor = con.cursor()


def InserirTabelaPaciente():
    print("\nEsta e uma tela para inseririr dados dos Pacientes")
    input_nome = input("Digite nome: ")
    input_endereco = input("Digite ser endereço: ")
    input_idade = input("Digite a idade do paciente: ")
    input_cpf = input("Digite o CPF do paciente: ")
    input_rg = input("Digite o RG do paciente: ")
    input_sexo = input("Digite o sexo do paciente: ")
    input_cep = input("Digite o CEP do paciente: ")
    input_bairro = input("Digite o bairro do paciente: ")
    input_cidade = input("Digite o cidade do paciente: ")
    input_estado = input("Digite o estado do paciente: ")
    input_telefone = input("Digite o telefone do paciente: ")
    input_altura = input("Digite o altura do paciente: ")
    input_peso = input("Digite o peso do paciente: ")


    comando_sql = ("INSERT INTO Paciente (nome,endereco,idade,cpf,rg,sexo,cep,bairro,cidade,estado,telefone,altura,peso) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    valores = (input_nome, input_endereco,input_idade,input_cpf,input_rg,input_sexo,input_cep,input_bairro,input_cidade,input_estado,input_telefone,input_altura,input_peso)

    mycursor.execute(comando_sql, valores)