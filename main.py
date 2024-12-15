from settings import *

from snake import Snake

class Main:
    def __init__(self):
        
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        #Window title
        pygame.display.set_caption('Python Snake')

        #game objects
        self.bg_rects = [pygame.Rect((col + int(row % 2 == 0)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) for col in range(0,COLS,2) for row in range(ROWS)]

        self.snake = Snake()

        """
        This is just a small change for test my git repo
        """
        

    def drawbg(self):
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN, rect)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.display_surface.fill(LIGHT_GREEN)
            self.drawbg()
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()