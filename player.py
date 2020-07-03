from entity import Entity, init


class Player(Entity):
    def __init__(self):
        super().__init__(init.player_image, init.player_scale, init.player_width,
                         init.player_height, init.player_center_x, init.player_center_y,
                         init.player_speed, init.player_change_x, init.player_change_y)

    def on_key_press(self, key):
        pass
