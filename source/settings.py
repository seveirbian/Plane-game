class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # 子弹设置
        # self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 12

        # 外星人设置
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 3
        # fleet_direction为1表示向右移，为-1表示向左移
        # self.fleet_direction = 1

        #  游戏节奏加速度
        self.speed_scale = 1.1
        # 外星人点数提高速度
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 设置外星人分数
        self.alien_points = 10

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale

        '''提高外星人点数'''
        self.alien_points = int(self.alien_points * self.score_scale)