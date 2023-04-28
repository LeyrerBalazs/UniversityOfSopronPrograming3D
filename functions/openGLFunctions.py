# Importok:

# Python modul importok:

import pyrr
import math
from OpenGL.GL import *
import OpenGL.GL.shaders

#Egyedi Python modul importok:

from functions.glfwFunctions import *
from functions.world import World


# Függvények:

def readFile(filePath:str) -> str:
    """Beolvassa a fájl tartalmát.

    Args:
        filePath (str): Fájl útvonala és neve.

    Returns:
        str: Fájl tartalom.
    """

    with open(filePath) as f:
	    return f.read()
    
def makePerspectiveMatrix(shader):
    """Ez hozza létre a pyrr perspektív mátrixot.

    Args:
        shader (ShaderProgram): Shader adat.

    Returns:
        any: Késöbbiekben felhasznált adatok.
    """

    transformMatrix = glGetUniformLocation(shader, "modelView")
    perspectiveMatrix = glGetUniformLocation(shader, "perspectiveMatrix")
    perspMatrix = pyrr.matrix44.create_perspective_projection_matrix(45.0, 1280.0 / 720.0, 0.1, 1000.0)
    return transformMatrix, perspectiveMatrix, perspMatrix

def perspectiveMatrixMath(angle):
    """Ez számolja ki a perspektívmátrix-ot.

    Args:
        angle (float): Látószög.

    Returns:
        any : Perspektív mátrix számai.
    """

    transMat = pyrr.matrix44.create_from_translation(  pyrr.Vector3([0.0, 0.0, -60.0]))
    rotMat = pyrr.matrix44.create_from_axis_rotation(pyrr.Vector3([1., 1., 1.0]), math.radians(angle))
    return pyrr.matrix44.multiply(rotMat, transMat)

def giveDatasForVertex(angle, shader) -> None:
    """Adatok odaadása a './vertex_shader.vert' számára.

    Args:
        angle (float): Ltószög.
        shader (ShaderProgram): Shader adat.
    """

    transformMatrix, perspectiveMatrix, perspMatrix = makePerspectiveMatrix(shader)
    matrix = perspectiveMatrixMath(angle)
    glUniformMatrix4fv(transformMatrix, 1, GL_FALSE, matrix )
    glUniformMatrix4fv(perspectiveMatrix, 1, GL_FALSE, perspMatrix )
    
def makeShader():
    """Létrehozza a shader programot

    Returns:
        ShaderProgram: Shader adat.
    """

    return OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(readFile("shaders/vertex_shader.vert"), GL_VERTEX_SHADER), OpenGL.GL.shaders.compileShader(readFile("shaders/fragment_shader.frag"), GL_FRAGMENT_SHADER))

def setDatas(number:int):
    """Adatok beállítása.

    Args:
        number (int): Világ méret.

    Returns:
        any: GLFW window, World, ShaderProgram, szög (float), elipszisidő (float).
    """

    window = createGLFWwindow()
    shader = makeShader()
    glUseProgram(shader)
    world = World(number, shader)
    glEnable(GL_DEPTH_TEST)
    return window, world, shader, 0.0, 0.0