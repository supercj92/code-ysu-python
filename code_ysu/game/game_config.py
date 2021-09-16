

class GameConfig:
    def __init__(self):

        # screen config
        self.game_name = 'space war'
        self.window_size = (1200, 800)
        self.bg_color = (230, 230, 230)

        # ship config
        self.space_ship_speed = 1
        self.continue_fire = False

        # bullet config
        self.bullet_speed = 1
        # self.bullet_height = 15
        # self.bullet_width = 3
        self.bullet_height = 150
        self.bullet_width = 30
