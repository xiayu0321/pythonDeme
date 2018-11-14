import pygame
from settings import Settings
import  game_functions as gf
from ship import Ship
from alien import Alien
from pygame.sprite import Group    
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()

	ai_settings = Settings()  
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
 
	#创建一个飞船
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group() 

	gf.create_fleet(ai_settings,screen,ship,aliens)

	stats = GameStats(ai_settings)

	play_button = Button(ai_settings,screen,"Play")

	scoreboard = Scoreboard(ai_settings,screen,stats)

	while True:

		gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,scoreboard)
		if stats.game_active == True:
			ship.update()
			gf.updata_bullets(bullets,aliens,ai_settings,screen,ship,scoreboard,stats)
			gf.update_aliens(ai_settings,aliens,ship,screen,stats,bullets,scoreboard)

		gf.updata_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,scoreboard)


run_game()
