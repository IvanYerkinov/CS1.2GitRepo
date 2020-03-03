from flask import Flask
from random import randint
from markovmaster import MarkovChain

app = Flask(__name__)


@app.route('/')
def hello_world():
    bot = MarkovChain("test.txt", 2)
    return str(bot.walk_queue(randint(20, 50)))
