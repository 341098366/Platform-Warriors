import pygame, sys

def load_fonts():
    return {
        "menuTitleFont": pygame.font.SysFont("Centaur", 100),
        "menuButtonFont": pygame.font.SysFont("Centaur", 50),
        "selectionTitleFont": pygame.font.SysFont("Britannic", 75),
        "enterFont": pygame.font.SysFont("Britannic", 35),
        "superLargeFont": pygame.font.SysFont("Britannic", 300)
    }