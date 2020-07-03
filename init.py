import arcade

# window:
window_width = 960
window_height = 640

# player:
player_image = ":resources:images/space_shooter/playerShip1_green.png"
player_width = 32
player_height = 32
player_speed = 5
player_change_x = 1
player_change_y = 1
player_power_attack = 5
player_power_health = 5
player_scale = 1
player_center_x = window_width / 2
player_center_y = 32

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
