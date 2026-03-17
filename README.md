<p align="center">
  <img src="PW Images/Icon.png" width="500">
</p>

# Platform Warriors

**Platform Warriors** is a 2-player platform fighting game built with
**Python and Pygame**. Players battle on a platform map using movement,
jumps, and projectile attacks to reduce their opponent's health to zero.

Created by **Max Yang**\
Date: **May 26, 2023**

------------------------------------------------------------------------

# Overview

Platform Warriors is inspired by platform fighter games such as **Super
Smash Bros.**. Two players control characters on a stage and attack each
other using different projectile abilities.

The objective is simple:

-   Reduce your opponent's **HP to 0**
-   Avoid getting hit by attacks
-   Use movement and jumps strategically

------------------------------------------------------------------------

# Features

-   Main menu system
-   Multiplayer character selection
-   Countdown before match start
-   Player movement (left, right, jump)
-   Multiple projectile attacks
-   Health tracking system
-   Game over and winner screen
-   Background music
-   Map loading system

------------------------------------------------------------------------

# Controls

## Player 1

  Action             Key
  ------------------ -----
  Move Left          A
  Move Right         D
  Jump               W
  Primary Attack     T
  Secondary Attack   Y
  Special Ability    U

------------------------------------------------------------------------

## Player 2

  Action             Key
  ------------------ -------------
  Move Left          Left Arrow
  Move Right         Right Arrow
  Jump               Up Arrow
  Primary Attack     Numpad 7
  Secondary Attack   Numpad 8
  Special Ability    Numpad 9

------------------------------------------------------------------------

# Game Flow

1.  Launch the game
2.  Select **Multiplayer** from the main menu
3.  Player 1 selects a character with the mouse
4.  Player 2 selects a character using **Right Shift**
5.  Press **Enter** to start the fight
6.  Battle until one player's HP reaches **0**

------------------------------------------------------------------------

# Character

Currently available character:

-   **Black Ops**
    -   Bullet attack
    -   Rocket attack
    -   Vertical teleport ability

------------------------------------------------------------------------

# Maps

Current playable map:

-   **Grass Land**

Unused maps included in project assets:

-   Final Destination
-   Yoshi's Island
-   Green Greens

------------------------------------------------------------------------

# Installation

## Requirements

-   Python 3
-   Pygame

Install pygame:

``` bash
pip install pygame
```

------------------------------------------------------------------------

# Running the Game

Run the main Python file:

``` bash
python platform_warriors.py
```

Make sure the following folders exist in the project directory:

    PW Images/
    PW Music/
    PW Maps/

These folders contain the required game assets.

------------------------------------------------------------------------

# Asset Credits

Images and assets used in this project come from various sources:

-   **Black Ops character** -- dreamstime.com
-   **Fight / Game text** -- Super Smash Bros Ultimate
-   **Question mark icon** -- Google Images
-   **Rocket sprite** -- Soul Knight
-   **Grass land map** -- Google Images
-   **Unused maps** -- Super Smash Bros Ultimate

Music:

-   **Thunderzone V2** by Waterflame

------------------------------------------------------------------------

# Known Issues

-   Collision detection occasionally behaves inconsistently
-   Some unused maps are not fully implemented
-   CPU opponent for singleplayer is not implemented
-   Limited character roster

------------------------------------------------------------------------

# Future Improvements

-   Add more characters
-   Implement singleplayer CPU AI
-   Improve collision detection
-   Add more maps
-   Implement animations for jumping and attacks
-   Improve UI and menus

------------------------------------------------------------------------

# Author

**Max Yang**
