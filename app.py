from flask import Flask
from dictionary_words import run_dictionary
app = Flask(__name__)


@app.route('/')
def hello_world():
    return str(run_dictionary(5))
