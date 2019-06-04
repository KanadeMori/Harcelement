
from copy import deepcopy
import PIL

def cree_svg(A, target='mongraphe.svg'):
	"""
	Pour commencer on fait une copie du graphe A, puis on examine
	les fichiers images ; s'ils sont absents on met une petite image
	par défaut pour signaler le manque ; sinon s'ils sont trop grands
	on crée une miniature dans le sous-répertoire mini/ qu'on substitue
	à l'image d'origine
	"""
	A=deepcopy(A)
	for n in A.nodes_iter():
		print(dir(n))
	A.layout(prog="dot") # mise en forme graphique
	A.draw(target)
