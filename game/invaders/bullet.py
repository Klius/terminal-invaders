from ..teng import Actor,vector2D
class Bullet(Actor):
    speed:int
    despawn:bool = False
    
    def __init__(self,position:vector2D,height:int=1,width:int=1,sprite:list=["*"],speed:int=-1):
        super().__init__(position,height,width,sprite)
        self.speed = speed

    def update(self):
        self.position.y += self.speed
