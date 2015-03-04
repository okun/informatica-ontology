# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:58:15 2015

@author: toporkov
"""

from flask import request, render_template, jsonify
from app import app
import rdflib

@app.route('/gettree')
def getTree():
    onto=rdflib.Graph()
    onto.parse("app/root-ontology.owl")
    results = onto.query("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?node ?parent  ?value
	WHERE { ?node rdfs:subClassOf ?parent .
	?node rdfs:comment ?description . }
    """)
    json_result = results.serialize(format='json', encoding='utf8')
    return json_result
    
@app.route('/')
@app.route('/index')
def index():
    
    ontology_title = 'informatica'

    return render_template("index.html", ontology_title=ontology_title)