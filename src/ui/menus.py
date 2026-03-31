import pygame, sys

WHITE=(255,255,255)
MENUBACKGROUND=(142,36,142)
MENUTEXT=(255,100,100)

#Draws the main menu screen
def drawMainMenu(gameWindow, fonts):
    gameWindow.fill(MENUBACKGROUND)
    menuTitle = fonts["menuTitleFont"].render("Platform Warriors", 1, MENUTEXT)
    gameWindow.blit(menuTitle, (325, 75))
    drawMainMenuButtons(gameWindow, fonts, 500, 250, 300, 100)
    return

#Draws buttons for the main menu screen
def drawMainMenuButtons(gameWindow, fonts, x, y, z, a):
    for i in range(3):
        pygame.draw.rect(gameWindow, MENUTEXT, (x,y+(i*150),z,a), 0)
    singleplayerButton = fonts["menuButtonFont"].render("Singleplayer", 1, WHITE)
    gameWindow.blit(singleplayerButton, (x+45, y+25))
    multiplayerButton = fonts["menuButtonFont"].render("Multiplayer", 1, WHITE)
    gameWindow.blit(multiplayerButton, (x+45, y+175))
    exitButton = fonts["menuButtonFont"].render("Quit", 1, WHITE)
    gameWindow.blit(exitButton, (x+100, y+325))
    return