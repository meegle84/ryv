#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
