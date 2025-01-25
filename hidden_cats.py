#pip install pygame
import pygame, sys


class hiddencats:
    """
    A class to represent the hidden cats game.

    This game displays an image with several invisible "collision boxes" that represent hidden cats.
    When a user clicks on a box, it gets highlighted, indicating that the cat has been found.

    Attributes:
        collision_box_list (list): List of dictionaries representing each collision box with its properties.
        collision_box_border_color (tuple): RGB color for the border of collision boxes when clicked.
        window_color (tuple): RGB color for the game window background.
        window_height (int): Initial height of the game window.
        window_width (int): Initial width of the game window.
        image (pygame.Surface): Loaded and scaled image for the game background.
        initial_window_height (int): Original height of the loaded image.
        initial_window_width (int): Original width of the loaded image.
        GAMEWINDOW (pygame.Surface): The main game window surface.
    """
    
    def __init__(self):
        """
        Initializes the game by setting up the collision boxes, window, and background image.
        """
        pygame.init()
        self.collision_box_list = [
            {"clicked": False, "position": (39, 55), "dimension": (19, 18), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (1117, 145), "dimension": (40, 33), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (868, 264), "dimension": (11, 13), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (785, 449), "dimension": (30, 31), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (332, 345), "dimension": (25, 42), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (395, 599), "dimension": (38, 36), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (230, 642), "dimension": (15, 18), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (285, 725), "dimension": (35, 25), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (440, 950), "dimension": (25, 25), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (753, 666), "dimension": (31, 36), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (1013, 645), "dimension": (12, 20), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (1294, 648), "dimension": (30, 21), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (1394, 770), "dimension": (30, 22), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (914, 898), "dimension": (16, 17), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
            {"clicked": False, "position": (1362, 418), "dimension": (29, 22), "scaled_dimension": (0, 0), "scaled_position": (0, 0)},
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
        """
        The main game loop. Handles events like window resizing and mouse clicks.
        """
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
                    self.check_for_collisions(x, y)
            pygame.display.update() 
        
    def create_window(self, width, height):
        """
        Updates the game window dimensions and redraws the background image.

        Args:
            width (int): The new width of the window.
            height (int): The new height of the window.
        """
        self.window_height = height
        self.window_width = width
        pygame.display.set_caption("15 hidden cats on Prosek") 
        self.GAMEWINDOW = pygame.display.set_mode((width, height), pygame.RESIZABLE) 
        self.GAMEWINDOW.fill(self.window_color)
        self.create_image(width, height)
        
    def create_collision_boxes(self, width, height):
        """
        Scales and redraws the collision boxes based on the current window dimensions.

        Args:
            width (int): The current window width.
            height (int): The current window height.
        """
        for i in range( len(self.collision_box_list)):
            
                height_scale = height / self.initial_window_height
                width_scale = width / self.initial_window_width
                
                scaled_position = (self.collision_box_list[i]["position"][0] * width_scale , self.collision_box_list[i]["position"][1] * height_scale)
                scaled_dimension = (self.collision_box_list[i]["dimension"][0] * width_scale , self.collision_box_list[i]["dimension"][1] * height_scale)
                
                self.collision_box_list[i]["scaled_position"] = scaled_position
                self.collision_box_list[i]["scaled_dimension"] = scaled_dimension
                
                collision_box = pygame.Rect(scaled_position, scaled_dimension)
                if self.collision_box_list[i]["clicked"] == True:
                    pygame.draw.rect(self.GAMEWINDOW, self.collision_box_border_color, collision_box, 4)
                
        
    def create_image(self, width, height):
        """
        Rescales and redraws the background image to fit the window.

        Args:
            width (int): The current window width.
            height (int): The current window height.
        """
        self.image = pygame.transform.scale(self.image, (width, height))
        self.GAMEWINDOW.blit(self.image, dest = (0, 0))
        
    def check_for_collisions(self, x, y):
        """
        Checks if the mouse click collides with any of the collision boxes.

        Args:
            x (int): The x-coordinate of the mouse click.
            y (int): The y-coordinate of the mouse click.
        """
        for i in range( len(self.collision_box_list)):
            
            scaled_position = self.collision_box_list[i]["scaled_position"]
            scaled_dimension = self.collision_box_list[i]["scaled_dimension"]
            
            collision_box = pygame.Rect(scaled_position, scaled_dimension)
            if collision_box.collidepoint(x, y):
                print("Collision detected with box", i)
                self.collision_box_list[i]["clicked"] = True
                # Highlight the clicked box
                pygame.draw.rect(self.GAMEWINDOW, self.collision_box_border_color, collision_box, 4)
                return
        
        
        
if __name__ == '__main__':
    hiddencats().run()