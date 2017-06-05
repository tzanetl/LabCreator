# Class for storing the new connection


class Connection(object):

    def __init__(self, m=None, n=None, to_m=None, to_n=None, weight=None,
                 direction=None):
        self.m = m                  # m -cordinate of new tile
        self.n = n                  # n -cordinate of new tile
        self.to_m = to_m            # where it connects on the lab m -cord
        self.to_n = to_n            # where is connects on the lab n -cord
        self.weight = weight        # weight of the connecting tile
        self.direction = direction  # connection direction

    def __str__(self):
        s = "m: {0} | n: {1} | to_m: {2} | to_n: {3} | weight: {4} | dir: {5}"\
            .format(self.m, self.n, self.to_m, self.to_n, self.weight,
                    self.direction)
        return s