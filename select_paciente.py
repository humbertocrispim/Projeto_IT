import mysql.connector

conectbd = mysql.connector.connect(
  host="localhost",
  user="root",
  password="teste",
  database="projetoit"
)

def SelectdadosPacientes():

    cursor = conectbd.cursor()

    print("\nVoce pode consultar os dados do paciente digitando nome, cpf ou numero de telefone. ")
    
    input_consulta = input("\nDigite a opção desejada: ")
    
    
    if input_consulta == "nome":
      input_nome_paciente = input("Agora digite o nome do paciente: ")
      comando_sql = f"SELECT * FROM pacientes WHERE {input_consulta} LIKE '%{input_nome_paciente}%'"
    
    elif input_consulta == "cpf":
      input_cpf_paciente = input("Agora digite o cpf do paciente: ")
      comando_sql = f"SELECT * FROM pacientes WHERE {input_consulta} LIKE '%{input_cpf_paciente}%'"
    
    elif input_consulta == "telefone":
      input_telefone_paciente = input("Agora digite o telefone do paciente: ")
      comando_sql = f"SELECT * FROM pacientes WHERE {input_consulta} LIKE '%{input_telefone_paciente}%'"


    cursor.execute(comando_sql)

    resultado = cursor.fetchall()
    print(resultado)

