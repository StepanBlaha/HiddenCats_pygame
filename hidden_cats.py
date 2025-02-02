#pip install pygame
import pygame, sys
from main_menu import gamemenu


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
        
        self.font = pygame.font.Font(None, 75)
        self.clicked_cats = []
        self.text = ""
        self.stage =  "menu"
        
    def create_button(self, text, rect, color, action):
        """
        Creates a button with given properties.
        
        Parameters:
        text (str): The text displayed on the button.
        rect (tuple): A tuple (x, y, width, height) defining the button's position and size.
        color (str): The color of the button.
        action (function): The function executed when the button is clicked.
        
        Returns:
        list: A list containing button attributes.
        """
        #Create button rectangle
        button_rect = pygame.Rect(rect)
        #Create text to be put into button
        button_text = self.font.render(text, True, "black")
        #Rectangle with the text
        text_rect = button_text.get_rect(center=button_rect.center)
        return [button_text, text_rect, button_rect, color, action, False]
    
    def button_check(self, info, event):
        """
        Checks for button interaction (hover and click).
        
        Parameters:
        info (list): The button's attribute list.
        event (pygame.event.Event): The event to check.
        """
        #Get the button info
        button_text, text_rect, button_rect, color, action, hover = info
        
        #Checks for mouse motion
        if event.type == pygame.MOUSEMOTION:
            #If mouse motion colides with the rectangle sets hover to true
            info[-1] =  button_rect.collidepoint(event.pos)
        
        #Checks for mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            #If hover is true and action is set, runs the action
            if hover and action:
                action()
        
    def button_draw(self, screen, info):
        """
        Draws a button on the screen.
        
        Parameters:
        screen (pygame.Surface): The game window surface.
        info (list): The button's attribute list.
        """
        #Get the button info
        button_text, text_rect, button_rect, color, action, hover = info
        #Draw the button
        pygame.draw.rect(self.GAMEWINDOW, color, button_rect )
        #Draw the text into the button
        self.GAMEWINDOW.blit(button_text, text_rect)
        
    def on_click_start_game(self):
        """Handles the start game button click event."""
        self.stage = "game"
        print("Accessed game")
    
    def on_click_options(self):
        """Handles the options button click event."""
        self.stage = "options"
        print("Accessed options")
        
    def on_click_menu(self):
        """Handles the menu button click event."""
        self.stage = "menu"
        print("Accessed menu")
        
    def initialize_menu_buttons(self):
        """
        Creates and returns menu buttons.
        
        Returns:
        list: A list containing the menu buttons.
        """
        #Dynamic centering
        centeredWidth = ( self.window_width / 2 ) - 100
        #Creates the buttons
        button_start = self.create_button("GAME", (centeredWidth, 100, 200, 75), "red", self.on_click_start_game)
        button_options = self.create_button("OPTIONS", (centeredWidth - 50, 200, 300, 75), "red", self.on_click_options)
        return [button_start, button_options]
    
    def initialize_game_buttons(self):
        """
        Creates and returns the game screen buttons.
        
        Returns:
        list: The menu button.
        """
        #Dynamic centering
        centeredWidth = self.window_width - 170
        #Creates the menu button
        button_menu =  self.create_button("Menu", (centeredWidth, 30, 150, 75), "red", self.on_click_menu)
        return button_menu
        
    def create_menu(self):
        """
        Creates and runs the menu screen, handling events and rendering buttons.
        """
        #Setup the buttons
        button_start, button_options = self.initialize_menu_buttons()
        while True:   
            #Checks for quiting the game
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                
                #If stage == menu checks for colisions with the buttons
                if self.stage == "menu":
                    self.button_check(button_start, event)
                    self.button_check(button_options, event)
                    
                #Check for resize
                if event.type == pygame.VIDEORESIZE:
                    button_start, button_options = self.initialize_menu_buttons()
                    self.create_window(event.w, event.h)
                    self.create_collision_boxes(event.w, event.h)

            #If stage == menu draws the buttons 
            self.GAMEWINDOW.fill("white")
            if self.stage == "menu":
                self.button_draw(self.GAMEWINDOW, button_start)
                self.button_draw(self.GAMEWINDOW, button_options)
                
            #If stage is changed to game, draws the game
            elif self.stage == "game":
                self.create_game()
            pygame.display.update() 
                
    def create_game(self):
        """
        Creates and runs the game screen, handling events, rendering the counter, and drawing buttons.
        """
        #Setup the menu button
        button_menu = self.initialize_game_buttons()
        #Initial game setup
        self.create_image(self.window_width, self.window_height)
        self.create_collision_boxes(self.window_width, self.window_height)
        self.create_window(self.window_width, self.window_height)
        self.create_collision_boxes(self.window_width, self.window_height)
        while True:
            #Offsets for centering the counter
            widthOffset = self.window_width - 240
            heightOffset = 50
            #Draw the rectangle behind counter
            pygame.draw.rect(self.GAMEWINDOW, "white", (widthOffset, heightOffset, 80, 50))
            #Sets the counter text
            self.text = self.font.render(str(len(self.clicked_cats)), True, "red")
            #Draws the counter
            self.GAMEWINDOW.blit(self.text, [widthOffset, heightOffset])
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                
                #If stage == game checks for colisions with the menu button
                if self.stage == "game":
                    self.button_check(button_menu, event)
                
                #Check for resize
                if event.type == pygame.VIDEORESIZE:
                    button_menu = self.initialize_game_buttons()
                    self.create_window(event.w, event.h)
                    self.create_collision_boxes(event.w, event.h)
                    
                #Check for mousedown
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Get mouse position
                    x, y =pygame.mouse.get_pos()
                    #Check for colisions
                    self.check_for_collisions(x, y)
            
            #If stage == game draws the menu button
            if self.stage == "game":
                self.button_draw(self.GAMEWINDOW, button_menu)
                
            #If stage is changed to menu, draws the menu
            elif self.stage == "menu":
                self.create_menu()
            pygame.display.update() 

              
    def run(self):
        """
        Runs the game by launching the appropriate stage.
        """
        #Run the currrent stage
        if self.stage =="menu":
            self.create_menu()
        elif self.stage == "game":
            self.create_game()
        
        
        
        
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
                if i not in self.clicked_cats:
                    self.clicked_cats.append(i)
                self.collision_box_list[i]["clicked"] = True
                # Highlight the clicked box
                pygame.draw.rect(self.GAMEWINDOW, self.collision_box_border_color, collision_box, 4)
                return
        
        
        
if __name__ == '__main__':
    game = hiddencats()
    game.run()