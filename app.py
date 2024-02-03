import time
import os
from colorama import Fore, just_fix_windows_console
from game.teng.screen import Screen
from game.teng import vector2D
from game.invaders import Player

if os.name == "nt":
    from game.teng.input.windows_input import read_input
    just_fix_windows_console()
else:
    from game.teng.input.linux_input import read_input


key = ""

# States
XOUT: bool = False


screen: Screen
player: Player

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    global screen
    global XOUT
    global key
    global player
    screen = Screen(40,20,space_char=" ")
    player = Player(position=vector2D(20,18),height=1,width=1,sprite=["▁☗▁","███"])
    while not XOUT:
        key = read_input()
        update()
        draw()
        # TODO cap the framerate so it is consistent
        # https://stackoverflow.com/questions/3102888/game-development-how-to-limit-fps
        time.sleep(0.1)


def update():
    global key
    global XOUT
    global player
    
    if key == 'x':
        XOUT = True
        return
    if key == ' ':
        player.shoot=True
    if key == 'd':
        player.move_right=True
    elif key == 'a':
        player.move_left=True

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
    global player
    # Clear previous frame and draw next
    clean()
    screen.clear_buffer()
    screen.add_sprite(player.position.x,player.position.y,player.sprite)
    for bullet in player.bullet_pool.bullets:
        screen.add_sprite(bullet.position.x,bullet.position.y,sprite=bullet.sprite)
    screen.draw()

    
    


try:
    clean()
    main()
    clean()
    print("Thanks for playing!")
except (KeyboardInterrupt, SystemExit):
    os.system('stty sane')
    clean()
