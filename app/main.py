from flask import Flask, jsonify, request

app = Flask(__name__) 


@app.route('/https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL', methods =['GET'])
def getConversao():
    json_data = request.json
    print(json_data)

if __name__ == '__main__':
    app.run()