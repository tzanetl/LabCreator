# Function for handling the labyrinth


from random import randint
from Lab import Lab
from Tile import Tile
from Connection import Connection


# Generate labyrinth
def labgen(lab):

    for i in range(lab.h * lab.h):
        con = Connection(0, 0, 0, 0, lab.maxweight + 1)

        for m in range(lab.h):

            for n in range(lab.w):

                if lab.tiles[m][n].type == " ":
                    con = lookaround(lab, con, m, n)

        if con.weight < lab.maxweight:
            lab.tiles[con.m][con.n].type = " "

    return lab


# Adds direction to the Conncetion
def getdir(con):

    if con.m > con.to_m:
        return

    return con


# Decides if tile needs to be wall or " "
def deftype(lab):

    return lab


# Looks around the " " tile for tile weights
def lookaround(lab, con, m, n):

    # Look up
    if m - 1 >= 0:
        con = look(lab.tiles, con, m - 1, n, m, n)

    # Look down
    if m + 1 < lab.h:
        con = look(lab.tiles, con, m + 1, n, m, n)

    # Look left
    if n - 1 >= 0:
        con = look(lab.tiles, con, m, n - 1, m, n)

    # Look right
    if n + 1 < lab.w:
        con = look(lab.tiles, con, m, n + 1, m, n)

    return con


# Checks is Tile.type is None and if its lower weight than current
def look(tiles, con, m, n, to_m, to_n):

    if tiles[m][n].type is None and tiles[m][n].weight < con.weight:
        con = Connection(m, n, to_m, to_n, tiles[m][n].weight)

    return con


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
