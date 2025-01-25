#pip install pygame
import pygame, sys


class hiddencats:
    def __init__(self):
        pygame.init()
        self.collision_box_list = [
            {
                "position": (39, 55),
                "dimension": (19, 18)
            },
            {
                "position": (1117, 145),
                "dimension": (40, 33)
            },
            {
                "position": (868, 264),
                "dimension": (11, 13)
            },
            {
                "position": (785, 449),
                "dimension": (30, 31)
            },
            {
                "position": (332, 345),
                "dimension": (25, 42)
            },
            {
                "position": (395, 599),
                "dimension": (38, 36)
            },
            {
                "position": (230, 642),
                "dimension": (15, 18)
            },
            {
                "position": (285, 725),
                "dimension": (35, 25)
            },
            {
                "position": (440, 950),
                "dimension": (25, 25)
            },
            {
                "position": (753, 666),
                "dimension": (31, 36)
            },
            {
                "position": (1013, 645),
                "dimension": (12, 20)
            },
            {
                "position": (1294, 648),
                "dimension": (30, 21)
            },
            {
                "position": (1394, 770),
                "dimension": (30, 22)
            },
            {
                "position": (914, 898),
                "dimension": (16, 17)
            },
            {
                "position": (1362, 418),
                "dimension": (29, 22)
            }
        ]
        self.collision_box_border_color = (0, 0, 0)
        self.window_color = (255, 255, 255)
        self.window_height = 900
        self.window_width = 1600
        self.image = pygame.image.load("assets/Prosek.png")
        self.initial_window_height = self.image.get_size()[1]
        self.initial_window_width = self.image.get_size()[0]
        self.image = pygame.transform.scale(self.image, (self.window_width, self.window_height))
        self.GAMEWINDOW = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE) 
        self.GAMEWINDOW.fill(self.window_color)
        self.create_image(self.window_width, self.window_height)
        self.create_collision_boxes(self.window_width, self.window_height)
            
              
    def run(self):
        while True:  
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                    
                if event.type == pygame.VIDEORESIZE:
                    self.create_window(event.w, event.h)
                    self.create_collision_boxes(event.w, event.h)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y =pygame.mouse.get_pos()
                    print(f'mouse clicked at {x}, {y}')
            pygame.display.update() 
        
    def create_window(self, width, height):
        pygame.display.set_caption("15 hidden cats on Prosek") 
        self.GAMEWINDOW = pygame.display.set_mode((width, height), pygame.RESIZABLE) 
        self.GAMEWINDOW.fill(self.window_color)
        self.create_image(width, height)
        
    def create_collision_boxes(self, width, height):
        for i in range( len(self.collision_box_list)):
                height_scale = height / self.initial_window_height
                width_scale = width / self.initial_window_width
                scaled_position = (self.collision_box_list[i]["position"][0] * width_scale , self.collision_box_list[i]["position"][1] * height_scale)
                scaled_dimension = (self.collision_box_list[i]["dimension"][0] * width_scale , self.collision_box_list[i]["dimension"][1] * height_scale)
                collision_box = pygame.Rect(scaled_position, scaled_dimension)
                pygame.draw.rect(self.GAMEWINDOW, self.collision_box_border_color, collision_box, 1)
        
    def create_image(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.GAMEWINDOW.blit(self.image, dest = (0, 0))
        
        
        
if __name__ == '__main__':
    hiddencats().run()