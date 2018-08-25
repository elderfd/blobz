import pygame
from util import msecs_since_epoch


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

    def resize(self, new_size):
        pygame.display.set_mode(new_size, self.screen_options)
        self.render()

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

    def render(self, force = False):
        # pygame.draw.rect(self.screen, colour, rect)

        # pygame.draw.line(self.screen, black, startCoords, endCoords)

        if not force and msecs_since_epoch() - self.time_of_last_draw < self.min_time_between_frames:
            return

        pygame.display.update()
