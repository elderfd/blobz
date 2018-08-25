from world_state import WorldState
from random import random
from blob import Blob


class Simulator:
    def __init__(self):
        self.current_state = WorldState.generate_random_state()

    def get_next_state(self):
        max_step_size = Blob.radius * 2
        
        for blob in self.current_state.blobs:
            blob.x += random() * 2 * max_step_size - max_step_size
            blob.y += random() * 2 * max_step_size - max_step_size

            if blob.x + blob.radius > 1:
                blob.x = 1 - blob.radius
            elif blob.x - blob.radius < 0:
                blob.x = blob.radius

            if blob.y + blob.radius > 1:
                blob.y = 1 - blob.radius
            elif blob.y - blob.radius < 0:
                blob.y = blob.radius

        return self.current_state
