# Function for handling the labyrinth


from random import randint
from Lab import Lab
from Tile import Tile


# Generate labyrinth
def labgen(lab):

    for i in range(lab.h * lab.h):
        least = [lab.maxweight + 1, 0, 0]

        for m in range(lab.h):

            for n in range(lab.w):

                if lab.tiles[m][n].type == " ":
                    least = lookaround(lab.tiles, least, m, n)

    return lab


# Looks around the " " tile for tile weights
def lookaround(tiles, least, m, n):

    return least


# Initializes tiles with weights and types
def labinit(h=11, w=None, start=None, maxweight = 10000):

    if w is None:
        w = 0 + h

    if start is None:
        start = int(h/2)

    tiles = []

    # Create a weighted Tile matrix
    for m in range(h):
        row = []

        for n in range(w):
            tile = Tile(randint(1, maxweight))
            row.append(tile)

        tiles.append(row)

    lab = Lab(h, w, start, maxweight, tiles)

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
