from flask import Flask, request, render_template, make_response
from flask_bootstrap import Bootstrap

import os
import uuid
import base64

from PIL import Image
import warnings
warnings.simplefilter('error', Image.DecompressionBombWarning)

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def do_get():
    return render_template('index_line.html')
# ryoshi
@app.route('/ryoushi')
def ryoushi():
    return render_template('course_ryoushi.html')
# sumkoguri
@app.route('/sumoguri')
def sumoguri():
    return render_template('course_sumoguri.html')
# urashima
@app.route('/urashima')
def urashima():
    return render_template('course_urashima.html')

@app.route('/date')
def date():
    return render_template('date.html')

@app.route('/final')
def final():
    return render_template('final.html')

@app.route('/line')
def line():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()