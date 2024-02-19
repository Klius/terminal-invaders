import random
import time
import os


class Screen():
    MAX_X: int
    MAX_Y: int
    SPACE_CHAR: str
    screen_buffer: list

    def __init__(self, x: int = 80, y: int = 80, space_char: str = " "):
        """Create a screen of size x*y

        Args:
            x (int, optional): Total width of the screen. Defaults to 80.
            y (int, optional): Total height of the screen. Defaults to 80.
        """
        self.MAX_X = x
        self.MAX_Y = y
        self.SPACE_CHAR = space_char
        self.clear_buffer()

    def clear_buffer(self):
        clear_screen = list()
        for i in range(self.MAX_Y):
            clear_screen.append(self.SPACE_CHAR*self.MAX_X)

        self.screen_buffer = clear_screen

    def add_sprite(self, x: int, y: int, sprite: list):
        for i in range(len(sprite)):
            if y+i < self.MAX_Y:
                line = list(self.screen_buffer[y+i])
                sprite_line = sprite[i]
                for xx in range(len(sprite_line)):
                    if x+xx < self.MAX_X and x+xx >= 0:
                        line[x+xx] = sprite_line[xx]

                self.screen_buffer[y+i] = "".join(line)

    def draw(self):
        """
        Print out the screen
        """
        print(f"╔{'═'*self.MAX_X}╗")
        for idx in range(len(self.screen_buffer)):
            print(f"║{self.screen_buffer[idx]}║")
        # print("\n".join(self.screen_buffer))
        print(f"╚{'═'*self.MAX_X}╝")
        # Return cursor up https://stackoverflow.com/questions/34828142/cmd-console-game-reduction-of-blinking
        # print("\033[1;1H", end="")


# just_fix_windows_console()
# s = Screen(50, 20)

# x = 7
# y = 16
# while True:
#     clear()
#     s.clear_buffer()
#     # https://symbl.cc/es/unicode/table/#geometric-shapes
#     # SPRITE = ["┏━━━┓", "┃   ┃", "┗━━━┛"]
#     SPRITE = [f"▄▄▄",
#               f"▛▀▜"]
#     SPRITE2 = ["☗"]
#     # SPRITE = ["👾👾👾👾👾👾👾"]
#     s.add_sprite(x, y, SPRITE)
#     for i in range(1, 4):
#         s.add_sprite(x+(10*i), y, SPRITE)

#     s.add_sprite(24, 19, SPRITE2)
#     s.draw()

#     time.sleep(0.0167)
