class Light:
    def __init__(self):
        self.x = -10.0
        self.y = 0.0
        self.z = 0.0
        self.leftToRight = True
        self.downToUp = True

    def lightPos(self) -> None:
        """Ez állítja be a Fény mozgó Pozicíóját.
        Args:
            lx (float): Fény x koordináta.
            ly (float): Fény x koordináta.
            leftToRight (bool): Balról megy jobbra.
            downToUp (bool): Lentről megy fel.
        Returns:
            lx (float): Fény x koordináta.
            ly (float): Fény x koordináta.
            leftToRight (bool): Balról megy jobbra.
            downToUp (bool): Lentről megy fel."""
        if int(self.x) == 10.0:
            self.leftToRight = False
        elif int(self.x) == -10.0:
            self.leftToRight= True
        if int(self.y) == 10:
            self.downToUp = False
        elif int(self.y) == -10.0:
            self.downToUp= True
        if self.leftToRight == True:
            self.x += 0.1
        elif self.leftToRight == False:
            self.x -= 0.1
        if self.downToUp == True:
            self.y += 0.1
        elif self.downToUp == False:
            self.y -= 0.1