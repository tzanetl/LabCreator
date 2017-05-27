# Class for storing the labyrinth


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
