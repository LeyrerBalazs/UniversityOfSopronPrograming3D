from objects.cube import Cube
from functions.lighting import Light
import random
import numpy as np
from OpenGL.GL import *

class World:
    def __init__(self, number:int, shader) -> None:
        self.cubesCount = 0
        self.cubes, self.VBOs = [], []
        self.__generateTerrain(number)
        self.light = Light(shader)
    
    def __generateTerrain(self, widthXheight:int):
        """Ez a függvény felelős létrehozni az alap területet.
        Args:
            widthXheight (int): Egy szám amely megadja, hogy hányszór hányas a platform."""
        for x in range(int(-1 * (widthXheight/2)), int(widthXheight/2), 1):
            for z in range(int(-1 * (widthXheight/2)), int(widthXheight/2), 1):
                for y in range(-3, 3, 1):
                    if y < 1:
                        c = Cube([x,y,z],[random.uniform(0.00,255.00),random.uniform(0.00,1.00),random.uniform(0.00,1.00)])
                        self.__saveCube(c)
                    elif y == 1 and random.randint(1,100) < 65 and (x > 2 or x < -2 or z > 2 or z < -2):
                        c = Cube([x,y,z],[random.uniform(0.00,255.00),random.uniform(0.00,1.00),random.uniform(0.00,1.00)])  
                        self.__saveCube(c)
                    elif y == 2 and random.randint(1,100) < 40  and (x > 2 or x < -2 or z > 2 or z < -2):
                        c = Cube([x,y,z],[random.uniform(0.00,255.00),random.uniform(0.00,1.00),random.uniform(0.00,1.00)])  
                        self.__saveCube(c)
    
    def __saveCube(self, c:Cube):
        self.cubes.append(c)
        rectangle = np.array(c.vertPoints, dtype=np.float32)
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, rectangle.nbytes, rectangle, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        self.VBOs.append(VBO)
        self.cubesCount += 1
    
    def drawObjects(self) -> None:
        """Ezt a fügvényt hívja meg a végtelen ciklus és ez törli az előzőt és rajzolja ki az objektumokat újra."""
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for i in range(self.cubesCount):
            glBindBuffer(GL_ARRAY_BUFFER, self.VBOs[i])
            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, None)
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
            glDrawArrays(GL_QUADS, 0, self.cubes[i].vertCounts)
            glDisableVertexAttribArray(0)
            glDisableVertexAttribArray(1)