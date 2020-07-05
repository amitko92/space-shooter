import classes.init as init
from classes import laser
import time


class Cannon:
    def __init__(self, angle):
        self.angle = angle
        self.ready_to_shut = True

    def shoot(self, entity):
        pass

    def check_if_can_shut(self):
        pass


class Laser_cannon(Cannon):
    def __init__(self, angle):
        super().__init__(angle)
        self.last_shoot_time = 0
        self.min_shoot_time = init.cannon_a_daly_time

    def shoot(self, entity):
        print(entity.change_y)
        return laser.Laser(init.cannon_a_laser_image, entity.center_x, entity.center_y, entity.change_y, self.angle)

    def check_if_can_shut(self):
        current_time = time.time()
        if current_time - self.last_shoot_time > self.min_shoot_time:
            self.last_shoot_time = current_time
            print(current_time)
            return True
        return False
