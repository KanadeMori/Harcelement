#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "G. Khaznadar"

import pygraphviz as pgv

def cree_html(node, edges, path="output"):
    """
    Crée un fichier HTML sous le répertoire path,
    correspondant à un noeud du graphe
    @param node le noeud du graphe pour la page
    @param edges liste de tous les liens du graphe
    @param path répertoire où créer la nouvelle page HTML
    """
    # création du répertoire si celui-ci n'existe pas encore
    import os
    os.makedirs(path, exist_ok=True)
    
    # le nom du fichier HTML se compose à partir du nom de noeud ;
    # le nom du noeud est censé être unique dans le graphe
    nom_fichier=os.path.join(path, f"page_{node}.html")
    
    liste_boutons=[]
    liste_scripts=[]
    for e in edges:
        if e[0] == node:
            # il s'agit d'un lien sortant de la page
            label=e.attr["label"].replace("\\n", "<br/>")
            liste_boutons.append(f"""\
      <li><a href="page_{e[1]}.html" class="bouton">{label}</a></li>
""")
            # si timeout est défini, on lance un chronomètre
            # pour changer de page, en langage Javascript
            if e.attr["timeout"]:
                t=float(e.attr["timeout"])
                liste_scripts.append(f"""\
<script type="text/javascript">
  setTimeout(function(){{ window.location.replace("page_{e[1]}.html"); }}, 1000*{t});
</script>""")
    boutons="".join(liste_boutons)
    scripts="".join(liste_scripts)
    
    with open(nom_fichier, "w") as sortie:
        label=node.attr["label"].replace("\\n", "<br/>")
        sortie.write(f"""\
<html>
  <head>
    <title>Page générée pour le nœud {node}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style type="text/css">
    ul {{
      list-style-type: none;
      text-align: center;
    }}
    ul li {{
      display: inline-block;
      text-align: center;
    }}
    ul li a {{
      display: inline-block;
      text-decoration: none;
      background-color: #EEEEEE;
      color: #333333;
      padding: 2px 6px 2px 6px;
      border-top: 1px solid #CCCCCC;
      border-right: 1px solid #333333;
      border-bottom: 1px solid #333333;
      border-left: 1px solid #CCCCCC;
      margin: 5px;
      text-align: center;
    }}
    </style>
  </head>
  <body><center>
    <h1>{label}</h1>
    <img src="{node.attr["image"]}" alt="image principale"/>
    <ul>
    {boutons}
    </ul>
    {scripts}
  </center></body>
</html>
""")
    
    
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

noeuds=list(A.nodes_iter())
liens=list(A.edges_iter())

for n in noeuds:
    cree_html(n, liens)
