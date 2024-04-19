from flask import Flask

import json

app = Flask(__name__)

api = '/api/card-scheme/verify/'

@app.route(api, methods=['GET'])
def verify():
    return json.dumps([])