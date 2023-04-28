# Importok:

# Python modul importok:

from PIL import Image
from OpenGL.GL import *


# Osztályok:

class Texture:
    """Textura kezelő osztály.
    """

    def __init__(self):
        """Konstruktor.
        """

        self.texture = self.__createTexture()

    # Belső függvények:

    def __createTexture(self):
        """Létrehozza a texturát.

        Returns:
            any: Visszadja a texturát.
        """
        
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = Image.open("./image/dirt.png")
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        glBindTexture(GL_TEXTURE_2D, 0)
        return texture