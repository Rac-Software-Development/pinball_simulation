# pinball_simulation 
Een flipperkast simulatie van Dylan Mendes Freire (1024040)

This project simulates a pinball game using Python, Pygame and Pymunk for physics handling. It includes features such as flippers, bumpers, targets and more, along with MQTT integration for live score updates and game events.

# Overview
This project is a simulation of a pinball game where the player controls flippers to keep the ball in play. The game includes obstacles such as bumpers, slingshots, and targets that interact witth the ball. Players score points by hitting the targets. The game uses Pygame for the graphical interface and pymunk for the physics simulation.

# Key features
1. Flippers: Control left and right flippers by using the keys (<-) and (->).
2. Bumpers: Bounce the ball back for maintaining a crazy dynamic in game.
3. Targets: Hit the targets to earn points
4. Slingshots: Bounce the ball back in the game.
5. Ball physics: Realistic ball physics and collisions
6. Scoreboard: Track score and lives, with a highscore between sessions
7. MQTT integration: send real-time score updates and game events over MQTT (I've used mosquitto).

# other features:
1. Gravity and Damping: simulated gravity and velocity damping for realistic ball movement.
2. collision handling: Detects collisions between the ball, targets, bumpers, and other game components.
3. Game Over Screen: Displays the final score and highscore, with options to either restart or quit.

# Installation

Requirements:
 1. Python above version 3
 2. Pygame
 3. Pymunk
 4. paho-mqtt (for MQTT communication)

steps:
 1. clone this repository (either from https or SSH) into your IDE of choice

 2. install the required dependencies:
  pip install pygame
  pip install pymunk
  pip install paho-mqtt

3. Run the game:
  python main.py

# How to play
1. Launch the game: After running the game, the simulation starts with the ball in play.
2. Control the flippers: Use the left arrow key (<-) to control the left flipper and the right arrrow key (->) to control the right flipper
3. Score pointsL Hit targets to score points. The scoreboard shows your current score and remaining lives
4. Lose a life: If the ball falls out of play (bounds) you lose a life. The game ends when all lives are lost.
5. Game Over: The game will display a "Game Over" screen, showing your score and the highscore. You can restart the game or quit.

# MQTT Integration
 This simulation includes MQTT communication to send score updates and game events to an MQTT Broker. The two main topics are:
    1. pinball/score: Sends the current score to the MQTT broker
    2. pinball/game: sends game events like bumper hits


# Credits:
1. Pygame: Used for the graphical interface and event handling.
2. pymunk: Provides physics simulation for realistic ball movements and collisions
3. paho-mqtt: Handles MQTT communication for sending real-time game data. 

Sources that I've used for this project:
1. https://www.pymunk.org/en/latest/
2. https://docs.python.org/3/library/index.html
3. ChatGPT.com for debugging purposes
4. YouTube with the following videos:
    1. https://www.youtube.com/watch?v=y9VG3Pztok8
    2. https://www.youtube.com/watch?v=tLsi2DeUsak
    3. https://www.youtube.com/watch?v=5j0uU3aJxJM

5. https://mosquitto.org/download/


