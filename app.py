#!/usr/bin/env python3

from flask import Flask, render_template

# Gandalf Sax Guy 10 Hours HD
DEFAULT_ID = 'G1IbRujko-A'

app = Flask(__name__)

# define homage
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html', youtube_id=DEFAULT_ID)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
