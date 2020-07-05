from classes.entity import Entity
from classes import init


class Laser(Entity):
    def __init__(self, laser_image, center_x, center_y, change_y, angle):
        super().__init__(laser_image, init.laser_scale, init.laser_width,
                         init.laser_height, center_x, center_y,
                         init.laser_speed)
        self.angle = angle
        self.change_y = change_y

    def on_update(self, delta_time: float = 1 / 60):
        self.center_y += self.speed * self.change_y
