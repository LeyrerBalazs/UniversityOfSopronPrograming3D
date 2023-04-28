# Importok:

# Python modul importok:

from OpenGL.GL import *
from OpenGL.GLU import *

# Egyedi python modul importok:

from functions.openGLFunctions import *
from functions.glfwFunctions import cameraMoves


# Függvények:

def main() -> None:
    """Main függvény.
    """
    window, world, shader, angle, elapsedTime = setDatas(30)
    cameraMatrix = glGetUniformLocation(shader, "camera")
    while not glfw.window_should_close(window):
        startTime = glfw.get_time()
        glfw.poll_events() 
        cameraMoves(world.camera, window, elapsedTime)
        world.light.lightPos()
        giveDatasForVertex(angle, shader)
        world.drawObjects(world.camera, cameraMatrix)
        glfw.swap_buffers(window)
        endTime = glfw.get_time()
        elapsedTime = endTime - startTime
    glfw.terminate()


# Program main-je:

if __name__ == "__main__":
    """Python fájl main-je.
    """
    main()
