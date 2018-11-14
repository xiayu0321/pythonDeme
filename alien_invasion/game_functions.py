import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def get_number_rows(ai_settings,ship_height,alien_height):
	available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
	number_rows = int(available_space_y / (2 * alien_height))

	return number_rows


def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (alien_width * 2))

	return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number,number_row):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number

	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_row

	aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height) 


	for number_row in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,number_row)

		
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,bullets,screen,ship)


def fire_bullet(ai_settings,bullets,screen,ship):
	if len(bullets) < ai_settings.bullet_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)


def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def  check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,scoreboard):
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()

		pygame.mouse.set_visible(False)

		stats.reset_stats()
		stats.game_active = True

		scoreboard.prep_score()
		scoreboard.prep_high_score()
		scoreboard.prep_level()
		scoreboard.prep_ships()

		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings,screen,ship,aliens)

		ship.center_ship()


def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,scoreboard):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x , mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,scoreboard)


def change_fleet_direciton(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direciton(ai_settings,aliens)
			break


def check_bullet_alien_collision(bullets,aliens,ai_settings,screen,ship,scoreboard,stats):
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_point * len(aliens)
			scoreboard.prep_score()
		check_high_score(stats,scoreboard)


	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()

		stats.level += 1
		scoreboard.prep_level()
		create_fleet(ai_settings,screen,ship,aliens)


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,scoreboard):
	if stats.ship_left > 0:
		stats.ship_left -= 1
		scoreboard.prep_ships()

		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_high_score(stats,scoreboard):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		scoreboard.prep_high_score()

def check_aliens_bottom(ai_settings,stats,screen,ship,bullets,aliens,scoreboard):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,scoreboard)
			break


def update_aliens(ai_settings,aliens,ship,screen,stats,bullets,scoreboard):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()

	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets,scoreboard)

	check_aliens_bottom(ai_settings,stats,screen,ship,bullets,aliens,scoreboard)


def updata_bullets(bullets,aliens,ai_settings,screen,ship,scoreboard,stats):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collision(bullets,aliens,ai_settings,screen,ship,scoreboard,stats)


def updata_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,scoreboard):
	"""更新屏幕上的图像，并切换到新屏幕"""
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()

	aliens.draw(screen)

	scoreboard.show_score()

	if not stats.game_active:
		play_button.draw_button()

	#让最近绘制的屏幕可见
	pygame.display.flip()


