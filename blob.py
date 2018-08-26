from random import random
from uuid import uuid4 as uuid


class Blob:
    def __init__(self, x = 0, y = 0, colour = None):
        self.x = x
        self.y = y
        self.id = uuid()

        if colour is not None:
            self.colour = colour
        else:
            self.colour = (
                int(random() * 255),
                int(random() * 255),
                int(random() * 255)
            )

    radius = 0.025
