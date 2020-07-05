from classes import init
from classes.entity import Entity
from classes.shootable import Shootable


class Player(Shootable):
    def __init__(self, key_up, key_down, key_left, key_right, key_to_shoot, cannon, list_of_lasers):
        super().__init__(init.player_image, init.player_scale, init.player_width,
                         init.player_height, init.player_center_x, init.player_center_y,
                         init.player_speed, cannon)
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.key_to_shoot = key_to_shoot
        self.cannon = cannon
        self.list_of_lasers = list_of_lasers

    def on_key_press(self, key):
        if key == self.key_up:
            pass
        elif key == self.key_down:
            pass
        elif key == self.key_left:
            self.change_x = -1
        elif key == self.key_right:
            self.change_x = 1

    def on_key_release(self, key: int):
        if key == self.key_up:
            pass
        elif key == self.key_down:
            pass
        elif key == self.key_left:
            self.change_x = 0
        elif key == self.key_right:
            self.change_x = 0
        elif key == self.key_to_shoot:
            self.shoot(self.list_of_lasers)

    def on_update(self, delta_time: float = 1 / 60):
        self._set_position()

