#!/usr/bin/env python3

from flask import Flask, render_template

# Gandalf Sax Guy 10 Hours HD
DEFAULT_ID = 'G1IbRujko-A'
# Las mejores frases de Gandalf en 'El señor de los anillos' | Fotogramas
ALTERNATE_ID = 'jbauqKIApoA'

app = Flask(__name__)

# define homage
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html', link_id=ALTERNATE_ID, youtube_id=DEFAULT_ID)

@app.route('/<id>', methods=['GET'])
def id(id):
    return render_template('index.html', link_id=id, youtube_id=id)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
