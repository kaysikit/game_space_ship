import pygame.font


class Scoreboard():
    """Class for displaying game information."""
    def __init__(self, ai_settings, screen, stats):
        """Initializes the scoring attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for invoice withdrawal.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Preparing the original image.
        self.prep_score()

    def prep_score(self):
        """Converts the current account to a graphical display."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # Account withdrawal in the upper right part of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right + 1000
        self.score_rect.top = 20

    def show_score(self):
        """Displays the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
