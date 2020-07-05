import arcade
from classes import level_1, init


class Game(arcade.Window):
    def __init__(self):
        super().__init__(init.window_width, init.window_height, "space shooter")
        self.level_1 = level_1.Level1()

    def play(self):
        self.show_view(self.level_1)
        arcade.run()


g = Game()
g.play()
