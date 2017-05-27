# class for storing the tiles in the lab


class Tile(object):
    def __init__(self, weight=None, type=None):
        self.weight = weight
        self.type = type

    def __str__(self):
        s1 = "None"
        s2 = "None"

        if self.weight is not None:
            s1 = self.weight

        if self.type is not None:
            s2 = self.type

        s = "Weight: {0}\n" \
            "Type:  \"{1}\"".format(s1, s2)
        return s
