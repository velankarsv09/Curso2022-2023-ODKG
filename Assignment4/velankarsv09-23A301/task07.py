# -*- coding: utf-8 -*-
"""**task07.ipynb"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
ns = Namespace("http://somewhere#")
from rdflib.plugins.sparql import prepareQuery

#RDFLib
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s) # Visualize the results

#SPARQL
q1 = q1 = prepareQuery('''
  SELECT ?Sub WHERE { 
    ?Sub rdfs:subClassOf ns:Person. 
    }
  ''',
  initNs = { "ns": ns,
            "rdfs": RDFS}
)

for r in g.query(q1): 
  print(r) # Visualize the results

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses) [testo del link](https://)**"""

# TO DO

#RDFLib
for s1,p1,o1 in g.triples((None, RDF.type, ns.Person)):  # Individuals of Person
  print(s1) # Visualize the results
print("a")
for s1,p1,o1 in g.triples((None, RDFS.subClassOf, ns.Person)): #Individuals of Subclasses of Person
    for s2,p2,o2 in g.triples((None, RDF.type, s1)):
        print(s2) # Visualize the results

#SPARQL
q2 = prepareQuery('''
  SELECT ?Ind WHERE { 
    ?subclass rdfs:subClassOf* ns:Person.
    ?Ind rdf:type ?subclass. 
    }
  ''',
  initNs = {"ns":ns,
            "rdf":RDF,
            "rdfs":RDFS
            }
)

for r in g.query(q2): # Visualize the results
  print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""

# TO DO

#RDFLib
for s1,p1,o1 in g.triples((None, RDF.type, ns.Person)):  # Individuals,Properties and Classes of Person
  for s2,p2,o2 in g.triples((s1,None,None)):
    print(s2,p2,o2) # Visualize the results

print ("a")

for s1,p1,o1 in g.triples((None, RDFS.subClassOf, ns.Person)): #Individuals,Properties and Classes of Person
    for s2,p2,o2 in g.triples((None, RDF.type, s1)):
      for s3,p3,o3 in g.triples((s2,None,None)):
        print(s3,p3,o3) # Visualize the results


#SPARQL
q3 = prepareQuery('''
  SELECT ?Ind ?prop ?class WHERE { 
    ?subclass rdfs:subClassOf* ns:Person.
    ?Ind rdf:type ?subclass.
    ?Ind ?prop ?class
    }
  ''',
  initNs = {"ns":ns,
            "rdf":RDF,
            "rdfs":RDFS,
            }
)

for r in g.query(q3): # Visualize the results
  print(r)