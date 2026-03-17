#Platform Warriors, A platform fighter game, Max Yang, 26/05/2023

#Image Credits:
#Black Ops retrieved from dreamstime.com
#Fight and game text retrieved from SSBU
#Question Mark taken from google images
#Rocket retrieved from Soul Knight
#Grass land take from google images
#Unused Maps taken from SSBU
#Thunderzone V2 by Waterflame

#Imports
import pygame, sys
from pygame.locals import QUIT
from random import randint
from pygame import mixer
mixer.init()

#Images
questionMark=pygame.image.load("PW Images/Question Mark.png")
fightText=pygame.image.load("PW Images/Fight!.png")
gameText=pygame.image.load("PW Images/Game!.png")
vs=pygame.image.load("PW Images/VS Screen.png")
#Black Ops Images
blackOps=pygame.image.load("PW Images/Black Ops.png")
blackOpsRight=pygame.image.load("PW Images/Black Ops Standing Right.png")
blackOpsLeft=pygame.image.load("PW Images/Black Ops Standing Left.png")
blackOpsMoveRight=pygame.image.load("PW Images/Black Ops Move Right.png")
blackOpsMoveLeft=pygame.image.load("PW Images/Black Ops Move Left.png")
#blackOpsJumpRight=pygame.image.load("PW Images/Black Ops Jump Right.png")
#blackOpsJumpLeft=pygame.image.load("PW Images/Black Ops Jump Left.png")
rocketLeft=pygame.image.load("PW Images/Rocket Left.png")
rocketRight=pygame.image.load("PW Images/Rocket Right.png")

#Music
mixer.music.load("PW Music/Thunderzone 2.mp3")
mixer.music.play(-1)

#Maps
grassLand=pygame.image.load("PW Maps/Grass Land.png")
#Unused maps
finalDestination=pygame.image.load("PW Maps/Final Destination.png")
yoshi=pygame.image.load("PW Maps/Yoshi's Island.png")
greenGreens=pygame.image.load("PW Maps/Green Greens.png")

#Functions

#Draws the main menu screen
def drawMainMenu():
    gameWindow.fill(MENUBACKGROUND)
    menuTitle = menuTitleFont.render("Platform Warriors", 1, MENUTEXT)
    gameWindow.blit(menuTitle, (325, 75))
    drawMainMenuButtons(500,250,300,100)
    return

#Draws buttons for the main menu screen
def drawMainMenuButtons(x,y,z,a):
    for i in range(3):
        pygame.draw.rect(gameWindow, MENUTEXT, (x,y+(i*150),z,a), 0)
    singleplayerButton = menuButtonFont.render("Singleplayer", 1, WHITE)
    gameWindow.blit(singleplayerButton, (x+45, y+25))
    multiplayerButton = menuButtonFont.render("Multiplayer", 1, WHITE)
    gameWindow.blit(multiplayerButton, (x+45, y+175))
    exitButton = menuButtonFont.render("Quit", 1, WHITE)
    gameWindow.blit(exitButton, (x+100, y+325))
    return

#Draw Multiplayer Selection Screen
def drawMultiplayerSelection():
    gameWindow.fill(SELECTIONSCREENBACKGROUND)
    drawEnterAndEscape()
    drawCharacterGrids()
    drawSelectionTitle()
    drawPlayerDisplay()
       #work on characters,double jump,wtf is wrong with check collision and HP

    return

#Draw enter and escape hints
def drawEnterAndEscape():
    pygame.draw.rect(gameWindow, WHITE, (1000,25,220,125),0)
    graphics=enterFont.render("Press Enter",1, BLACK)
    gameWindow.blit(graphics, (1020,45))
    graphics=enterFont.render("To Fight",1, BLACK)
    gameWindow.blit(graphics, (1050,90))
    pygame.draw.rect(gameWindow, WHITE, (60,25,220,125),0)
    graphics=enterFont.render("Press Escape",1, BLACK)
    gameWindow.blit(graphics, (65,45))
    graphics=enterFont.render("To Go Back",1, BLACK)
    gameWindow.blit(graphics, (80,90))
    return

