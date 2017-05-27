# Class for storing the labyrinth

from Tile import Tile

class Lab(object):

    def __init__(self, h=None, w=None, start=None, tiles=None):
        self.h = h
        self.w = w
        self.start = start
        self.tiles = tiles

    def __repr__(self):
        r = "w:     {0}\n" \
            "h:     {1}\n" \
            "start: {2}\n" \
            "tiles: {3}".format(self.w, self.h, self.start, self.tiles)
        return r

    def __str__(self):

        res = "h: {0} | w: {1} | start: {2}".format(self.h, self.w, self.start)

        if self.tiles is not None:

            for row in self.tiles:
                s = "\n"

                for tile in row:

                    if tile.t is None:
                        s += "N"

                    else:
                        s += tile.t

                res += s

        else:
            res += "\nNo map"

        return res
