# Importok:

# Python modul importok:

import random
import numpy as np
from OpenGL.GL import *

#Egyedi Python modul importok:

from objects.cube import Cube
from functions.camera import Camera
from functions.lighting import Light
from functions.texture import Texture


# Osztályok:

class World:
    """Világ.
    """

    def __init__(self, number:int, shader) -> None:
        """Konstruktor

        Args:
            number (int): Terület mérete.
            shader (ShaderProgram): Shader adat.
        """
        self.cubesCount = 0
        self.cubes, self.VBOs = [], []
        self.__generateTerrain(number)
        self.light = Light(shader)
        self.texture = Texture()
        self.camera = Camera(shader)
    
    # Belső függvények

    def __generateTerrain(self, size:int) -> None:
        """Terület legenárálása és spawnpoint kihagyása a domborzatból.

        Args:
            size (int): Terület mérete (Négyzet forma oldalhossza).
        """
        for x in range(int(-1 * (size/2)), int(size/2), 1):
            for z in range(int(-1 * (size/2)), int(size/2), 1):
                for y in range(-3, 3, 1):
                    if y < 1:
                        self.__saveCube([x, y, z])
                    elif y == 1 and random.randint(1,100) < 65 and (x > 2 or x < -2 or z > 2 or z < -2):
                        self.__saveCube([x, y, z])
                    elif y == 2 and random.randint(1,100) < 40  and (x > 2 or x < -2 or z > 2 or z < -2):
                        self.__saveCube([x, y, z])
    
    def __saveCube(self, coords:list) -> None:
        """"Generált kocka elmentése.

        Args:
            coords (list): X, y, z koordináták
        """
        c = Cube(coords,[0,0,0])
        self.cubes.append(c)
        rectangle = np.array(c.vertPoints, dtype=np.float32)
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, rectangle.nbytes, rectangle, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        self.VBOs.append(VBO)
        self.cubesCount += 1
    

    # Külső függvények

    def drawObjects(self, camera, cameraMatrix) -> None:
        """Világ kirajzolása.

        Args:
            camera (Camera): Kamera osztálypéldány.
            cameraMatrix (any): Kamera mátrix adatai.
        """
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for i in range(self.cubesCount):
            glBindBuffer(GL_ARRAY_BUFFER, self.VBOs[i])
            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, None)
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
            glEnableVertexAttribArray(2)
            glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))
            glEnableVertexAttribArray(2)
            glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))
            camera.apply(cameraMatrix)
            glBindTexture(GL_TEXTURE_2D, self.texture.texture)
            glDrawArrays(GL_QUADS, 0, self.cubes[i].vertCounts)
            glDisableVertexAttribArray(0)
            glDisableVertexAttribArray(1)
            glDisableVertexAttribArray(2)