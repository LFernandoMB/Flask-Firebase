from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

link = "https://nodemcu-cb45c.firebaseio.com/"

@app.route('/')
def get_data():
    lista = list()
    requisicao = requests.get(f'{link}.json')
    dict_requisicao = requisicao.json()
    for k, v in dict_requisicao.items():
        lista.append(f'{k} - {v}')
    return render_template('index.html', list=lista)

if __name__ == '__main__':
    app.run(debug=True)