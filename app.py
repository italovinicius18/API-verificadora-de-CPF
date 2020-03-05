from flask import Flask,jsonify
import re

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Api focada em verificar cpf", 200

@app.route('/verifica/<string:cpf>',methods=['GET'])
def verifica_cpf(cpf):
    cpf = re.sub('[^0-9]', '', cpf) # Utilizo regex para descartar caracteres que são diferentes de números
    if(len(cpf)!=11 or cpf.count(cpf[0])==11): # Se o cpf for diferente de 11 ou se todos números forem repetidos
        return jsonify({
            'cpf': 'invalido'
        })
    else:
        digito1_verificado = False
        digito2_verificado = False
        resultado = 0
        a = 10
        for i in range(0,9):
            resultado+=int(cpf[i])*a
            a-=1
        resto = (resultado*10)%11
        if(resto==10):
            resto = 0
        if(resto==int(cpf[9])): # Verifica o primeiro dígito verificador
            digito1_verificado = True
        resultado = 0
        a = 11
        for i in range(0,10):
            resultado+=int(cpf[i])*a
            a-=1
        resto = (resultado*10)%11
        if(resto==10):
            resto = 0
        if(resto==int(cpf[10])): # Verifica o segundo dígito verificador
            digito2_verificado = True
        print(digito1_verificado,digito2_verificado)
        if digito1_verificado and digito2_verificado:
            return jsonify({
                'cpf': 'valido'
            })
        else:
            return jsonify({
                'cpf': 'invalido'
            })



if __name__ == '__main__':
    app.run(debug==True)

