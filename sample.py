# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:29:31 2015

@author: toporkov
"""
import rdflib

onto=rdflib.Graph()
    #onto.parse("/root-ontology.owl")
onto.parse("app/root-ontology.owl")
results = onto.query("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?subject ?object  ?value
	WHERE { ?subject rdfs:subClassOf ?object .
	?subject rdfs:comment ?value . }
    """)

json_result = results.serialize(format='json', encoding='utf8')
#for row in json_result:
#    print row
print json_result
