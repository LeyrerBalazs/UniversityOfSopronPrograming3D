from OpenGL.GL import *
from OpenGL.GLU import *

class Light:
    def __init__(self, shader):
        self.x, self.y, self.z = -10.0, 0.0, 0.0
        self.leftToRight, self.downToUp = True, True
        self.__giveLightDataToVertex(shader)

    def lightPos(self) -> None:
        """Ez állítja be a Fény mozgó Pozicíóját.
        Args:
            lx (float): Fény x koordináta.
            ly (float): Fény x koordináta.
            leftToRight (bool): Balról megy jobbra.
            downToUp (bool): Lentről megy fel.
        Returns:
            lx (float): Fény x koordináta.
            ly (float): Fény x koordináta.
            leftToRight (bool): Balról megy jobbra.
            downToUp (bool): Lentről megy fel."""
        if int(self.x) == 10.0:
            self.leftToRight = False
        elif int(self.x) == -10.0:
            self.leftToRight= True
        if int(self.y) == 10:
            self.downToUp = False
        elif int(self.y) == -10.0:
            self.downToUp= True
        if self.leftToRight == True:
            self.x += 0.1
        elif self.leftToRight == False:
            self.x -= 0.1
        if self.downToUp == True:
            self.y += 0.1
        elif self.downToUp == False:
            self.y -= 0.1
    
    def __giveLightDataToVertex(self, shader):
        glUniform3f(glGetUniformLocation(shader, 'lightPos'), self.x, self.y, self.z)