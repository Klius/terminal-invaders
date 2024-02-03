class vector2D:

    x:int
    y:int

    def __init__(self,x:int=0,y:int=0):
        """Vector holding x and y coordinates

        Args:
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __add__(self,other):
        temp = vector2D()
        temp = self.x + other.x
        temp = self.y + other.y
        return temp

    def __sub__(self,other):
        temp = vector2D()
        temp = self.x - other.x
        temp = self.y - other.y
        return temp


    def __mul__(self,other):
        temp = vector2D()
        temp = self.x * other.x
        temp = self.y * other.y
        return temp

    def __eq__(self, other):
        return self.x ==other.x and self.y ==other.y

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"
    