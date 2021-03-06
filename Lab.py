# Class for storing the labyrinth


class Lab(object):

    def __init__(self, h=None, w=None, start=None, maxweight=None, tiles=None):
        self.h = h
        self.w = w
        self.start = start
        self.maxweight = maxweight
        self.tiles = tiles

    def __repr__(self):
        r = "w:         {0}\n" \
            "h:         {1}\n" \
            "start:     {2}\n" \
            "Maxweight: {3}\n" \
            "tiles:     {4}"\
                .format(self.w, self.h, self.start, self.maxweight, self.tiles)
        return r

    def __str__(self):

        res = "h: {0} | w: {1} | start: {2} | maxweight: {3}"\
            .format(self.h, self.w, self.start, self.maxweight)

        if self.tiles is not None:

            for row in self.tiles:
                s = "\n"

                for tile in row:

                    if tile.type is None:
                        s += "N"

                    else:
                        s += tile.type

                res += s

        else:
            res += "\nNo map"

        return res

    def map(self):

        if self.tiles is None:
            return None

        res = ""

        for row in self.tiles:
            s = ""

            for tile in row:

                if tile.type is None:
                    s += "N"

                else:
                    s += tile.type

            res += s + "\n"

        return res.rstrip()
