import time
import os
from colorama import Fore, just_fix_windows_console
from game.teng.screen import Screen
from game.teng import vector2D, Clock
from game.invaders import Player, EnemyPool

if os.name == "nt":
    from game.teng.input.windows_input import read_input
    just_fix_windows_console()
else:
    from game.teng.input.linux_input import read_input


key = ""

# States
XOUT: bool = False
CLEAR: bool = False


# CONST
FPS = 60


screen: Screen
player: Player
enemies: EnemyPool
clock: Clock
score: int


def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def init():
    global screen, player, enemies, clock, score
    screen = Screen(30, 20, space_char=" ")
    player = Player(position=vector2D(20, 18), height=1,
                    width=1, sprite=["▁☗▁", "███"])
    enemies = EnemyPool(sprite="A", max_enemies_row=10)
    score = 0
    clock = Clock()
    game_loop()


def game_loop():
    global XOUT, key, clock
    while not XOUT:
        clock.update()
        start = time.process_time_ns()
        key = read_input()
        update()
        draw()
        elapsed_microseconds = (time.process_time_ns() - start)/1000
        nap_time = ((1000000 / FPS) - elapsed_microseconds) / 1000000
        if nap_time > 0:
            time.sleep(nap_time)


def update():
    update_player()
    check_collisions()
    update_enemies()


def update_enemies():
    global enemies, screen, clock
    enemies.update(screen.MAX_X, clock.get_delta())


def check_collisions():
    global player, enemies, score
    for bullet in player.bullet_pool.bullets:
        col_done = False
        x = len(enemies.enemies)
        for row in enemies.enemies:
            for e in row:
                if not e.despawn and bullet.position.x < e.position.x + e.width and bullet.position.x + bullet.width > e.position.x \
                        and bullet.position.y < e.position.y + e.height and bullet.position.y + bullet.height > e.position.y:
                    bullet.despawn = True
                    e.despawn = True
                    col_done = True
                    # FIXME this ain't working right
                    score += 10*x
                    break
            if col_done:
                break
            x -= 1
        if col_done:
            continue


def update_player():
    global key, XOUT, player

    if key == 'x':
        XOUT = True
        return
    if key == ' ':
        player.shoot = True
    if key == 'd':
        player.move_right = True
    elif key == 'a':
        player.move_left = True

    player.update()


def length_ansi_string(string: str):
    ESC = Literal('\x1b')
    integer = Word(nums)
    escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer, ';')) +
                        oneOf(list(alphas)))

    def nonAnsiString(s): return Suppress(escapeSeq).transformString(s)

    unColorString = nonAnsiString(string)
    return len(unColorString)


def end_msg_box(msg: str, padding: int = 32):
    pad = " "*(padding-length_ansi_string(msg))+"┃"
    return msg+pad


def draw():
    global player, enemies, score
    # Clear previous frame and draw next
    clean()
    screen.clear_buffer()
    screen.add_sprite(player.position.x, player.position.y, player.sprite)
    for row in enemies.enemies:
        for enemy in row:
            screen.add_sprite(enemy.position.x, enemy.position.y, enemy.sprite)
    for bullet in player.bullet_pool.bullets:
        screen.add_sprite(bullet.position.x,
                          bullet.position.y, sprite=bullet.sprite)
    screen.draw()
    print(score)


try:
    clean()
    init()
    clean()
    print("Thanks for playing!")
except (KeyboardInterrupt, SystemExit):
    os.system('stty sane')
    clean()
