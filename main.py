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


def traitement_d_image(origin_image: PIL.Image.Image,
                       flipped: bool = False,
                       mirror: bool = False,
                       grey_nuance: bool = False,
                       negate: bool = False) -> PIL.Image.Image:
    """fonction qui fait les changements d'image que tu veux
    ----
    :pre:
        - origin_image est une instance de PIL.Image.Image
        - flipped est un bool
        - mirror est un bool
        - grey_nuance est un bool
        - negate est un bool
    :post:
        - new_img est une instance de PIL.Image.Image
    """

    # Assertion pre
    assert isinstance(origin_image, PIL.Image.Image), \
        "origin_image must be a instance of PIL.Image.Image, not {}" \
        .format(type(origin_image))
    assert isinstance(flipped, bool), \
        "flipped must be a bool, not {}".format(type(flipped))
    assert isinstance(mirror, bool), \
        "mirror must be a bool, not {}".format(type(mirror))
    assert isinstance(grey_nuance, bool), \
        "grey_nuance must be a bool, not {}".format(type(grey_nuance))
    assert isinstance(negate, bool), \
        "negate must be a bool, not {}".format(type(negate))

    def valeur_gris(a: tuple) -> int:
        """fonction qui retourne la valeur de gris en fonction de la couleur du
        pixel en faisant la moyenne des trois intensité
        ----
        :pre:
            - a est un tuple de 3 int
        :post:
            - grey est un int
        """

        # Asertion pre
        assert isinstance(a, tuple), \
            "a must be a tuple, not {}".format(type(a))
        assert len(a) == 3, \
            "a must contain 3 elements, not {}".format(len(a))
        for j, i in enumerate(a):
            assert isinstance(i, int), \
                "l'element {} must be a int, not {}".format(j, type(i))

        grey = (a[0] + a[1] + a[2]) // 3

        # Assertion post
        assert isinstance(grey, int), \
            "grey must be a int, not {}".format(type(grey))

        return grey

    # le programme récupère la définition de l'image d'origin
    width, height = origin_image.size

    # le programme crée une nouvelle image de la même définition de celle
    # d'origine son mode est soit RGB soit L selon le fait que grey_nuance
    # soit True ou False
    # le programme utilise une condition ternaire, schéma ci-dessous:
    # (valeur_si_False, valeur_si_True)[condition]
    # attention, il faut que les deux valeurs soientt possible avant la
    # condition
    new_img = PIL.Image.new(("RGB", "L")[grey_nuance], (width, height))

    for x in range(width):
        for y in range(height):
            # calcul de la couleur du nouveau pixel
            couleur = origin_image.getpixel((x, y))
            if negate:
                couleur = tuple(255 - i for i in origin_image.getpixel((x, y)))
            if grey_nuance:
                couleur = valeur_gris(couleur)
            position_x = (x, width - 1 - x)[mirror]
            position_y = (y, height - 1 - y)[flipped]
            position = (position_x, position_y)
            new_img.putpixel(position, couleur)

    # Assertion post
    assert isinstance(new_img, PIL.Image.Image), \
        "new_img must be a instance of PIL.Image.Image, not {}"\
        .format(type(new_img))

    return new_img


IMAGE = PIL.Image.open("images/13-photo.jpg")
# IMAGE.show()

"""
# revoie l'image retourner
IMAGE2 = symetrie_horizontale(IMAGE)
IMAGE2.show()

# renvoie l'image avec la gauche à droite et la droite à gauche
IMAGE3 = symetrie_vertical(IMAGE)
IMAGE3.show()
"""

img2 = traitement_d_image(IMAGE, mirror=True)
img2.save("images/img2.jpg")
