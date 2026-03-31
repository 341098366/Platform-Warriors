import pygame, sys

WHITE = (255,255,255)
BLACK = (0,0,0)
SELECTIONSCREENBACKGROUND=(201,183,183)
SELECTIONTITLE=(245,214,18)
CHARACTERBACKGROUND=(147,221,239)
PLAYER1=(255,31,31)
PLAYER1LIGHT=(255,88,88)
PLAYER2=(20,116,242)
PLAYER2LIGHT=(97,166,255)
CPU=(163,166,169)
CPULIGHT=(197,199,201)

#Draw Multiplayer Selection Screen
def drawMultiplayerSelection(gameWindow, mode, fonts, images):
    gameWindow.fill(SELECTIONSCREENBACKGROUND)
    drawEnterAndEscape(gameWindow, fonts)
    drawCharacterGrids(gameWindow, images)
    drawSelectionTitle(gameWindow, mode, fonts)
    drawPlayerDisplay(gameWindow, mode, fonts, images)
       #work on characters,double jump,wtf is wrong with check collision and HP
    return

#Draw enter and escape hints
def drawEnterAndEscape(gameWindow, fonts):
    pygame.draw.rect(gameWindow, WHITE, (1000,25,220,125),0)
    graphics=fonts["enterFont"].render("Press Enter",1, BLACK)
    gameWindow.blit(graphics, (1020,45))
    graphics=fonts["enterFont"].render("To Fight",1, BLACK)
    gameWindow.blit(graphics, (1050,90))
    pygame.draw.rect(gameWindow, WHITE, (60,25,220,125),0)
    graphics=fonts["enterFont"].render("Press Escape",1, BLACK)
    gameWindow.blit(graphics, (65,45))
    graphics=fonts["enterFont"].render("To Go Back",1, BLACK)
    gameWindow.blit(graphics, (80,90))
    return

#Draw selection title
def drawSelectionTitle(gameWindow, mode, fonts):
    pygame.draw.rect(gameWindow, SELECTIONTITLE, (340,50,600,100),0)
    if mode == "Singleplayer":
        selectionTitle=fonts["selectionTitleFont"].render("Singleplayer", 1, BLACK)
    elif mode == "Multiplayer":
        selectionTitle=fonts["selectionTitleFont"].render("Multiplayer", 1, BLACK)
    gameWindow.blit(selectionTitle, (435, 60))
    return

#Draw grids for characters
def drawCharacterGrids(gameWindow, images):
    for i in range (2):
        for p in range(4):
            pygame.draw.rect(gameWindow, CHARACTERBACKGROUND, (0+(p*320),160+(i*170),320,170),0)
    pygame.draw.line(gameWindow, BLACK,(0,330),(1280,330),1)
    for i in range(3):
        pygame.draw.line(gameWindow, BLACK,(320+(i*320),160),(320+(i*320),500),1)
    gameWindow.blit(images["blackOps"], (103.5,160))
    return

#Draw Player Display for Character Selection Screen
def drawPlayerDisplay(gameWindow, mode, fonts, images):
    pygame.draw.rect(gameWindow, PLAYER1, (0,500,320,220),0)
    pygame.draw.rect(gameWindow, PLAYER1LIGHT, (320,500,320,220),0)
    graphics=fonts["enterFont"].render("Player 1",1, BLACK)
    gameWindow.blit(graphics, (20,520))
    if mode == "Singleplayer":
        pygame.draw.rect(gameWindow, CPU, (640,500,320,220),0)
        pygame.draw.rect(gameWindow, CPULIGHT, (960,500,320,220),0)
        graphics=fonts["enterFont"].render("CPU",1, BLACK)
        gameWindow.blit(graphics, (660,520))
        graphics=fonts["enterFont"].render("Random",1, BLACK)
        gameWindow.blit(graphics, (660,680))
        gameWindow.blit(images["questionMark"], (992,500))
    elif mode == "Multiplayer":
        pygame.draw.rect(gameWindow, PLAYER2, (640,500,320,220),0)
        pygame.draw.rect(gameWindow, PLAYER2LIGHT, (960,500,320,220),0)
        graphics=fonts["enterFont"].render("Player 2",1, BLACK)
        gameWindow.blit(graphics, (660,520))
    if P1Character=="Black Ops":
        gameWindow.blit(images["blackOps"], (400,530))
    if P2Character=="Black Ops":
        gameWindow.blit(images["blackOps"], (1100,530))
    return