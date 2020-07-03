import init


class Entity(init.arcade.Sprite):
    def __init__(self, image, scale, width, height, center_x, center_y, speed, change_x, change_y):
        super().__init__(filename=image, scale=scale)
        self.center_x = center_x
        self.center_y = center_y
        self.height = height
        self.width = width
        self.speed = speed
        self.change_x = change_x
        self.change_y = change_y

    def on_update(self, delta_time: float = 1 / 60):
        self.set_position()

    def set_position(self):
        print(self.change_x)
