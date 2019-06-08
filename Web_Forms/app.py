from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_book_details():
    author=request.args.get('author')
