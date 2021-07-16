import sys

import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Refreshes the screen image and displays a new screen."""
    # At each pass of the loop, the screen is redrawn.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Displays the last drawn screen.
    pygame.display.flip()
