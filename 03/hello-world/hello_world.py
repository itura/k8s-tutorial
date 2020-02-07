import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def endpoint():
    with open('/data/hello.txt', 'a') as f:
        f.write('Hello World\n')

    response = ""
    with open('/data/hello.txt', 'r') as f:
        for line in f:
            response = response + line

    return response

app.run(host='0.0.0.0', port='8080')
