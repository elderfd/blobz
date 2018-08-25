import pygame
from blob import Blob


class Display:
    """Provides the display for the simulation and allows interaction"""
    def __init__(self, window_width, window_height, max_fps, debug_mode = False):
        self.debug_mode = debug_mode

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
        self.raw_blob_image = pygame.image.load("Resources/cut_blob.png").convert_alpha()

    def resize(self, new_size):
        self.window_width = new_size[0]
        self.window_height = new_size[1]

        self.screen = pygame.display.set_mode(new_size, self.screen_options)

        # TODO: Scale according to smaller dimension
        blob_aspect_ratio = self.raw_blob_image.get_width() / self.raw_blob_image.get_height()

        desired_blob_width = self.window_width * Blob.radius * 2
        desired_blob_height = desired_blob_width / blob_aspect_ratio

        self.blob_image = pygame.transform.scale(
            self.raw_blob_image,
            (
                int(desired_blob_width),
                int(desired_blob_height)
            )
        )

        if self.last_state is not None:
            self.render(self.last_state)

    def world_to_display_coords(self, x, y):
        new_x = int(x * self.window_width)
        new_y = int(y * self.window_height)

        return (new_x, new_y)

    def render(self, world_state):
        self.last_state = world_state

        self.screen.fill([255, 255, 255])

        for blob in world_state.blobs:
            centre_coords = self.world_to_display_coords(blob.x, blob.y)

            self.screen.blit(
                self.blob_image,
                (
                    centre_coords[0] - self.blob_image.get_width() // 2,
                    centre_coords[1] - self.blob_image.get_height() // 2
                )
            )
            
            if self.debug_mode:
                pygame.draw.circle(self.screen, [255, 0, 0], centre_coords, 5, 2)

        pygame.display.update()
