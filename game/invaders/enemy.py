from ..teng import Actor, vector2D
from .bulletpool import BulletPool


class Enemy(Actor):
    speed: int
    bullet_pool: BulletPool
    move_left: bool = False
    move_right: bool = False
    shoot: bool = False
    direction = 1
    despawn = False

    def __init__(self, position: vector2D, height: int = 1, width: int = 1, sprite: list = ["@"], speed: int = 1):
        super().__init__(position, height, width, sprite)
        self.speed = speed
        self.bullet_pool = BulletPool(sprite=["▴"])

    def update(self):
        if self.direction > 0:
            self.position.x += self.speed
        else:
            self.position.x -= self.speed
