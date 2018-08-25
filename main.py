import pygame
import datetime

# Gives the current number of milliseconds since epoch
def msecs_since_epoch():
    epoch = datetime.datetime(1970, 1, 1)
    diff = datetime.datetime.now() - epoch
    return (diff.microseconds * 1000)


# Provides the display for the simulation and allows interaction
class Display:
    def __init__(self, max_fps):
        # Set up pygame stuff first
        pygame.init()

        # Some defaults
        default_window_width = 500
        default_window_height = 500

        self.screen_options = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

        pygame.display.set_caption("Blobz")
        
        self.screen = pygame.display.set_mode(
            [default_window_width, default_window_height],
            self.screen_options
        )

        self.inSetUpMode = True
        self.buttonPressedInWindow = False

        self.min_time_between_frames = 1 / max_fps
        self.time_of_last_draw = 0

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

    def render(self):
        # pygame.draw.rect(self.screen, colour, rect)

        # pygame.draw.line(self.screen, black, startCoords, endCoords)

        pygame.display.update()

    def run(self):
        stop = False

        # Initial draw
        self.render()

        while not stop:
            # Deal with any queued events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True
                    break
                elif event.type == pygame.VIDEORESIZE:
                    # Rescale to match new size
                    newRes = event.dict['size']
                    pygame.display.set_mode(newRes, self.screen_options)

                    self.render()
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                    # self.buttonPressed = event.button
                    # self.buttonPressedInWindow = True
                    # self.buttonPressCoords = pygame.mouse.get_pos()
                # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # If running then pause, otherwise start running
                    # self.simulating = not self.simulating
                    # self.render()

            # Make sure we don't render too quickly
            if msecs_since_epoch() - self.time_of_last_draw > self.min_time_between_frames:
                self.render()

if __name__ == "__main__":
    d = Display(60)
    d.run()

#poop