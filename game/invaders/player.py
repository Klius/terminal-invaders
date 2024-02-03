from ..teng import Actor,vector2D
from .bulletpool import BulletPool

class Player(Actor):

    speed:int
    bullet_pool: BulletPool
    move_left: bool = False
    move_right: bool = False
    shoot: bool = False

    def __init__(self,position:vector2D,height:int=1,width:int=1,sprite:list=["@"],speed:int=1):
        super().__init__(position,height,width,sprite)
        self.speed = speed
        self.bullet_pool = BulletPool(sprite=["▴"])

    def update(self):
        if self.move_left:
            self.position.x -= self.speed
        if self.move_right:
            self.position.x += 1
        if self.shoot:
            pos = vector2D(x=self.position.x+1,y=self.position.y)
            self.bullet_pool.spawn(position=pos)
        
        self.move_left = False
        self.move_right = False
        self.shoot = False
        
        self.bullet_pool.update()

    
        
        
    