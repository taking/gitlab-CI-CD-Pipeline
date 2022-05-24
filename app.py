#!/usr/bin/python

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'ok'}), 200


@app.route('/test')
def test():
    return jsonify({'message': 'test'}), 200


if __name__ == "__main__":
    print("Hello World!")
    app.run(debug=True, host="0.0.0.0", port=8080)
