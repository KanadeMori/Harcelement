
import pygraphviz as pgv
from PIL import Image, ImageFont, ImageDraw
import re, os, subprocess

def cree_svg(A, target='mongraphe.svg', maxImgSize=100):
    """
    Pour commencer on fait une copie du graphe A, puis on examine
    les fichiers images ; s'ils sont absents on met une petite image
    par défaut pour signaler le manque ; sinon s'ils sont trop grands
    on crée une miniature dans le sous-répertoire mini/ qu'on substitue
    à l'image d'origine
    """
    # effacement du répertoire missing/ des images manquantes
    # et du répertoire mini/ des miniatures
    subprocess.call("rm -rf missing/*", shell=True)
    subprocess.call("rm -rf mini/*", shell=True)
    
    # on exporte le Agraph sous forme d'une liste de lignes de code DOT
    # et on le relit, ce qui revient à en faire une copie profonde
    Adot = A.to_string().split("\n");
    A=pgv.AGraph(directed=True).from_string("\n".join(Adot))
    
    for n in A.nodes_iter():
        newsize=None
        if "image" in n.attr.keys():
            imgPath=n.attr["image"]
            directory = os.path.dirname(imgPath)
            basename  = os.path.basename(imgPath)
            if os.path.exists(imgPath):
                img=Image.open(imgPath)
                if img.size[0] > maxImgSize:
                    facteur=maxImgSize/img.size[0]
                    newsize=(int(img.size[0]*facteur), int(img.size[1]*facteur))
                elif img.size[1] > maxImgSize:
                    facteur=maxImgSize/img.size[1]
                    newsize=(int(img.size[0]*facteur), int(img.size[1]*facteur))
                if newsize != None:
                    img=img.resize(newsize)
                    destdir=os.path.join("mini", directory)
                    os.makedirs(destdir, exist_ok=True)
                    newPath=os.path.join(destdir, basename)
                    img.save(newPath)
                    n.attr["image"]=newPath
            else:
                font = ImageFont.truetype("sans-serif.ttf", 12)
                color=(240,0,240)
                img=Image.open("missing.jpg")
                draw = ImageDraw.Draw(img)
                draw.text((0, 0),"Image manquante",color,font=font)
                draw.text((0, 26),basename,color,font=font)
                destdir=os.path.join("missing", directory)
                os.makedirs(destdir, exist_ok=True)
                newPath=os.path.join(destdir, basename)
                img.save(newPath)
                n.attr["image"]=newPath
    A.layout(prog="dot") # mise en forme graphique
    A.draw(target)           
    return
