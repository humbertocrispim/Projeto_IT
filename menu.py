from Insert_paciente import InsertdadosPacientes
from select_paciente import SelectdadosPacientes


print(f"\nOla você esta no sistema de cadastro e consultas, de pacientes.")
print("\nDigite 1 para cadastrar paciente: ")
print(f"\nDidite 2 para consultar pacientes cadastrados: ")

opcao = int(input("\ndigite opção: "))


if opcao == 1:
    InsertdadosPacientes()
    
elif opcao == 2:
    SelectdadosPacientes()

else:
    print("Didite opção 1 ou 2")

