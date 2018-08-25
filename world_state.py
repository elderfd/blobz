from random import random
from blob import Blob


class WorldState:
    def __init__(self):
        self.blobs = []

    @staticmethod
    def generate_random_state():
        new_state = WorldState()

        number_of_blobs = 3

        for _ in range(number_of_blobs):
            new_state.blobs.append(Blob(x = random(), y = random()))

        return new_state
