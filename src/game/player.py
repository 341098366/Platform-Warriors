import pygame

class Player:
    def __init__(self):
        self.character = ""
        self.height = 0
        self.width = 0
        self.state = ""
        self.x = 0
        self.y = 0
        self.jumped = False
        self.jumpTime = 0
        self.firstDelay = 0
        self.secondDelay = 0
        self.thirdDelay = 0
        #continue working