import pygame
from display import Display
from simulator import Simulator
from util import secs_since_epoch

class App:
    def __init__(self):
        # Set up pygame stuff first
        pygame.init()

        # Some defaults
        default_window_width = 500
        default_window_height = 500

        self.time_of_last_draw = 0

        self.display = Display(
            window_width = default_window_width,
            window_height = default_window_height,
            max_fps = 60
        )

        self.simulator = Simulator()

    def run(self):
        keep_going = True

        # Initial draw
        self.display.render(self.simulator.current_state)

        time_of_last_calculation = 0
        min_time_between_sim_steps = 1 / 2

        while keep_going:
            # Deal with any queued events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False
                    break
                elif event.type == pygame.VIDEORESIZE:
                    # Rescale to match new size
                    new_size = event.dict['size']

                    self.display.resize(new_size)

            time_now = secs_since_epoch()

            if time_now - time_of_last_calculation >= min_time_between_sim_steps:
                self.display.render(
                    self.simulator.get_next_state()
                )
                time_of_last_calculation = time_now


if __name__ == "__main__":
    app = App()
    app.run()
