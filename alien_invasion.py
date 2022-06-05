import pygame
from pygame.sprite import Group

from alien import Alien
import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship

def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make a group of alients
    aliens = Group()
    
    # Create fleet of alients
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active: 
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    
run_game()