from OpenGL.GL import *

class Character:
    def __init__(self, shader):
        self.x = 0.0
        self.y = 2.0
        self.z = 0.0
        self.__giveCharacterDatasToVertex(shader)
    
    def __giveCharacterDatasToVertex(self, shader):
        glUniform3f(glGetUniformLocation(shader, 'viewPos'), self.x, self.y, self.z)