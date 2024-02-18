from .enemy import Enemy
from ..teng import vector2D
from copy import deepcopy


class EnemyPool():
    sprite: list
    speed: int
    enemies: list[Enemy]
    rows: int
    max_enemies: int
    movement_cooldown: float
    _cooldown: float

    def __init__(self, max_enemies_row: int = 8, rows: int = 4, speed: int = 1, sprite=["👾"]):
        self.speed = speed
        self.enemies = list()
        self.rows = rows
        self.movement_cooldown = 0.5
        self._cooldown = self.movement_cooldown
        pos = vector2D(0, 0)
        for row in range(rows):
            temp_list = []
            for i in range(max_enemies_row):
                temp_list.append(Enemy(deepcopy(pos), sprite=sprite))
                pos.x += 2
            # FIXME y position has to be tracked on row
            pos.y += 1
            pos.x = 0
            self.enemies.append(temp_list)

    def update(self, max_x: int = 20, delta: float = 0):
        updated_list = []
        self._cooldown -= delta*100
        for row in self.enemies:
            change_direction = False
            for enemy in row:
                if self._cooldown <= 0:
                    enemy.update()
                if enemy.despawn:
                    enemy.sprite = [" "]
                if enemy.position.x < 0 or enemy.position.x >= max_x:
                    change_direction = True

            if change_direction and self._cooldown <= 0:
                for enemy in row:
                    enemy.position.y += 1
                    enemy.direction *= -1
            updated_list.append(row)
        if self._cooldown <= 0:
            self._cooldown = self.movement_cooldown
        updated_list = list(
            filter(lambda row: len(row) != 0, updated_list))
        self.enemies = updated_list

    # def spawn(self, position: vector2D):
    #     if len(self.bullets) < self.MAX_BULLETS:
    #         new_bullet = Bullet(position=position,
    #                             speed=self.speed, sprite=self.sprite)
    #         self.bullets.append(new_bullet)
