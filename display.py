import pygame


class Display:
    """Provides the display for the simulation and allows interaction"""
    def __init__(self, window_width, window_height, max_fps):
        self.screen_options = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

        pygame.display.set_caption("Blobz")
        
        self.screen = pygame.display.set_mode(
            [window_width, window_height],
            self.screen_options
        )

        self.min_time_between_frames = 1 / max_fps
        self.time_of_last_draw = 0

        self.last_state = None

    def resize(self, new_size):
        pygame.display.set_mode(new_size, self.screen_options)
        self.render(self.last_state)

    # Returns a Rect which matches the given grid x, y coordinates
    # def gridCoordsToDisplayRect(self, x, y):
    #     left = self.gridXToDisplayX(x)
    #     top = self.gridYToDisplayY(y)
    #     width = self.squareXSize + 2 * self.borderThickness
    #     height = self.squareYSize + 2 * self.borderThickness
    #     return pygame.Rect(left, top, width, height)

    # def gridXToDisplayX(self, x):
    #     return x * self.squareXSize + self.borderThickness

    # def gridYToDisplayY(self, y):
    #     return y * self.squareYSize + self.borderThickness

    def render(self, world_state):
        self.last_state = world_state
        # pygame.draw.rect(self.screen, colour, rect)

        # pygame.draw.line(self.screen, black, startCoords, endCoords)

        # TODO: Draw the world

        pygame.display.update()
