import pygame
import game_functions as gf 

from ship import Ship 
from settings import Settings
from pygame.sprite import Group 

#  generates objects such as settings, the screen and the ship

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Set the background color.
    bg_color = (230,230,230)

    # Begins the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()