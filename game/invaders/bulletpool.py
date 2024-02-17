from .bullet import Bullet
from ..teng import vector2D


class BulletPool():
    MAX_BULLETS: int
    sprite: list
    speed: int
    bullets: list[Bullet]

    def __init__(self, max_bullets: int = 3, speed: int = -1, sprite=["*"]):
        self.MAX_BULLETS = 3
        self.speed = speed
        self.bullets = list()
        self.sprite = sprite

    def update(self, max_y: int = 20):
        self.bullets = list(
            filter(lambda bullet: not bullet.despawn, self.bullets))
        for bullet in self.bullets:
            bullet.update()
            if bullet.position.y < 0 or bullet.position.y > max_y:
                bullet.despawn = True

    def spawn(self, position: vector2D):
        if len(self.bullets) < self.MAX_BULLETS:
            new_bullet = Bullet(position=position,
                                speed=self.speed, sprite=self.sprite)
            self.bullets.append(new_bullet)
