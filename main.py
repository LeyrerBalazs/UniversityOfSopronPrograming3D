from OpenGL.GL import *
from OpenGL.GLU import *
from functions.openGLFunctions import *
from functions.glfwFunctions import cameraMoves

def main() -> None:
    """Main function"""
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

if __name__ == "__main__":
    """__main___"""
    main()
