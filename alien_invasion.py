import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initializes the game and creates game objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creation of a ship.
    ship = Ship(screen)

    # Starting the main loop
    while True:
        # Tracking keyboard and mouse events
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()