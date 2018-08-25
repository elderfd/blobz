import pygame


class Display:
    """Provides the display for the simulation and allows interaction"""
    def __init__(self, window_width, window_height, max_fps):
        self.screen_options = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

        # TODO: tidy up so not calling this multiple times
        self.screen = pygame.display.set_mode((window_width, window_height), self.screen_options)

        self.load_resources()

        pygame.display.set_caption("Blobz")

        self.last_state = None

        self.resize((window_width, window_height))

        self.min_time_between_frames = 1 / max_fps
        self.time_of_last_draw = 0

    def load_resources(self):
        self.raw_blob_image = pygame.image.load("Resources/basic_blob.png").convert_alpha()

    def resize(self, new_size):
        self.window_width = new_size[0]
        self.window_height = new_size[1]

        self.screen = pygame.display.set_mode(new_size, self.screen_options)

        desired_blob_x_perc = 0.05
        desired_blob_y_perc = 0.05

        self.blob_image = pygame.transform.scale(
            self.raw_blob_image,
            (
                int(desired_blob_x_perc * self.window_width),
                int(desired_blob_y_perc * self.window_height)
            )
        )

        if self.last_state is not None:
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

    def world_to_display_coords(self, x, y):
        new_x = int(x * self.window_width)
        new_y = int(y * self.window_height)

        return (new_x, new_y)

    def render(self, world_state):
        self.last_state = world_state
        # pygame.draw.rect(self.screen, colour, rect)

        # pygame.draw.line(self.screen, black, startCoords, endCoords)

        # TODO: Draw the world
        self.screen.fill([255, 255, 255])

        for blob in world_state.blobs:
            self.screen.blit(
                self.blob_image,
                self.world_to_display_coords(blob.x, blob.y)
            )

        pygame.display.update()
