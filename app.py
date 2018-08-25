import pygame
from display import Display

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

    def run(self):
        stop = False

        # Initial draw
        self.display.render()

        while not stop:
            # Deal with any queued events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True
                    break
                elif event.type == pygame.VIDEORESIZE:
                    # Rescale to match new size
                    new_size = event.dict['size']

                    self.display.resize(new_size)

            self.display.render()

if __name__ == "__main__":
    app = App()
    app.run()
