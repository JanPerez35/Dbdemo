from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def greeting():
    return 'Hello World! This is the DB Project'

@app.route('/PersonApp')
def greeting2():
    return 'Hello World! This is the db Part App'


if __name__ == '__main__':
    app.run(debug=True)

