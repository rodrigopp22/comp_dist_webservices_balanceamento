import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/convertemoeda/<valor_consultado_brl>', methods=['GET'])
def home(valor_consultado_brl):
    try:
        valor_consultado_brl = float(valor_consultado_brl.replace(',','.'))
    except:
        return "Informar valor numerico.."
    return convertemoeda(valor_consultado_brl)

def convertemoeda(valor_em_brl):
    response = requests.request('GET', 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL').json()
    usd_para_real = float(response['USDBRL']['ask'])
    eur_para_real = float(response['EURBRL']['ask'])
    resultado = {
        "conversao": {
            "real": valor_em_brl,
            "dolar": valor_em_brl/usd_para_real,
            "euro": valor_em_brl/eur_para_real,
        }
    }
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
