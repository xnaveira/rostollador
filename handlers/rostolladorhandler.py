from random import randint


class RostolladorHandler:
    def __init__(self, p):
        self.p = p

    def _prob(self):
        r = randint(0, 100)
        if r <= self.p:
            return True
        else:
            return False