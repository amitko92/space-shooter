from classes import laser, player, init
import arcade

from classes.cannon import Laser_cannon


class Level1(arcade.View):
    def __init__(self):
        super().__init__()
        self.lasers_list = arcade.SpriteList()
        self.player = player.Player(init.player_key_up, init.player_key_down, init.player_key_left,
                                    init.player_key_right, init.player_key_to_shoot, Laser_cannon(init.laser_angle_player), self.lasers_list)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.lasers_list.draw()
        self.window.flip()
        arcade.finish_render()

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time: float):
        self.player.on_update()
        self.lasers_list.on_update()

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol)

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.player.on_key_release(_symbol)
