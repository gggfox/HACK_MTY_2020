from flask import Flask
from blockchain import Blockchain
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
