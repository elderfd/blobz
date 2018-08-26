from world_state import WorldState
from random import random
from blob import Blob, MovementDirection
from math import sqrt


class Simulator:
    def __init__(self):
        self.current_state = WorldState.generate_random_state()

    def get_next_state(self):
        max_step_size = Blob.radius * 2
        
        for blob in self.current_state.blobs:
            x_step = random() * 2 * max_step_size - max_step_size
            y_step = random() * 2 * max_step_size - max_step_size

            if x_step < 0:
                blob.movement_direction = MovementDirection.LEFT
            elif x_step > 0:
                blob.movement_direction = MovementDirection.RIGHT

            blob.x += x_step
            blob.y += y_step

            if blob.x + blob.radius > 1:
                blob.x = 1 - blob.radius
            elif blob.x - blob.radius < 0:
                blob.x = blob.radius

            if blob.y + blob.radius > 1:
                blob.y = 1 - blob.radius
            elif blob.y - blob.radius < 0:
                blob.y = blob.radius

        for i in range(len(self.current_state.blobs) - 1):
            for j in range(i + 1, len(self.current_state.blobs)):
                blob_i = self.current_state.blobs[i]
                blob_j = self.current_state.blobs[j]
                
                distance_between = sqrt((blob_i.x - blob_j.x) ** 2 + (blob_i.y - blob_j.y) ** 2)

                have_collided = distance_between < 2 * Blob.radius

                if have_collided:
                    # TODO
                    pass

        return self.current_state
