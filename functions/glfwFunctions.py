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
    window = glfw.create_window(1400, 1000, "OpenGL window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("glfw window init hiba")
    glfw.set_window_pos(window, 400, 200)
    glfw.make_context_current(window)
    # Returns
    return window
