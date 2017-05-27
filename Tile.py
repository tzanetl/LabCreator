# class for storing the tiles in the lab


class Tile(object):
    def __init__(self, weight=None, type=None):
        self.weight = weight
        self.t = type

    def __str__(self):
        s1 = "None"
        s2 = "None"

        if self.weight is not None:
            s1 = self.weight

        if self.t is not None:
            s2 = self.t

        s = "Weight: {0}\n" \
            "Type:  \"{1}\"".format(s1, s2)
        return s
