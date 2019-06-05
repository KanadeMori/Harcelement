#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "G. Khaznadar"

import pygraphviz as pgv

from dot.dot2html import cree_html
from dot.dot2svg import cree_svg

"""
La classe AGraph est documentée à
http://pygraphviz.github.io/documentation/pygraphviz-1.5/reference/agraph.html

ici, les seules méthodes utilisées sont :
- le constructeur,
- from_string(),
"""
A=pgv.AGraph(      # création d'un graphe
    directed=True, # les liens sont directifs
)

# lecture du graphe depuis un fichier .dot
A.from_string(open("BD0.dot","r").read())

cree_html(A, path="output")
print("les fichier html sont créés dans le dossier output/ ;")

cree_svg(A, target="mongraphe.svg")
print("le fichier mongraphe.svg est créé.")
