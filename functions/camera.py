# Importok:

# Python modul importok:

import math
import pyrr
from OpenGL.GL import *


# Osztályok:

class Camera:
    """Kamera.
    """

    def __init__(self, shader) -> None:
        """Konstruktor.

        Args:
            shader (ShaderProgram): Shader adat.
        """

        self.x, self.y, self.z = 0, 2.5, -60
        self.dirX, self.dirY, self.dirZ = 10, 0, -1
        self.angleVert, self.angleHoriz = -90.0, 0.0
        self.__giveCameraDataToVertex(shader)
        pass


    # Belső függvények:

    def __giveCameraDataToVertex(self, shader) -> None:
        """Adatok odaadása a './vertex_shader.vert' számára.

        Args:
            shader (ShaderProgram): Shader adat.
        """

        glUniform3f(glGetUniformLocation(shader, 'viewPos'), self.x, self.y, self.z)
        pass

    def __update(self) -> None:
        """Kamera frissitése
        """

        self.dirX = math.cos(math.radians(self.angleVert))
        self.dirZ = math.sin(math.radians(self.angleVert))
        self.dirY = math.sin(math.radians(self.angleHoriz))
        length = math.sqrt(self.dirX ** 2 + self.dirY ** 2 + self.dirZ ** 2)
        self.dirX /= length
        self.dirY /= length
        self.dirZ /= length
        pass


    # Külső függvények

    def move(self, dist) -> None:
        """Kamera mozgás.

        Args:
            dist (float): Mozgás értéke.
        """

        self.x += self.dirX * dist
        self.y += self.dirY * dist
        self.z += self.dirZ * dist
        pass

    def rotateUpDown(self, movement) -> None:
        """Kamera forgás az y, z tengely menten, az x tengely körül. -45 és 45 fok között.

        Args:
            movement (float): Mozgás értéke.
        """

        self.angleHoriz += movement
        self.angleHoriz = min(45.0, max(-45.0, self.angleHoriz))
        self.__update()

    def rotateRightLeft(self, movement) -> None:
        """Kamerat forgatása az x, z tengely menten, az y tengely körül.

        Args:
            movement (float): Mozgás értéke.
        """

        self.angleVert += movement
        self.__update()

    def apply(self, cameraMatrix) -> None:
        """Atadja az OpenGL-nek a kamera beallitasait.

        Args:
            cameraMatrix (any): Kamera mátrix adatati.
        """
        
        transMat = pyrr.matrix44.create_look_at(pyrr.Vector3([self.x, self.y, self.z]), pyrr.Vector3([self.x + self.dirX, self.y + self.dirY, self.z + self.dirZ]), pyrr.Vector3([0.0, 1.0, 0.0]))
        glUniformMatrix4fv(cameraMatrix, 1, GL_FALSE, transMat)