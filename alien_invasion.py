import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initializes the game and creates game objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a Play button.
    play_button = Button(ai_settings, screen, "Play game")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    bg_color = (230, 230, 230)

    # Creation of a ship.
    ship = Ship(ai_settings, screen)

    # Create a group to store bullets
    bullets = Group()

    # Create an alien
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Starting the main loop
    while True:
        # Tracking keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
