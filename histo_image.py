# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

import matplotlib.pyplot as plt


import PIL


class Y_graph:

    def __init__(self, name):
        """constructeur de la classe
        ----
        :pre:
            - name est un str
        """

        # Assertion pre
        assert isinstance(name, str), \
            "name must be a str, not {}".format(type(name))

        self.name = name
        self.y = [0] * 256

    def get_name(self) -> str:
        """fonction qui retourne le nom donné a l'object
        ----
        :post:
            - self.names est un str
        """

        # Assertion post
        assert isinstance(self.name, str), \
            "self.name must be a str, not {}".format(type(self.name))

        return self.name

    def get_y(self) -> list:
        """fonction qui retourne la liste y
        ----
        :post:
            - self.y est une liste
        """

        # Assertion post
        assert isinstance(self.y, list), \
            "self.y must be a list, not {}".format(type(self.y))

        return self.y

    def accrement(self, rang: int) -> None:
        """ajoute 1 à l'élément du rang donné en argument
        ----
        :pre:
            - rang est un int compris entre 0 et 255 inclus
        """

        # Assertions pre
        assert isinstance(rang, int), \
            "rang must be a int, not {}".format(type(rang))
        assert 0 <= rang <= 255, \
            "rang must be include in [0: 255], not {}".format(rang)

        self.y[rang] += 1


def histo_img(origin_image: PIL.Image.Image):
    """fonction qui retourne les histogrammes de luminosité et d'intesité des
    couleurs
    ----
    :pre:
        - origin_image est une instance de PIL.Image.Image
    """

    # Assertion pre
    assert isinstance(origin_image, PIL.Image.Image), \
        "origin_image must be a instance of PIL.Image.Image, not {}" \
        .format(type(origin_image))

    x_graph = [i for i in range(256)]
    y_brightness = Y_graph("brightness")
    y_red_graph = Y_graph("red graph")
    y_green_graph = Y_graph("green graph")
    y_blue_graph = Y_graph("blue graph")

    width, height = origin_image.size
    for x in range(width):
        for y in range(height):
            R, G, B = origin_image.getpixel((x, y))
            GRIS = (R + G + B) // 3
            y_brightness.accrement(GRIS)
            y_red_graph.accrement(R)
            y_green_graph.accrement(G)
            y_blue_graph.accrement(B)

    # graphiques
    plt.plot(
        x_graph,
        y_brightness.get_y(),
        color='grey',
        label=y_brightness.get_name()
    )
    plt.legend()
    plt.show()
    plt.plot(
        x_graph,
        y_red_graph.get_y(),
        color='red',
        label=y_red_graph.get_name()
    )
    plt.legend()
    plt.show()
    plt.plot(
        x_graph,
        y_green_graph.get_y(),
        color='green',
        label=y_green_graph.get_name()
    )
    plt.legend()
    plt.show()
    plt.plot(
        x_graph,
        y_blue_graph.get_y(),
        color='blue',
        label=y_blue_graph.get_name()
    )
    plt.legend()
    plt.show()


IMAGE = PIL.Image.open("images/13-photo.jpg")
histo_img(IMAGE)
