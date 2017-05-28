# Class for storing the new connection


class Connection(object):

    def __init__(self, m=None, n=None, to_m=None, to_n=None, weight=None):
        self.m = m
        self.n = n
        self.to_m = to_m
        self.to_n = to_n
        self.weight = weight

    def __str__(self):
        s = "m: {0} | n: {1} | to_m: {2} | to_n: {3} | weight: {4}"\
            .format(self.m, self.n, self.to_m, self.to_n, self.weight)
        return s