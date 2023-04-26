# Imports
# Default imports
from OpenGL.GL import *
from OpenGL.GLU import *
# Custom imports
from functions.openGLFunctions import *

def main() -> None:
    """Main function
    """
    # Declare variables
    window, count, cubes, VBOs, shader, angle, elapsedTime = setDatas(30)
    lightCoords = [-10.0, 0.0, 0.0]
    leftToRight = True
    downToUp = True
    # Main function
    while not glfw.window_should_close(window):
        startTime = glfw.get_time()
        glfw.poll_events() 
        angle += 45.0 * elapsedTime
        lightCoords[0], lightCoords[1], leftToRight, downToUp = lightPos(lightCoords[0], lightCoords[1], leftToRight, downToUp)
        giveDatasForVertex(angle, shader, lightCoords[0], lightCoords[1], lightCoords[2])
        drawObjects(count, cubes, VBOs)
        glfw.swap_buffers(window)	
        endTime = glfw.get_time()
        elapsedTime = endTime - startTime
    glfw.terminate()

if __name__ == "__main__":
    """__main___
    """
    main()
