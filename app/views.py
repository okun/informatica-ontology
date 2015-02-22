# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:58:15 2015

@author: toporkov
"""

from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    ontology_title = 'informatica'
    return render_template("index.html", ontology_title=ontology_title)