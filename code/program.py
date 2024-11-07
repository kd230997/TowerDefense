from models.main import Main
from models.configuration import Configuration
"""
How to run code

cd code
conda activate testEnv
python program.py

"""

"""
Game Idea
Zombie defense
Player will build the tower on the map to protect the house from zombie

Player: House Keeper
Map: Forest, Dessert, Water
Enemy: Red, Yellow, Blue (circle)

## Enemy will come from many waves, each wave more difficult
## The house will have 20 heart, if lose all, player lose
## Player have many tower type: Rectangle, Triangle, Hexagon

"""
if __name__ == "__main__":
    main = Main()
    main.run()
