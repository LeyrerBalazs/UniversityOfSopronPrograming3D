class Cube:
    """ Kocka osztály.
    """
    def __init__(self, coords:list, colors:list) -> None:
        """Konstruktor.

        Args:
            coords (list): Középponti koordináta.
            colors (list): Szín.
        """

        # Pontok logikája
        # a = [ coords[0] - 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2] ]
        # b = [ coords[0] + 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2] ]
        # c = [ coords[0] + 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2] ]
        # d = [ coords[0] - 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2] ]
        # e = [ coords[0] - 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2] ]
        # f = [ coords[0] + 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2] ]    
        # g = [ coords[0] + 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2] ]
        # h = [ coords[0] - 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2] ]
        
        self.vertPoints = [ coords[0] - 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2],
                            coords[0] - 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2],
                            coords[0] - 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2],
                            coords[0] + 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] + 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2],
                            coords[0] + 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] - 0.5, coords[2] + 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2],
                            coords[0] - 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] - 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] + 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2], coords[0] - 0.5, coords[1] + 0.5, coords[2] - 0.5, colors[0], colors[1], colors[2]]
        self.vertCounts = int(len(self.vertPoints) / 3)
