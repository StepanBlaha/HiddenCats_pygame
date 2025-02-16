#pip install pygame
import random
import  os
import datetime
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
        self.cat_sound_list = ["meow_1.wav", "meow_2.wav",  "meow_3.wav",  "meow_4.wav",  "meow_5.wav",  "meow_6.wav"]
        self.window_color = (255, 255, 255)
        self.window_height = 900
        self.window_width = 1600
        self.button_color = "black"
        self.button_text_color = "white"
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
        
        self.sound_switch  = False
        self.sound_switch_button_style = 5
        self.seconds_counter = 0
        
    def play_sound(self):
        if not self.sound_switch:
            return
        random_index = random.randint(0, len(self.cat_sound_list) - 1)
        print(random_index)
        random_sound = self.cat_sound_list[random_index]
        sound_folder_path = "assets/cat_sounds"
        complete_path = os.path.join(sound_folder_path, random_sound)
        
        pygame.mixer.init()
        pygame.mixer.music.load(complete_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        
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
        button_text = self.font.render(text, True, self.button_text_color)
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
        
    def button_draw(self, screen, info, width = 0):
        """
        Draws a button on the screen.
        
        Parameters:
        screen (pygame.Surface): The game window surface.
        info (list): The button's attribute list.
        """
        #Get the button info
        button_text, text_rect, button_rect, color, action, hover = info
        #Draw the button
        pygame.draw.rect(self.GAMEWINDOW, color, button_rect , width, 5)
        #Draw the text into the button
        self.GAMEWINDOW.blit(button_text, text_rect)
        
    def on_click_start_game(self):
        """Handles the start game button click event."""
        for box in self.collision_box_list:
            box["clicked"] = False
        self.stage = "game"
        print("Accessed game")
        pygame.display.update()
    
    def on_click_options(self):
        """Handles the options button click event."""
        self.stage = "options"
        print("Accessed options")
        pygame.display.update()
        
    def on_click_menu(self):
        """Handles the menu button click event."""
        self.stage = "menu"
        print("Accessed menu")
        pygame.display.update()
        
    def on_click_replay_game(self):
        #Reset clicked boxes
        for box in self.collision_box_list:
            box["clicked"] = False
        self.stage = "game"
        print("Game restarted")
        pygame.display.update()
        
    def on_game_win(self):
         # Refresh to apply changes
        self.stage = "gameover"
        print("Game won")
        
    def set_sounds(self):
        self.sound_switch = not (self.sound_switch)
        if not self.sound_switch:
            self.sound_switch_button_style = 5
        else:
            self.sound_switch_button_style = 0
        
    def initialize_menu_buttons(self):
        """
        Creates and returns menu buttons.
        
        Returns:
        list: A list containing the menu buttons.
        """
        #Dynamic centering
        centeredWidth = ( self.window_width / 2 ) - 100
        #Creates the buttons
        button_start = self.create_button("GAME", (centeredWidth, 200, 200, 75), self.button_color, self.on_click_start_game)
        button_options = self.create_button("OPTIONS", (centeredWidth - 50, 300, 300, 75), self.button_color, self.on_click_options)
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
        button_menu =  self.create_button("Menu", (centeredWidth, 30, 150, 75), self.button_color, self.on_click_menu)
        return button_menu
    
    def initialize_play_again_button(self):
        #Dynamic centering
        centeredWidth = ( self.window_width / 2 ) - 100
        #Creates the play again button
        play_again_button =  self.create_button("Replay", (centeredWidth, 300, 200, 75), self.button_color, self.on_click_replay_game)
        menu_button = self.create_button("Menu", (centeredWidth, 400, 200, 75), self.button_color, self.on_click_menu)
        return [ play_again_button, menu_button ]
        
    def initialize_options_buttons(self):
        #Dynamic centering
        centeredWidth = self.window_width - 170
        #Positioning  for the sound button
        soundWidthOffset = self.window_width/2 + 100
        soundHeightOffset = 200
        
        #Creates the menu button
        button_menu =  self.create_button("Menu", (centeredWidth, 30, 150, 75), self.button_color, self.on_click_menu)
        button_sounds = self.create_button("", (soundWidthOffset, soundHeightOffset, 50, 50), self.button_color, self.set_sounds)
        return button_menu, button_sounds
    
    def create_options(self):
        
        #Setup the menu button
        button_menu, button_sounds = self.initialize_options_buttons()
        
        
        
        while True:   
            #Positions for the page title
            titleWidthOffset = self.window_width/2- 130
            titleHeightOffset = 100
            titleFont = pygame.font.Font(None, 100)
            #Positions for the settings text
            textWidthOffset = self.window_width/2- 230
            textHeightOffset = 200
            buttonWidthOffset = self.window_width/2+100
            buttonHeightOffset = 200
            #Draw the rectangle behind counter
            pygame.draw.rect(self.GAMEWINDOW, "white", (buttonWidthOffset, buttonHeightOffset, 140, 50))
            #Display title 
            self.text = titleFont.render(f"Settings", True, self.button_color)
            self.GAMEWINDOW.blit(self.text, (titleWidthOffset, titleHeightOffset))
            #Sets the counter text
            self.text = self.font.render(f"Cat sounds", True, self.button_color)
            #Draws the counter
            self.GAMEWINDOW.blit(self.text, (textWidthOffset, textHeightOffset))
            
            
            #Checks for quiting the game
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                
                #If stage == menu checks for colisions with the buttons
                if self.stage == "options":
                    self.button_check(button_menu, event)
                    self.button_check(button_sounds, event)
                    
                #Check for resize
                if event.type == pygame.VIDEORESIZE:
                    button_menu, button_sounds = self.initialize_options_buttons()
                    self.create_window(event.w, event.h)
                    self.create_collision_boxes(event.w, event.h)

            #If stage == menu draws the buttons 
            
            self.GAMEWINDOW.fill("white")
            self.text = titleFont.render(f"Settings", True, self.button_color)
            self.GAMEWINDOW.blit(self.text, (titleWidthOffset, titleHeightOffset))
            self.text = self.font.render(f"Cat sounds", True, self.button_color)
            self.GAMEWINDOW.blit(self.text, (textWidthOffset, textHeightOffset))
            
            if self.stage == "options":
                self.button_draw(self.GAMEWINDOW, button_menu)
                self.button_draw(self.GAMEWINDOW, button_sounds, self.sound_switch_button_style)
                
            #If stage is changed to game, draws the game
            elif self.stage == "menu":
                self.create_menu()
            pygame.display.update() 
        
    def create_menu(self):
        """
        Creates and runs the menu screen, handling events and rendering buttons.
        """
        #Setup the buttons
        button_start, button_options = self.initialize_menu_buttons()
        while True:   
            titleWidthOffset = self.window_width/2- 430
            titleHeightOffset = 100
            titleFont = pygame.font.Font(None, 100)
            self.text = titleFont.render(f"15 Hidden cats on Prosek", True, self.button_color)
            self.GAMEWINDOW.blit(self.text, (titleWidthOffset, titleHeightOffset))
            




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
            self.GAMEWINDOW.blit(self.text, (titleWidthOffset, titleHeightOffset))
            if self.stage == "menu":
                self.button_draw(self.GAMEWINDOW, button_start)
                self.button_draw(self.GAMEWINDOW, button_options)
                
            #If stage is changed to game, draws the game
            elif self.stage == "game":
                self.start_ticks = pygame.time.get_ticks()
                self.create_game()
                
            elif self.stage == "options":
                self.create_options()
            pygame.display.update() 
    
    def create_win_screen(self):
        
        self.clicked_cats = []
        surface = pygame.Surface((self.window_width, self.window_height))
        surface.set_alpha(180)
        surface.fill((255, 255, 255))
        
        self.GAMEWINDOW.blit(surface,  (0,  0)) # Paint the screen white
        
        
        
        
        print("gameover shown")
        #Setup the replay button
        play_again_button, menu_button = self.initialize_play_again_button()
        win_font = pygame.font.Font(None, 140)
        centeredWidth = ( self.window_width / 2 ) - 200
        win_text = win_font.render(f"You won", True, self.button_color)
        self.GAMEWINDOW.blit(win_text, (centeredWidth, 150))
        
        time_text = self.font.render(str(datetime.timedelta(seconds = self.seconds_counter)), True, "black")
        #pygame.draw.rect(self.GAMEWINDOW, "black", (( self.window_width / 2 ) - 115, 525, 230, 90))
        self.GAMEWINDOW.blit(time_text, (( self.window_width / 2 ) - 90, 500))
        #predtim 550
        
        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                
                
                if self.stage == "gameover":
                    self.button_check(play_again_button, event)
                    self.button_check(menu_button, event)
                
                #Check for resize
                if event.type == pygame.VIDEORESIZE:
                    play_again_button = self.initialize_play_again_button()
                    self.create_window(event.w, event.h)
                    self.create_collision_boxes(event.w, event.h)
                    
                #Check for mousedown
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Get mouse position
                    x, y =pygame.mouse.get_pos()
                    #Check for colisions
                    self.check_for_collisions(x, y)
            
            #If stage == game draws the menu button
                
            if self.stage == "gameover":
                self.button_draw(self.GAMEWINDOW, play_again_button)
                self.button_draw(self.GAMEWINDOW, menu_button)
            elif self.stage == "game":
                self.create_game()
            elif self.stage == "menu":
                self.create_menu()
            pygame.display.update()
        
                
    def create_game(self):
        """
        Creates and runs the game screen, handling events, rendering the counter, and drawing buttons.
        """
        #Setup the replay button
        play_again_button = self.initialize_play_again_button()
        #Setup the menu button
        button_menu = self.initialize_game_buttons()
        #Initial game setup
        print(self.clicked_cats)
        self.GAMEWINDOW.fill(self.window_color)
        pygame.display.update() 
        self.create_image(self.window_width, self.window_height)
        self.create_collision_boxes(self.window_width, self.window_height)
        self.create_window(self.window_width, self.window_height)
        self.create_collision_boxes(self.window_width, self.window_height)
        
        #Timer setup
        timer_interval = 1000
        timer_event = pygame.USEREVENT + 1 
        pygame.time.set_timer(timer_event, timer_interval)
        
        while True:

            #Offsets for centering the counter
            widthOffset = self.window_width - 330
            heightOffset = 50
            #Draw the rectangle behind counter
            pygame.draw.rect(self.GAMEWINDOW, "white", (widthOffset, heightOffset, 140, 50))
            #Gets the number of clicked  cats
            clicked_counter = len(self.clicked_cats)
            #Sets the counter text
            self.text = self.font.render(f"{clicked_counter}/15", True, self.button_color)
            #Draws the counter
            self.GAMEWINDOW.blit(self.text, (widthOffset, heightOffset))
            
            #Draw timer
            time_text = self.font.render(str(datetime.timedelta(seconds = self.seconds_counter)), True, self.button_color)
            pygame.draw.rect(self.GAMEWINDOW, "white", (self.window_width - 250, self.window_height - 120, 250, 80))
            self.GAMEWINDOW.blit(time_text, (self.window_width - 230, self.window_height - 100))
            
            if clicked_counter == 15:
                self.on_game_win()
               
               
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    #For exiting the window
                    sys.exit()
                
                elif event.type == timer_event:
                    self.seconds_counter +=1
                    time = str(datetime.timedelta(seconds = self.seconds_counter))
                    print(time)
                
                #If stage == game checks for colisions with the menu button
                if self.stage == "game":
                    self.button_check(button_menu, event)
                
                if self.stage == "gameover":
                    self.button_check(play_again_button, event)
                
                #Check for resize
                if event.type == pygame.VIDEORESIZE:
                    button_menu = self.initialize_game_buttons()
                    play_again_button = self.initialize_play_again_button()
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
                
            elif self.stage == "gameover":
                self.create_win_screen()
                
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
        elif self.stage  == "gameover":
            self.create_win_screen()
        elif self.stage == "options":
            self.create_options()
        
        
        
        
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
                    self.play_sound()
                self.collision_box_list[i]["clicked"] = True
                # Highlight the clicked box
                pygame.draw.rect(self.GAMEWINDOW, self.collision_box_border_color, collision_box, 4)
                return
        
        
        
if __name__ == '__main__':
    game = hiddencats()
    game.run()