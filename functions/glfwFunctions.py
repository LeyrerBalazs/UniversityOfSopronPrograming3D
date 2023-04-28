# Importok:

# Python modul importok:

import glfw


# Függvények:

def createGLFWwindow() -> glfw:
    """GLFW ablak létrehozása, inicializálása.

    Raises:
        GLFW init ERROR: Esetleges GLFW inicializálási hiba.
        GLFW window ERROR: Esetleges GLFW window inicializálási hiba.

    Returns:
        glfw: GLFW window.
    """

    if not glfw.init():
        raise Exception("glfw init hiba")	
    window = glfw.create_window(1000, 800, "OpenGL window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("glfw window init hiba")
    glfw.set_window_pos(window, 200, 200)
    glfw.make_context_current(window)
    return window

def cameraMoves(camera, window, elapsedTime) -> None:
    """Event figyelés kamera mozgásra.

    Args:
        camera (Camera): Kamera osztály példány.
        window (glfw): GLFW ablak
        elapsedTime (float): Elipszis idő
    """

    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS or glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
        camera.move(elapsedTime * 5)
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS or glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
        camera.move(-elapsedTime * 5)
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS or glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        camera.rotateRightLeft(-elapsedTime * 10)
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS or glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
        camera.rotateRightLeft(elapsedTime * 10) 
