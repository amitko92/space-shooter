from classes import init


class Entity(init.arcade.Sprite):
    def __init__(self, image, scale, width, height, center_x, center_y, speed):
        super().__init__(filename=image, scale=scale)
        self.center_x = center_x
        self.center_y = center_y
        self.height = height
        self.width = width
        self.speed = speed

    def on_update(self, delta_time: float = 1 / 60):
        self._set_position()

    def _set_position(self):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

