import init
import laser
import player
import arcade


class Level1(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = player.Player()
        self.laser = laser.Laser(200, 200, 1, 1, init.laser_angle_player)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.laser.draw()
        self.window.flip()
        arcade.finish_render()

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

