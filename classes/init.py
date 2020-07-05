import arcade

# window:
window_width = 960
window_height = 640

# player:
player_image = ":resources:images/space_shooter/playerShip1_green.png"
player_width = 64
player_height = 64
player_speed = 5
player_power_attack = 5
player_power_health = 5
player_scale = 1
player_center_x = window_width / 2
player_center_y = 64
player_key_up = 65362  # up arrow
player_key_down = 65364  # down arrow
player_key_left = 65361  # left arrow
player_key_right = 65363  # right arrow
player_key_to_shoot = 97  # A


# laser:
laser_image = ":resources:images/space_shooter/laserBlue01.png"
laser_width = 32
laser_height = 4
laser_speed = 5
laser_power_attack = 5
laser_scale = 1

# player laser:
laser_player_change_y = 1
laser_angle_player = 90

# enemy laser:
laser_enemy_change_y = 1
laser_enemy_player = 360

# cannon A
cannon_a_laser_image = ":resources:images/space_shooter/laserBlue01.png"
cannon_a_daly_time = 1
cannon_a_laser_width = 32
cannon_a_laser_height = 4
cannon_a_laser_speed = 5
cannon_a_laser_power_attack = 5
cannon_a_laser_scale = 1
