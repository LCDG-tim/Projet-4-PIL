# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""
with PIL.Image.open("path.ext") as img:
    img.resize((x, y)) # reformate img au format (x, y)
    img.save("path.ext") # sauvegarde le fichier avec le chemin et l'extension
    # donnée
    img.convert("mode") # change mode de l'image : RGB, RGBA, L(Noir et Blanc)
    img.rotate(a) # effectue une rotation de a° dans le sens anti-horair
    PIL.ImageOps.miror(img) # renvoie l'image avec la gauche à droite et la
    # droite à gauche
    PIL.ImageOps.flip(img) # revoie l'image retourner
    img.copy() # créer une copie
    PIL.ImageDraw.Draw(img).rectanle([(x1, y1), (x2, y2)]) # dessine un
    # rectangle de coordonnée x1, y1 pour le point en haut à gauche et x2, y2
    # pour le point en bas à droite
    PIL.ImageOps.expand(bird, border=a, fill="color") # agrandi l'image de a
    # pixels à gauche droite haut bas et rempli la zone de la couleur mise à la
    # place de color
    img.crop((a, b, c, d)) # rogne l'image tel que a est l'abscisse axe gauche,
    # b est l'ordonné de l'axe haut, c est l'abscisse de l'axe droite, d est
    # l'ordonné de l'axe en bas de la nouvelle image
    # changer la lumineusité
    img = PIL.ImageEnhance.Brightness(img).enhance(a) # a est une valeur
    # placer un filtre EMBOSS, BLUR, CONTOUR, DETAIL, EDGE_ENHANCE,
    # EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH_MORE, SHARPEN
    img = img.filter(ImageFilter.EMBOSS)

# afficher une image sur une autre
# le programme charge les deux image
img1 = PIL.Image.open("path.ext")
img2 = PIL.Image.open("path.ext")
# affichage de l'image 2 sur l'image 1
img1.paste(img, (x, y)) # (x, y) sont les coordonnés du point en haut à gauche
# de l'endroit de où sera coller l'image 2

"""


import PIL


with PIL.Image.open("images/13-photo.jpg") as IMAGE:
    img = IMAGE.copy()
    # renvoie l'image avec la gauche à droite et la droite à gauche
    PIL.ImageOps.mirror(img).show()
    # revoie l'image retourner
    PIL.ImageOps.flip(img).show()
    print(type(img))
    IMAGE.show()
