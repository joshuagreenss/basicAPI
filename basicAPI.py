import flask

app = flask.Flask(__name__)

@app.route('/',methods=['GET']
def hello():
    return "<p>Hello world!</p>"

app.run(host="0.0.0.0",port=8090)