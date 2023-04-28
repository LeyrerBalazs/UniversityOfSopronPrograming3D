from OpenGL.GL import *
import math
import pyrr

class Camera:
    def __init__(self, shader):
        self.x = 0
        self.y = 2.5
        self.z = -60
        self.dirX = 10
        self.dirY = 0
        self.dirZ = -1
        self.angleVert = -90.0
        self.angleHoriz = 0.0
        self.__giveCameraDataToVertex(shader)

    def __giveCameraDataToVertex(self, shader):
        glUniform3f(glGetUniformLocation(shader, 'viewPos'), self.x, self.y, self.z)

    def move(self, dist):
        """!
            Az kamera aktualis iranyanak megfelelo iranyba mozditja el a kamerat.
            @param dist: Azt adja meg, hogy az iranyvektor hanyszorosaval mozduljunk el.
        """
        self.x += self.dirX * dist
        self.y += self.dirY * dist
        self.z += self.dirZ * dist

    def __update(self):
        self.dirX = math.cos(math.radians(self.angleVert))
        self.dirZ = math.sin(math.radians(self.angleVert))
        self.dirY = math.sin(math.radians(self.angleHoriz))
        length = math.sqrt(self.dirX ** 2 + self.dirY ** 2 + self.dirZ ** 2)
        self.dirX /= length
        self.dirY /= length
        self.dirZ /= length

    def rotateUpDown(self, movement):
        """!
            A kamerat forgatja el az yz sik menten, az x tengely korul. Ugyel arra, hogy -45 és 45
            fok kozott maradjunk, ne tudjunk 'hatrabukfencet' csinalni.
        """
        self.angleHoriz += movement
        self.angleHoriz = min(45.0, max(-45.0, self.angleHoriz))
        self.__update()

    def rotateRightLeft(self, movement):
        """!
            A kamerat forgatja el az xz sik menten, az y tengely korul.
        """
        self.angleVert += movement
        self.__update()

    def apply(self, cameraMatrix):
        """!
            Atadja az OpenGL-nek a kamera beallitasait.
        """
        transMat = pyrr.matrix44.create_look_at(
            pyrr.Vector3([self.x, self.y, self.z]), 
            pyrr.Vector3([self.x + self.dirX, self.y + self.dirY, self.z + self.dirZ]), 
            pyrr.Vector3([0.0, 1.0, 0.0]))
        glUniformMatrix4fv(cameraMatrix, 1, GL_FALSE, transMat)