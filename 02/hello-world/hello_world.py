import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def endpoint():
    return 'Hello World'

app.run(host='0.0.0.0', port='8080')
