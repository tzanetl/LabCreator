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
                    least = lookaround(lab, least, m, n)

        if least[0] < lab.maxweight + 1:
            lab.tiles[least[1]][least[2]].type = " "

    return lab


# Decides if tile needs to be wall or " "
def deftype(lab):
    

    return lab


# Looks around the " " tile for tile weights
def lookaround(lab, least, m, n):

    # Look up
    if m - 1 >= 0:
        least = look(lab.tiles, least, m - 1, n)

    # Look down
    if m + 1 < lab.h:
        least = look(lab.tiles, least, m + 1, n)

    # Look left
    if n - 1 >= 0:
        least = look(lab.tiles, least, m, n - 1)

    # Look right
    if n + 1 < lab.w:
        least = look(lab.tiles, least, m, n + 1)

    return least


# Checks is Tile.type is None and if its lower weight than current
def look(tiles, least, m, n):

    if tiles[m][n].type is None and tiles[m][n].weight < least[0]:
        least[0] = tiles[m][n].weight
        least[1] = m
        least[2] = n

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
