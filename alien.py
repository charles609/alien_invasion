import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ 表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化alien并设置其位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载alien图像并设置其rect属性
        self.image = pygame.image.load('D:/myGame/codes/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 在alien的属性x中存储小数值
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制alien"""
        self.screen.blit(self.image, self.rect)
