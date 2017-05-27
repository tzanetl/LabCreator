# Function for handling the labyrinth


from random import randint
from Lab import Lab
from Tile import Tile


# Initializes tiles with weights and types
def labinit(h=11, w=None, start=None):

    if w is None:
        w = 0 + h

    if start is None:
        start = int(h/2)

    tiles = []

    # Create a weighted Tile matrix
    for m in range(h):
        row = []

        for n in range(w):
            tile = Tile(randint(1, 100))
            row.append(tile)

        tiles.append(row)

    lab = Lab(h, w, start, tiles)

    # Add bottom and top walls
    for n in range(w):
        lab.tiles[0][n].type = "#"
        lab.tiles[h - 1][n].type = "#"

    # Add left wall
    for m in range(h):
        lab.tiles[m][0].type = "#"

    # Add starting point
    lab.tiles[start][0].type = " "

    return lab