#Draw selection title
def drawSelectionTitle():
    pygame.draw.rect(gameWindow, SELECTIONTITLE, (340,50,600,100),0)
    if singleplayer==True:
        selectionTitle=selectionTitleFont.render("Singleplayer", 1, BLACK)
    elif multiplayer==True:
        selectionTitle=selectionTitleFont.render("Multiplayer", 1, BLACK)
    gameWindow.blit(selectionTitle, (435, 60))
    return

#Draw grids for characters
def drawCharacterGrids():
    for i in range (2):
        for p in range(4):
            pygame.draw.rect(gameWindow, CHARACTERBACKGROUND, (0+(p*320),160+(i*170),320,170),0)
    pygame.draw.line(gameWindow, BLACK,(0,330),(1280,330),1)
    for i in range(3):
        pygame.draw.line(gameWindow, BLACK,(320+(i*320),160),(320+(i*320),500),1)
    gameWindow.blit(blackOps, (103.5,160))
    return

#Draw Player Display for Character Selection Screen
def drawPlayerDisplay():
    pygame.draw.rect(gameWindow, PLAYER1, (0,500,320,220),0)
    pygame.draw.rect(gameWindow, PLAYER1LIGHT, (320,500,320,220),0)
    graphics=enterFont.render("Player 1",1, BLACK)
    gameWindow.blit(graphics, (20,520))
    if singleplayer==True:
        pygame.draw.rect(gameWindow, CPU, (640,500,320,220),0)
        pygame.draw.rect(gameWindow, CPULIGHT, (960,500,320,220),0)
        graphics=enterFont.render("CPU",1, BLACK)
        gameWindow.blit(graphics, (660,520))
        graphics=enterFont.render("Random",1, BLACK)
        gameWindow.blit(graphics, (660,680))
        gameWindow.blit(questionMark, (992,500))
    elif multiplayer==True:
        pygame.draw.rect(gameWindow, PLAYER2, (640,500,320,220),0)
        pygame.draw.rect(gameWindow, PLAYER2LIGHT, (960,500,320,220),0)
        graphics=enterFont.render("Player 2",1, BLACK)
        gameWindow.blit(graphics, (660,520))
    if P1Character=="Black Ops":
        gameWindow.blit(blackOps,(400,530))
    if P2Character=="Black Ops":
        gameWindow.blit(blackOps,(1100,530))
    return

