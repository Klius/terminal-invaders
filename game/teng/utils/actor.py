from .vector import vector2D
class Actor:
    position: vector2D
    height: int
    width : int
    sprite: list

    def __init__(self,position:vector2D,height:int,width:int,sprite:list):
        self.position = position
        self.height = height
        self.width = width
        self.sprite = sprite

    def __update__(self):
        pass
        