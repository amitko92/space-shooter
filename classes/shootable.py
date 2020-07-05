import arcade

from classes import entity


class Shootable(entity.Entity):
    def __init__(self, image, scale, width, height, center_x, center_y, speed, cannon):
        super().__init__(image, scale, width, height, center_x, center_y, speed)
        self.cannon = cannon

    def shoot(self, list_of_sprites):
        if self.cannon.check_if_can_shut():
            list_of_sprites.append(self.cannon.shoot(self))
