from OpenGL.GL import *
import OpenGL.GL.shaders
import pyrr
import math
from functions.glfwFunctions import *
from functions.world import World

def readShaderFile(filename:str) -> str:
    """Shader fájl beolvasás.
    Args:
        filename (str): Fájl neve.
    Returns:
        str: Fájl tartalma."""
    with open(filename) as f:
	    return f.read()
    

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

def giveDatasForVertex(angle, shader) -> None:
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
        world (World): A világ információi
        light (Light): A Cubo-k adatai.
        VBOs (list): Vertex Buffer Objectum-ok.
        shader: Shader Program adatok.
        angle (float): Szög.
        elapsedTime (float): Elipszis idő."""
    window = createGLFWwindow()
    shader = loadShaders()
    glUseProgram(shader)
    world = World(number, shader)
    glEnable(GL_DEPTH_TEST)
    return window, world, shader, 0.0, 0.0


