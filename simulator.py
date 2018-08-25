from world_state import WorldState


class Simulator:
    def __init__(self):
        self.current_state = WorldState.generate_random_state()

    def get_next_state(self):
        # TODO: calculate something

        return self.current_state
