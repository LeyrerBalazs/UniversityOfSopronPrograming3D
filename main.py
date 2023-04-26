from OpenGL.GL import *
from OpenGL.GLU import *
from functions.openGLFunctions import *
from functions.lighting import Light

def main() -> None:
    """Main function"""
    window, count, cubes, VBOs, shader, angle, elapsedTime = setDatas(30)
    light = Light()
    while not glfw.window_should_close(window):
        startTime = glfw.get_time()
        glfw.poll_events() 
        angle += 45.0 * elapsedTime
        light.lightPos()
        giveDatasForVertex(angle, shader, light.x, light.y, light.z)
        drawObjects(count, cubes, VBOs)
        glfw.swap_buffers(window)
        endTime = glfw.get_time()
        elapsedTime = endTime - startTime
    glfw.terminate()

if __name__ == "__main__":
    """__main___"""
    main()
