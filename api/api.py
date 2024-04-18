from flask import Flask

app = Flask(__name__)

api = '/api/card-scheme/verify/'

@app.route(api, methods=['GET'])
def verify():
    pass