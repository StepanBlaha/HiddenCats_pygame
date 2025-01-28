import pygame
import sys


class gamemenu:
    def __init__(self, game_object):
        pygame.init()
        self.menu_state = True
        self.game_object = game_object
        self.menu_color = (255, 0, 0)
        self.menu_box = pygame.Rect(30, 30, 60, 60)
    
    def run(self):
        self.create_menu()
        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y =pygame.mouse.get_pos()
                    self.close_menu(x, y)
                    
            pygame.display.update() 



    def create_menu(self):
        pygame.draw.rect(self.game_object, self.menu_color, self.menu_box)
        pygame.display.flip()

    def close_menu(self, x, y):
        if self.menu_box.collidepoint(x, y):
            print("collisoimn")
        