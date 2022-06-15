import mysql.connector

conectbd = mysql.connector.connect(
  host="localhost",
  user="root",
  password="teste",
  database="projetoit"
)

def InsertdadosPacientes():

    print("\nBem vindos ao cadastro de pacientes: ")

    cursor = conectbd.cursor()

    input_nome = input("Digite nome do paciente: ")
    input_endereco = input("Digite o endereço do paciente: ")
    input_idade = input("Digite a idade do paciente: ")
    input_cpf = input("Digite o CPF do paciente: ")
    input_rg = input("Digite o RG do paciente: ")
    input_sexo = input("Digite o sexo do paciente: ")
    input_cep = input("Digite o CEP do paciente: ")
    input_bairro = input("Digite o bairro do paciente: ")
    input_cidade = input("Digite a cidade do paciente: ")
    input_estado = input("Digite o estado do paciente: ")
    input_telefone = input("Digite o telefone do paciente: ")
    input_altura = input("Digite a altura do paciente: ")
    input_peso = input("Digite o peso do paciente: ")

    comando_sql = "INSERT INTO pacientes (nome,endereco,idade,cpf,rg,sexo,cep,bairro,cidade,estado,telefone,altura,peso) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (input_nome, input_endereco,input_idade,input_cpf,input_rg,input_sexo,input_cep,input_bairro,input_cidade,input_estado,input_telefone,input_altura,input_peso)


    cursor.execute(comando_sql, valores)

    conectbd.commit()

    print(cursor.rowcount, "Paciente cadastrado com sucesso! .")

