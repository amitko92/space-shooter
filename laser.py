from entity import Entity, init


class Laser(Entity):
    def __init__(self, center_x, center_y, change_x, change_y, angle):
        super().__init__(init.laser_image, init.laser_scale, init.laser_width,
                         init.laser_height, center_x, center_y,
                         init.laser_speed, change_x, change_y)
        self.angle = angle
