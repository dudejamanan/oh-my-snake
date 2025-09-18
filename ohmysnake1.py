import pygame
pygame.init()

#colors
white = (255,255,255) #(R,G,B) , values hoti hai 0 to 255 , so so white light mei sab hota hai toh (255,255,255)
red = (255,0,0) #(R,G,B) , (255,0,0) because sirf red hi hai 
black = (0,0,0) #(R,G,B) koi color ni hai


screen_width = 1200
screen_height = 600

#creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#game title
pygame.display.set_caption("ohmysnake")
pygame.display.update()

#game specific variables
exit_game = False
game_over = False

#game loop 
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        
    
    gameWindow.fill(red)
    pygame.display.update()

pygame.quit()
quit()





