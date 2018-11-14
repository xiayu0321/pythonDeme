import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super(Ship,self).__init__()
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像闭关获取其外接矩形
		self.image = pygame.image.load('./images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.moving_right = False
		self.moving_left = False

		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)


	def update(self):
		if self.moving_right == True and self.rect.right <= self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		elif self.moving_left == True and self.rect.left >= 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def center_ship(self):
		self.center = self.screen_rect.centerx


	def blitme(self):
		'''指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)



