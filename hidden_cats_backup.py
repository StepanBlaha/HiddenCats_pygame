pygame.init() 
  
color = (255, 255, 255)
offset = (0, 0)
size = (1600, 900)
surface = (1600, 900)
#create canvas
canvas = pygame.display.set_mode(size, pygame.RESIZABLE) 
#get your image
image = pygame.image.load("assets/Prosek.png")
image = pygame.transform.scale(image, surface)

pygame.display.set_caption("15 hidden cats on Prosek") 
exit = False
  
while not exit: 
    canvas.fill(color)
    canvas.blit(image, dest =offset)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        if event.type == pygame.VIDEORESIZE:
            
            surface = (event.w, event.h)
            image = pygame.transform.scale(image, surface)
            canvas.blit(image, dest =offset)
            
            
            
    pygame.display.update() 
    