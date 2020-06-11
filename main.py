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


def symetrie_vertical(img: PIL.Image.Image) -> PIL.Image.Image:
    """fonction qui retourne l'image symetrique par un axe vertical
    """

    assert isinstance(img, PIL.Image.Image), "img not in goog format"

    longueur, hauteur = img.size
    new_img = PIL.Image.new("RGB", (longueur, hauteur))

    for x in range(longueur):
        for y in range(hauteur):
            new_img.putpixel((longueur - 1 - x, y), img.getpixel((x, y)))

    assert isinstance(new_img, PIL.Image.Image), "new_img not in good format"

    return new_img


def symetrie_horizontale(img: PIL.Image.Image) -> PIL.Image.Image:
    """fonction qui retourne l'image symetrique par un axe hrizontal
    """

    assert isinstance(img, PIL.Image.Image), "img not in goog format"

    longueur, hauteur = img.size
    new_img = PIL.Image.new("RGB", (longueur, hauteur))
    for x in range(longueur):
        for y in range(hauteur):
            new_img.putpixel((x, hauteur - 1 - y), img.getpixel((x, y)))

    assert isinstance(new_img, PIL.Image.Image), "new_img not in good format"

    return new_img


IMAGE = PIL.Image.open("images/13-photo.jpg")
# IMAGE.show()

# revoie l'image retourner
# re.flip(IMAGE).show()
IMAGE2 = symetrie_horizontale(IMAGE)
IMAGE2.show()

# renvoie l'image avec la gauche à droite et la droite à gauche
# re.mirror(IMAGE).show()
IMAGE3 = symetrie_vertical(IMAGE)
IMAGE3.show()
