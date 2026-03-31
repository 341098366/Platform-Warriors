import pygame

def load_maps():
    return {
        "grassLand": pygame.image.load("assets/PW Maps/Grass Land.png"),
        #Unused maps
        "finalDestination": pygame.image.load("assets/PW Maps/Final Destination.png"),
        "yoshi": pygame.image.load("assets/PW Maps/Yoshi's Island.png"),
        "greenGreens": pygame.image.load("assets/PW Maps/Green Greens.png")
    }