# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify


TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
url = 'https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# Запускаємо Flask додаток (він потрібен нам для обробки POST запитів)
app = Flask(__name__)


# Метод який приймає POST запити від телеграм і обробляє їх
@app.route('/', methods=['POST'])
def index():
    r = request.get_json()
    print(r)
    return jsonify(r)  # Повертає JSON об'єкт


# ---------------------------------------
if __name__ == '__main__':
    app.run()
