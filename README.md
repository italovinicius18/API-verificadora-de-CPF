# API-verificadora-de-CPF
API feita em Flask que tem como função verificar se o CPF é válido ou inválido 

## Requisitos

- Flask
- Requests

## Como utilizar a API

1. Primeiro precisa iniciar o flask

```shell
flask run 
```

2. Modifique o endereço de requisição, no arquivo teste.py, para o gerado a partir do comando anterior

```shell
verifica_json = requests.get('${endereco}/verifica/'+cpf)
```

3. Agora já pode rodar o teste.py a partir do comando abaixo e testar vários cpf's

```shell
python3 teste.py
```

Gostaria de poder melhorar essa API a partir de outros frameworks, como o Django Restful Framework ou melhorar a análise do CPF por meio de outras funções auxiliares, modularizando um pouco mais o código