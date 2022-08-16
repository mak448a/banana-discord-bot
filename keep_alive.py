from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return '<h1>Welcome!</h1>'


def run():
    app.run(host='0.0.0.0', port=5555)


def keep_alive():
    '''
	Creates and starts new thread that runs the function run.
	'''
    t = Thread(target=run)
    t.start()
