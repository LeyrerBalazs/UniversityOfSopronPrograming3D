from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
from objects.cube import Cube
import pyrr
import math
import random
from functions.glfwFunctions import *

def saveCube(c:Cube, cubes:list, count:int, VBOs:list):
    cubes.append(c)
    rectangle = np.array(c.vertPoints, dtype=np.float32)
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, rectangle.nbytes, rectangle, GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    VBOs.append(VBO)
    count += 1
    return cubes, count, VBOs


def generateTerrain(widthXheight:int):
    """Ez a függvény felelős létrehozni az alap területet.
    Args:
        widthXheight (int): Egy szám amely megadja, hogy hányszór hányas a platform.
    Returns:
        count (int): Hány darab Cube objektum jött létre.
        cubes (list): Lista amely tartalmazza a Cube példányokat.
        VBOs (list): Vertex Buffer Objectum-ok."""
    count = 0
    cubes, VBOs = [], []
    for x in range(int(-1 * (widthXheight/2)), int(widthXheight/2), 1):
        for z in range(int(-1 * (widthXheight/2)), int(widthXheight/2), 1):
            for y in range(-3, 3, 1):
                if y < 1:
                    c = Cube([x,y,z],[random.uniform(0.00,255.00),random.uniform(0.00,1.00),random.uniform(0.00,1.00)])
                    cubes, count, VBOs = saveCube(c, cubes, count, VBOs)
                elif y == 1 and random.randint(1,100) < 65 and (x > 1.5 or x < -1.5 or z > 1.5 or z < -1.5):
                    c = Cube([x,y,z],[random.uniform(0.00,255.00),random.uniform(0.00,1.00),random.uniform(0.00,1.00)])  
                    cubes, count, VBOs = saveCube(c, cubes, count, VBOs)
                elif y == 2 and random.randint(1,100) < 40  and (x > 1.5 or x < -1.5 or z > 1.5 or z < -1.5):
                    c = Cube([x,y,z],[random.uniform(0.00,255.00),random.uniform(0.00,1.00),random.uniform(0.00,1.00)])  
                    cubes, count, VBOs = saveCube(c, cubes, count, VBOs)
    return count, cubes, VBOs

def readShaderFile(filename:str) -> str:
    """Shader fájl beolvasás.
    Args:
        filename (str): Fájl neve.
    Returns:
        str: Fájl tartalma."""
    with open(filename) as f:
	    return f.read()
    
def drawObjects(count:int, cubes:list, VBOs:list) -> None:
    """Ezt a fügvényt hívja meg a végtelen ciklus és ez törli az előzőt és rajzolja ki az objektumokat újra.
    Args:
        count (int): Hány darab Cube-ot kell kirajzolnia.
        cubes (list): A Cubo-k adatai.
        VBOs (list): Vertex Buffer Objectum-ok."""
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for i in range(count):
        glBindBuffer(GL_ARRAY_BUFFER, VBOs[i])
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, None)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glDrawArrays(GL_QUADS, 0, cubes[i].vertCounts)
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)

def makePerspectiveMatrix(shader):
    """Ez a függvény felelős létrehozni a pyrr perspectívmátrixot.
    Args:
        shader: Shader Program adatok.
    Returns:
        Késöbbiekben szükséges adatok."""
    transformMatrix = glGetUniformLocation(shader, "modelView")
    perspectiveMatrix = glGetUniformLocation(shader, "perspectiveMatrix")
    perspMatrix = pyrr.matrix44.create_perspective_projection_matrix(45.0, 1280.0 / 720.0, 0.1, 1000.0)
    return transformMatrix, perspectiveMatrix, perspMatrix

def perspectiveMatrixMath(angle):
    """Ez számolja ki a perspektív mátrix értékeit.
    Args:
        angle (float): Szög.
    Returns:
        Késöbb szükséges adat."""
    transMat = pyrr.matrix44.create_from_translation(  pyrr.Vector3([0.0, 0.0, -60.0]))
    rotMat = pyrr.matrix44.create_from_axis_rotation(pyrr.Vector3([1., 1., 1.0]), math.radians(angle))
    return pyrr.matrix44.multiply(rotMat, transMat)

def giveDatasForVertex(angle, shader, lx:float,ly:float, lz:float) -> None:
    """Átad minden szükséges adatot a ./../shaders/vertex_shader.vert-nek.
    Args:
        angle (float): Szög.
        shader: Shader Program adatok.
        lx (float): Fény x koordinátája.
        ly (float): Fény y koordinátája.
        lz (float): Fény z koordinátája."""
    transformMatrix, perspectiveMatrix, perspMatrix = makePerspectiveMatrix(shader)
    matrix = perspectiveMatrixMath(angle)
    glUniformMatrix4fv(transformMatrix, 1, GL_FALSE, matrix )
    glUniformMatrix4fv(perspectiveMatrix, 1, GL_FALSE, perspMatrix )
    glUniform3f(glGetUniformLocation(shader, 'lightPos'), lx, ly, lz)

def loadShaders():
    """Shaderek beolvasása és Shader Program létrehozása.
    Returns:
        shader: Visszad egy shader program adatokat."""
    return OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(readShaderFile("shaders/vertex_shader.vert"), GL_VERTEX_SHADER), OpenGL.GL.shaders.compileShader(readShaderFile("shaders/fragment_shader.frag"), GL_FRAGMENT_SHADER))

def setDatas(number:int):
    """Beállítja a PyOpenGL beállításokat a window-ra.
    Args:
        number (int): Mekkora legyen a platform.
    Returns:
        window (glfw)
        count (int): Hány darab Cube-ot kell kirajzolnia.
        cubes (list): A Cubo-k adatai.
        VBOs (list): Vertex Buffer Objectum-ok.
        shader: Shader Program adatok.
        angle (float): Szög.
        elapsedTime (float): Elipszis idő."""
    window = createGLFWwindow()
    count, cubes, VBOs = generateTerrain(number)
    shader = loadShaders()
    glUseProgram(shader)
    glEnable(GL_DEPTH_TEST)
    return window, count, cubes, VBOs, shader, 0.0, 0.0


