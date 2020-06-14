import pygame
import game_functions as gf 

from ship import Ship 
from settings import Settings

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Set the background color.
    bg_color = (230,230,230)

    # Begins the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()