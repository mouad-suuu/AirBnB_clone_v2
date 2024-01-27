#!/usr/bin/python3
"""
adding the C rout and <text>
"""

from flask import Flask

app = flask(__name__)

@app.route('/',strict_slashes=False)
def index():
    """
    returning Hello HBNB!
    """
    return 'Hello HBNB!'

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """
    returning HBNB!
    """
    return 'HBNB'

@app.route('/c/<text>',strict_slashes=False)
def Cis(text):
    """
    returning what is in the <text>
    """
    return 'C' + text.replace('_', ' ' )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