#Draw loading screen
def drawLoadingScreen():
    gameWindow.fill(WHITE)
    pygame.display.update()
    selectingMap1Dot=menuTitleFont.render("Selecting Map .",1, BLACK)
    selectingMap2Dot=menuTitleFont.render("Selecting Map ..",1, BLACK)
    selectingMap3Dot=menuTitleFont.render("Selecting Map ...",1, BLACK)
    for i in range(3):
        for i in range(3):
            if i==0:
                gameWindow.blit(selectingMap1Dot, (310,310))
            elif i==1:
                gameWindow.blit(selectingMap2Dot, (310,310))
            elif i==2:
                gameWindow.blit(selectingMap3Dot, (310,310))
            pygame.display.update()
            pygame.time.delay(600)
            gameWindow.fill(WHITE)
    loading1Dot=menuTitleFont.render("Loading .",1, BLACK)
    loading2Dot=menuTitleFont.render("Loading ..",1, BLACK)
    loading3Dot=menuTitleFont.render("Loading ...",1, BLACK)
    for i in range(3):
        for i in range(3):
            if i==0:
                gameWindow.blit(loading1Dot, (400,310))
            elif i==1:
                gameWindow.blit(loading2Dot, (400,310))
            elif i==2:
                gameWindow.blit(loading3Dot, (400,310))
            pygame.display.update()
            pygame.time.delay(600)
            gameWindow.fill(WHITE)
    gameWindow.blit(vs,(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    if P1Character=="Black Ops":
        gameWindow.blit(blackOps,(300,250))
    if P2Character=="Black Ops":
        gameWindow.blit(blackOps,(940,250))
    pygame.display.update()
    pygame.time.delay(5000)
    return

#Draw the Game
def redrawGameWindow():
    gameWindow.blit(map,(0,0))
    drawP1()
    drawP2()
    drawHP()
    pygame.display.update()
    return

#Draw P1
def drawP1():
    gameWindow.blit(P1State,(P1X,P1Y))
    graphics=enterFont.render("P1",1, PLAYER1)
    gameWindow.blit(graphics, (P1X,P1Y-40))
    drawP1Attack()
    return

#Draw P2
def drawP2():
    gameWindow.blit(P2State,(P2X,P2Y))
    graphics=enterFont.render("P2",1, PLAYER2)
    gameWindow.blit(graphics, (P2X,P2Y-40))
    drawP2Attack()
    return

#Draw P1 Attack
def drawP1Attack():
    if P1Character=="Black Ops":
        for f in range(len(P1FirstX)):
            pygame.draw.rect(gameWindow, BLACK, (P1FirstX[f],P1FirstY[f],20,5),0)
            P1FirstX[f]=P1FirstX[f]+P1FirstSpeed[f]
        for s in range(len(P1SecondX)):
            if P1SecondSpeed[s]==33:
                gameWindow.blit(rocketRight, (P1SecondX[s], P1SecondY[s]))
            if P1SecondSpeed[s] == -33:
                gameWindow.blit(rocketLeft, (P1SecondX[s], P1SecondY[s]))
            P1SecondX[s]=P1SecondX[s]+P1SecondSpeed[s]            
    return

#Draw P2 Attack
def drawP2Attack():
    if P2Character=="Black Ops":
        for f in range(len(P2FirstX)):
            pygame.draw.rect(gameWindow, BLACK, (P2FirstX[f],P2FirstY[f],20,5),0)
            P2FirstX[f]=P2FirstX[f]+P2FirstSpeed[f]
        for s in range(len(P2SecondX)):
            if P2SecondSpeed[s]==33:
                gameWindow.blit(rocketRight, (P2SecondX[s], P2SecondY[s]))
            if P2SecondSpeed[s] == -33:
                gameWindow.blit(rocketLeft, (P2SecondX[s], P2SecondY[s]))
            P2SecondX[s]=P2SecondX[s]+P2SecondSpeed[s]
    return

#Check Bullet Collisions
def checkCollision(P1Health, P2Health):
    P1FirstDelete=[]
    P1SecondDelete=[]
    P2FirstDelete=[]
    P2SecondDelete=[]
    if P1Character=="Black Ops":
        for f in range(len(P1FirstX)):
            if P1FirstX[f] in range(P2X, P2X+P2CharacterWidth) and P1FirstY[f] in range(P2Y, P2Y+P2CharacterHeight):
                P1FirstDelete.append(f)
        for i in range(len(P1FirstDelete)):
            P1FirstX.pop(i)
            P1FirstY.pop(i)
            P1FirstSpeed.pop(i)
            P2Health=P2Health-5
        for s in range(len(P1SecondX)):
            if P1SecondX[s] in range(P2X, P2X+P2CharacterWidth) and P1SecondY[s] in range(P2Y-50, P2Y+P2CharacterHeight):
                P1SecondDelete.append(s)
        for i in range(len(P1SecondDelete)):
            P1SecondX.pop(i)
            P1SecondY.pop(i)
            P1SecondSpeed.pop(i)
            P2Health=P2Health-25
    if P2Character=="Black Ops":
        for f in range(len(P2FirstX)):
            if P2FirstX[f] in range(P1X, P1X+P1CharacterWidth) and P2FirstY[f] in range(P1Y, P1Y+P1CharacterHeight):
                P2FirstDelete.append(f)
        for i in range(len(P2FirstDelete)):
            P2FirstX.pop(i)
            P2FirstY.pop(i)
            P2FirstSpeed.pop(i)
            P1Health=P1Health-5
        for s in range(len(P2SecondX)):
            if P2SecondX[s] in range(P1X, P1X+P1CharacterWidth) and P2SecondY[s] in range(P1Y-50, P1Y+P1CharacterHeight):
                P2SecondDelete.append(s)
        for i in range(len(P2SecondDelete)):
            P2SecondX.pop(i)
            P2SecondY.pop(i)
            P2SecondSpeed.pop(i)
            P1Health=P1Health-25

#Display HP
def drawHP():
    P1HP=selectionTitleFont.render("P1 HP: "+str(P1Health),1, PLAYER1)
    P2HP=selectionTitleFont.render("P2 HP: "+str(P2Health),1, PLAYER2)
    gameWindow.blit(P1HP, (100,600))
    gameWindow.blit(P2HP, (800,600))
    return

#Main program
pygame.init()
WIDTH = 1280
HEIGHT = 720
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platform Warriors')

#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
MENUBACKGROUND=(142,36,142)
MENUTEXT=(255,100,100)
SELECTIONSCREENBACKGROUND=(201,183,183)
SELECTIONTITLE=(245,214,18)
CHARACTERBACKGROUND=(147,221,239)
PLAYER1=(255,31,31)
PLAYER1LIGHT=(255,88,88)
PLAYER2=(20,116,242)
PLAYER2LIGHT=(97,166,255)
CPU=(163,166,169)
CPULIGHT=(197,199,201)

#Fonts
menuTitleFont=pygame.font.SysFont("Centaur", 100)
menuButtonFont=pygame.font.SysFont("Centaur", 50)
selectionTitleFont=pygame.font.SysFont("Britannic",75)
enterFont=pygame.font.SysFont("Britannic",35)
superLargeFont=pygame.font.SysFont("Britannic", 300)

#Booleans
mainMenu=True
singleplayer=False
multiplayer=False
P1CharacterSelected=False
P2CharacterSelected=False
displayLoadingScreen=False
player2CPU=False
beforeFighting=False
fighting=False
gameOver=False

#Variables
allCharacters=["Black Ops"]
map=""

while True:
    mouseX, mouseY = pygame.mouse.get_pos()
    if mainMenu==True:
        drawMainMenu()
        #Reset all variables
        #P1 Variables
        P1Character=""
        P1CharacterHeight=0
        P1CharacterWidth=0
        P1State=""
        P1X=0
        P1Y=0
        P1Jumped=False
        P1JumpTime=0
        P1FirstDelay=0
        P1SecondDelay=0
        P1ThirdDelay=0
        P1FirstX=[]
        P1FirstY=[]
        P1FirstSpeed=[]
        P1FirstDelete=[]
        P1SecondX=[]
        P1SecondY=[]
        P1SecondSpeed=[]
        P1SecondDelete=[]
        P1ThirdX=[]
        P1ThirdY=[]
        P1ThirdSpeed=[]
        P1Health=0
        #P2 Variables
        P2Character=""
        P2CharacterHeight=0
        P2CharacterWidth=0
        P2State=""
        P2X=0
        P2Y=0
        P2Jumped=False
        P2JumpTime=0
        P2FirstDelay=0
        P2SecondDelay=0
        P2ThirdDelay=0
        P2FirstX=[]
        P2FirstY=[]
        P2FirstSpeed=[]
        P2FirstDelete=[]
        P2SecondX=[]
        P2SecondY=[]
        P2SecondSpeed=[]
        P2SecondDelete=[]
        P2ThirdX=[]
        P2ThirdY=[]
        P2ThirdSpeed=[]
        P2Health=0
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Unused SinglePLayer
                if mouseX in range(500, 800) and mouseY in range(250, 350):
                    print("Singleplayer")
                    singleplayer=True
                    mainMenu=False
                #Go to Multiplayer
                elif mouseX in range(500, 800) and mouseY in range(400, 500):
                    print("Multiplayer")
                    multiplayer=True
                    mainMenu=False
                #Exit Game
                elif mouseX in range(500, 800) and mouseY in range(550, 650):
                    print("Quit")
                    pygame.quit()
                    sys.exit()
    elif multiplayer==True:
        player2CPU=False
        drawMultiplayerSelection()
        for event in pygame.event.get():
            #Selecting P1 Character
            if event.type==pygame.MOUSEBUTTONDOWN:
                if mouseX in range(0,320) and mouseY in range(160,330):
                    print("Black Ops Selected")
                    P1Character="Black Ops"
                    P1CharacterSelected=True
                    P1CharacterHeight=94
                    P1CharacterWidth=70
                    P1State=blackOpsRight
                    P1Health=300
            if event.type == pygame.KEYDOWN:
                #Selecting P2 Character
                if event.key == pygame.K_RSHIFT:
                    if mouseX in range(0,320) and mouseY in range(160,330):
                        print("Black Ops Selected")
                        P2Character="Black Ops"
                        P2CharacterSelected=True
                        P2CharacterHeight=94
                        P2CharacterWidth=70
                        P2State=blackOpsLeft
                        P2Health=300
                #Go back to Main Menu
                if event.key == pygame.K_ESCAPE:
                    print("Go back")
                    P1CharacterSelected=False
                    P2CharacterSelected=False
                    mainMenu=True
                    multiplayer=False
                    P1Character=""
                    P2Character=""
                #Play Game
                if event.key==pygame.K_RETURN:
                    if P1CharacterSelected==True and P2CharacterSelected==True:
                        print("Fight")
                        multiplayer=False
                        displayLoadingScreen=True
                        whichMap=randint(1,1)
                        if whichMap==1:
                            map=grassLand
                            groundX1=0
                            groundX2=1280
                            groundY=575
                            P1X=100
                            P1Y=groundY-P1CharacterHeight
                            P2X=1180
                            P2Y=groundY-P2CharacterHeight
                        elif whichMap==2:
                            map=finalDestination
                        elif whichMap==3:
                            map=yoshi
                        elif whichMap==4:
                            map=greenGreens
                        gameWindow.blit(fightText,(0,100))
                        pygame.display.update()
                        pygame.time.delay(3000)
    #Loading Screen
    elif displayLoadingScreen==True:
        #drawLoadingScreen()
        displayLoadingScreen=False
        beforeFighting=True
    #Countdown
    elif beforeFighting==True:
        for i in range(4):
            gameWindow.blit(map,(0,0))
            gameWindow.blit(P1State,(P1X,P1Y))
            gameWindow.blit(P2State,(P2X,P2Y))
            if i==0:
                graphics=superLargeFont.render("3",1, BLACK)
            elif i==1:
                graphics=superLargeFont.render("2",1, BLACK)
            elif i==2:
                graphics=superLargeFont.render("1",1, BLACK)
            elif i==3:
                graphics=superLargeFont.render("GO!",1, BLACK)
            gameWindow.blit(graphics, (500,250))
            pygame.display.update()
            pygame.time.delay(1500)
        beforeFighting=False
        fighting=True
    #During the game
    elif fighting==True:
        redrawGameWindow()
        #checkCollision(P1Health, P2Health)
        #Below is identical to checkCollision. for some reason it would
        #not work when i put the code in a function.
        P1FirstDelete=[]
        P1SecondDelete=[]
        P2FirstDelete=[]
        P2SecondDelete=[]
        if P1Character=="Black Ops":
            for f in range(len(P1FirstX)):
                if P1FirstX[f] in range(P2X, P2X+P2CharacterWidth) and P1FirstY[f] in range(P2Y, P2Y+P2CharacterHeight):
                    P1FirstDelete.append(f)
            for i in range(len(P1FirstDelete)):
                P1FirstX.pop(i)
                P1FirstY.pop(i)
                P1FirstSpeed.pop(i)
                P2Health=P2Health-5
            for s in range(len(P1SecondX)):
                if P1SecondX[s] in range(P2X, P2X+P2CharacterWidth) and P1SecondY[s] in range(P2Y-50, P2Y+P2CharacterHeight):
                    P1SecondDelete.append(s)
            for i in range(len(P1SecondDelete)):
                P1SecondX.pop(i)
                P1SecondY.pop(i)
                P1SecondSpeed.pop(i)
                P2Health=P2Health-20
        if P2Character=="Black Ops":
            for f in range(len(P2FirstX)):
                if P2FirstX[f] in range(P1X, P1X+P1CharacterWidth) and P2FirstY[f] in range(P1Y, P1Y+P1CharacterHeight):
                    P2FirstDelete.append(f)
            for i in range(len(P2FirstDelete)):
                P2FirstX.pop(i)
                P2FirstY.pop(i)
                P2FirstSpeed.pop(i)
                P1Health=P1Health-5
            for s in range(len(P2SecondX)):
                if P2SecondX[s] in range(P1X, P1X+P1CharacterWidth) and P2SecondY[s] in range(P1Y-50, P1Y+P1CharacterHeight):
                    P2SecondDelete.append(s)
            for i in range(len(P2SecondDelete)):
                P2SecondX.pop(i)
                P2SecondY.pop(i)
                P2SecondSpeed.pop(i)
                P1Health=P1Health-20
        for event in pygame.event.get():
            if P1Character=="Black Ops":
                #P1 Movement
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a:
                        P1State=blackOpsMoveLeft
                    if event.key==pygame.K_d:
                        P1State=blackOpsMoveRight
                    if event.key==pygame.K_w and P1Jumped==False:
                        P1Jumped=True
                        P1JumpTime=25
                    #P1 Attack Buttons
                    if event.key==pygame.K_t and P1FirstDelay<=0:
                        if P1State==blackOpsMoveRight or P1State==blackOpsRight:
                            P1FirstX.append(P1X+P1CharacterWidth)
                            P1FirstSpeed.append(10)
                            P1FirstDelay=20
                        elif P1State==blackOpsMoveLeft or P1State==blackOpsLeft:
                            P1FirstX.append(P1X)
                            P1FirstSpeed.append(-10)
                            P1FirstDelay=20
                        P1FirstY.append(P1Y+40)
                    if event.key==pygame.K_y and P1SecondDelay<=0:
                        if P1State==blackOpsMoveRight or P1State==blackOpsRight:
                            P1SecondX.append(P1X+P1CharacterWidth)
                            P1SecondSpeed.append(33)
                            P1SecondDelay=50
                        elif P1State==blackOpsMoveLeft or P1State==blackOpsLeft:
                            P1SecondX.append(P1X)
                            P1SecondSpeed.append(-33)
                            P1SecondDelay=50
                        P1SecondY.append(P1Y+40)
                    if event.key==pygame.K_u and P1ThirdDelay<=0:
                        P1Y=P1Y-300
                        P1ThirdDelay=150
                        P1Jumped=True
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_a:
                        P1State=blackOpsLeft
                    if event.key==pygame.K_d:
                        P1State=blackOpsRight
            if P2Character=="Black Ops":
                #P2 Movement
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        P2State=blackOpsMoveLeft
                    if event.key==pygame.K_RIGHT:
                        P2State=blackOpsMoveRight
                    if event.key==pygame.K_UP and P2Jumped==False:
                        P2Jumped=True
                        P2JumpTime=25
                    #P2 Attack Buttons
                    if event.key==pygame.K_KP7 and P2FirstDelay<=0:
                        if P2State==blackOpsMoveRight or P2State==blackOpsRight:
                            P2FirstX.append(P2X+P2CharacterWidth)
                            P2FirstSpeed.append(10)
                            P2FirstDelay=20
                        elif P2State==blackOpsMoveLeft or P2State==blackOpsLeft:
                            P2FirstX.append(P2X)
                            P2FirstSpeed.append(-10)
                            P2FirstDelay=20
                        P2FirstY.append(P2Y+40)
                    if event.key==pygame.K_KP8 and P2SecondDelay<=0:
                        if P2State==blackOpsMoveRight or P2State==blackOpsRight:
                            P2SecondX.append(P2X+P2CharacterWidth)
                            P2SecondSpeed.append(33)
                            P2SecondDelay=50
                        elif P2State==blackOpsMoveLeft or P2State==blackOpsLeft:
                            P2SecondX.append(P2X)
                            P2SecondSpeed.append(-33)
                            P2SecondDelay=50
                        P2SecondY.append(P2Y+40)
                    if event.key==pygame.K_KP9 and P2ThirdDelay<=0:
                        P2Y=P2Y-300
                        P2ThirdDelay=150
                        P2Jumped=True
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        P2State=blackOpsLeft
                    if event.key==pygame.K_RIGHT:
                        P2State=blackOpsRight
        #Wall Collision and jumping mechanics for P1 and P2
        if P1Character=="Black Ops":
            if P1State==blackOpsMoveLeft:
                if P1X>0:
                    P1X=P1X-4
            if P1State==blackOpsMoveRight:
                if P1X<1280-P1CharacterWidth:
                    P1X=P1X+4
            if P1Jumped==True:
                if P1JumpTime!=0:
                    P1Y=P1Y-5
                    P1JumpTime=P1JumpTime-1
                elif P1JumpTime==0 and P1Y!=groundY-P1CharacterHeight:
                    P1Y=P1Y+5
                elif P1Y==groundY-P1CharacterHeight:
                    P1Jumped=False
        if P2Character=="Black Ops":
            if P2State==blackOpsMoveLeft:
                if P2X>0:
                    P2X=P2X-4
            if P2State==blackOpsMoveRight:
                if P2X<1280-P2CharacterWidth:
                    P2X=P2X+4
            if P2Jumped==True:
                if P2JumpTime!=0:
                    P2Y=P2Y-5
                    P2JumpTime=P2JumpTime-1
                elif P2JumpTime==0 and P2Y!=groundY-P2CharacterHeight:
                    P2Y=P2Y+5
                elif P2Y==groundY-P2CharacterHeight:
                    P2Jumped=False
        #Attack Delays
        P1FirstDelay=P1FirstDelay-1
        P1SecondDelay=P1SecondDelay-1
        P1ThirdDelay=P1ThirdDelay-1
        P2FirstDelay=P2FirstDelay-1
        P2SecondDelay=P2SecondDelay-1
        P2ThirdDelay=P2ThirdDelay-1
        drawHP()
        #Check if game over
        if P1Health<=0 or P2Health<=0:
            gameWindow.blit(gameText,(0,100))
            pygame.display.update()
            fighting=False
            gameOver=True
            pygame.time.delay(3000)
    elif gameOver==True:
        #Game Over Screen
        gameWindow.fill(WHITE)
        if P1Health<=0:
            graphics=menuTitleFont.render("Player 2 Wins!",1, BLACK)
        elif P2Health<=0:
            graphics=menuTitleFont.render("Player 1 Wins!",1, BLACK)
        gameWindow.blit(graphics, (400,310))
        pygame.display.update()
        pygame.time.delay(5000)
        gameOver=False
        #Go back to main menu
        mainMenu=True
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.event.clear()
