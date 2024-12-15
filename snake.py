from settings import *

class Snake:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(START_COL - col,START_ROW) for col in range(START_LENGHT)]
        print(self.body)
        