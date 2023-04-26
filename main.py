from OpenGL.GL import *
from OpenGL.GLU import *
from functions.openGLFunctions import *

def main() -> None:
    """Main function"""
    window, world, shader, angle, elapsedTime = setDatas(30)
    while not glfw.window_should_close(window):
        startTime = glfw.get_time()
        glfw.poll_events() 
        angle += 45.0 * elapsedTime
        world.light.lightPos()
        giveDatasForVertex(angle, shader)
        world.drawObjects()
        glfw.swap_buffers(window)
        endTime = glfw.get_time()
        elapsedTime = endTime - startTime
    glfw.terminate()

if __name__ == "__main__":
    """__main___"""
    main()
