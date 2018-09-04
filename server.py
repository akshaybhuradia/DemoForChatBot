from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index() :
    return "Chat Bot"

if __name__ == '__main__':
    app.debug = True
    app.run()
