# Function for handling the labyrinth


from random import randint
from Lab import Lab
from Tile import Tile


#Initializes tiles with weights and types
def labinit(h, w, start):
    lab = Lab()
    tiles = []

    for m in range(h):
        row = []

        for n in range(w):
            tile = Tile(randint(1, 100))
            row.append(tile)

        tiles.append(row)

    lab.tiles = tiles
    return lab
