import requests

cpf = input("Digite seu cpf: ")

verifica_json = requests.get('${endereco}/verifica/'+cpf)

verifica = verifica_json.json()

if verifica['cpf'] == 'valido':
    print("CPF VÁLIDO")
else:
    print("CPF INVÁLIDO")
