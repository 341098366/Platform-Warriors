import pygame

def load_images():
    return {
        "questionMark": pygame.image.load("assets/PW Images/Question Mark.png"),
        "fightText": pygame.image.load("assets/PW Images/Fight!.png"),
        "gameText": pygame.image.load("assets/PW Images/Game!.png"),
        "vs": pygame.image.load("assets/PW Images/VS Screen.png"),
        #Black Ops Images
        "blackOps": pygame.image.load("assets/PW Images/Black Ops.png"),
        "blackOpsRight": pygame.image.load("assets/PW Images/Black Ops Standing Right.png"),
        "blackOpsLeft": pygame.image.load("assets/PW Images/Black Ops Standing Left.png"),
        "blackOpsMoveRight": pygame.image.load("assets/PW Images/Black Ops Move Right.png"),
        "blackOpsMoveLeft": pygame.image.load("assets/PW Images/Black Ops Move Left.png"),
        #blackOpsJumpRight": pygame.image.load("assets/PW Images/Black Ops Jump Right.png"),
        #blackOpsJumpLeft": pygame.image.load("assets/PW Images/Black Ops Jump Left.png"),
        "rocketLeft": pygame.image.load("assets/PW Images/Rocket Left.png"),
        "rocketRight": pygame.image.load("assets/PW Images/Rocket Right.png")
    }