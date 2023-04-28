# Importok:

# Python modul importok:

from OpenGL.GL import *


# Osztályok:

class Light:
    """Fény.
    """

    def __init__(self, shader):
        """Konstruktor.

        Args:
            shader (ShaderProgram): Shader adat.
        """
        
        self.x, self.y, self.z = -10.0, 0.0, 0.0
        self.leftToRight, self.downToUp = True, True
        self.__giveLightDataToVertex(shader)


    # Belső függvények:

    def __giveLightDataToVertex(self, shader):
        """Adatok odaadása a './vertex_shader.vert' számára.

        Args:
            shader (ShaderProgram): Shader adat.
        """

        glUniform3f(glGetUniformLocation(shader, 'lightPos'), self.x, self.y, self.z)


    # Külső függvények:

    def lightPos(self) -> None:
        """A fény pozíciójának 45-fokban döntött pozícióval.
        """

        # Döntés hozás, merre menjen:

        if int(self.x) == 10.0:
            self.leftToRight = False
        elif int(self.x) == -10.0:
            self.leftToRight= True
        if int(self.y) == 10:
            self.downToUp = False
        elif int(self.y) == -10.0:
            self.downToUp= True


        # Fény koordinátáinak áthelyezése, fény mozgása:

        if self.leftToRight == True:
            self.x += 0.1
        elif self.leftToRight == False:
            self.x -= 0.1
        if self.downToUp == True:
            self.y += 0.1
        elif self.downToUp == False:
            self.y -= 0.1