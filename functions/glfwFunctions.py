import glfw

def createGLFWwindow() -> glfw:
    """Ez a függvény felelős a glfw window létrehozásáért és paraméterrel való ellátásáért.
    Raises:
        Exception: glfw inicializálási hiba
        Exception: glfw window inicializálási hiba
    Returns:
        window (glfw)"""
    # Main function
    if not glfw.init():
        raise Exception("glfw init hiba")	
    window = glfw.create_window(1000, 800, "OpenGL window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("glfw window init hiba")
    glfw.set_window_pos(window, 200, 200)
    glfw.make_context_current(window)
    # Returns
    return window

def cameraMoves(camera, window, elapsedTime) -> None:
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        camera.move(elapsedTime * 5)
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        camera.move(-elapsedTime * 5)
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        camera.rotateRightLeft(-elapsedTime * 10)
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        camera.rotateRightLeft(elapsedTime * 10) 
