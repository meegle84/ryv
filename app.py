#!/usr/bin/env python3

from flask import Flask, render_template, redirect, request, url_for
import requests
import secrets

# Gandalf Sax Guy 10 Hours HD
DEFAULT_ID = 'G1IbRujko-A'
# Las mejores frases de Gandalf en 'El señor de los anillos' | Fotogramas
ALTERNATE_ID = 'jbauqKIApoA'
# Youtube uri
YT = 'https://www.youtube.com/'

YT_WATCH_QUERY = 'watch?v='
OEMBED_QUERY = 'oembed?format=json&url='

# functions
def is_url_ok(url):
    return 200 == requests.head(url).status_code

def get_random_id():
    return secrets.token_urlsafe(8)

def is_valid_random_id(id):
    return is_url_ok(YT + YT_WATCH_QUERY + id)

def get_valid_random_id():
    valid_id = False
    while not valid_id:
        random_id = get_random_id()
        print(random_id)
        valid_id = is_valid_random_id(random_id)
        print(valid_id)
    else:
        return random_id

# start flask app
app = Flask(__name__)
app.config['development'] = True
app.config['SECRET_KEY'] = DEFAULT_ID

# define homage
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html', link_id=ALTERNATE_ID, youtube_id=DEFAULT_ID)

@app.route('/<id>', methods=['GET'])
def id(id):
    return render_template('index.html', link_id=id, youtube_id=id)

@app.route('/reload/', methods=['POST'])
def reload_clicked():
    app.logger.info('reload')
    return redirect('/')

@app.route('/random/', methods=['POST', 'GET'])
def random():
    if request.method == 'POST':
        random_id = get_valid_random_id()
        return redirect(url_for('id', id=random_id))
    else:
        return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
