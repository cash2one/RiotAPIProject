#!/usr/bin/python
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
if app.debug:
    from werkzeug.debug import DebuggedApplication
    app.wsgi_app = DebuggedApplication( app.wsgi_app, True )


import FlaskApp.views
