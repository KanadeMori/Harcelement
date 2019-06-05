
import pygraphviz as pgv
from PIL import Image
import re, os

def cree_svg(A, target='mongraphe.svg', maxImgSize=100):
    """
    Pour commencer on fait une copie du graphe A, puis on examine
    les fichiers images ; s'ils sont absents on met une petite image
    par défaut pour signaler le manque ; sinon s'ils sont trop grands
    on crée une miniature dans le sous-répertoire mini/ qu'on substitue
    à l'image d'origine
    """
    # on exporte le Agraph sous forme d'une liste de lignes de code DOT
    # 
    image_pattern=re.compile(r'(.*)image="(.*)"(.*)')
    Adot = A.to_string().split("\n");
    A=pgv.AGraph(directed=True).from_string("\n".join(Adot))
    for n in A.nodes_iter():
        print(dir(n))
    """
    for i in range(len(Adot)):
        m=image_pattern.match(Adot[i])
        newsize=None
        if m:
            #on a détecté une image
            imgPath=m.group(2)
            if os.path.exists(imgPath):
                img=Image.open(imgPath)
                print(imgPath, img.size)
                if img.size[0] > maxImgSize:
                    facteur=maxImgSize/img.size[0]
                    newsize=(int(img.size[0]*facteur), int(img.size[1]*facteur))
                elif img.size[1] > maxImgSize:
                    facteur=maxImgSize/img.size[1]
                    newsize=(int(img.size[0]*facteur), int(img.size[1]*facteur))
                print("newsize =", newsize)
                if newsize != None:
                    img=img.resize(newsize)
                    directory = os.path.dirname(imgPath)
                    basename  = os.path.basename(imgPath)
                    destdir=os.path.join("mini", directory)
                    os.makedirs(destdir, exist_ok=True)
                    newPath=os.path.join(destdir, basename)
                    img.save(newPath)
                    print("Miniature en", newPath)
                    Adot[i]=f'{m.group(1)}image="{newPath}"{m.group(3)}'
            else:
                print(imgPath, ": pas d'image")
                pass
    A=pgv.AGraph(directed=True).from_string("\n".join(Adot))
    print(A.to_string())
    A.layout(prog="dot") # mise en forme graphique
    A.draw(target)
    """
    return
