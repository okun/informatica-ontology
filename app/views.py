# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:58:15 2015

@author: toporkov
"""

from flask import render_template
from app import app
import rdflib
@app.route('/')
@app.route('/index')
def index():
    onto=rdflib.Graph()
    onto.parse("/root-ontology.owl")
    results = onto.query("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?subject ?object  ?value
	WHERE { ?subject rdfs:subClassOf ?object .
	?subject rdfs:comment ?value . }
    """)
    json_result = results.serialize(format='json', encoding='utf8')
    ontology_title = 'informatica'
    return render_template("index.html", ontology_title=ontology_title)