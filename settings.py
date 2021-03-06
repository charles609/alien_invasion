
class Settings:

    """存储《外星人入侵》 的所有设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (199, 237, 204)
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed_factor = 0.75

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
