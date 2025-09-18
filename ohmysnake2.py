import pygame
pygame.init()

#colors
white = (255,255,255) 
red = (255,0,0) 
black = (0,0,0) 


screen_width = 600
screen_height = 600

#creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#game title
pygame.display.set_caption("ohmysnake")
pygame.display.update()

#game specific variables
exit_game = False
game_over = False
snake_x= 45 #position of snake in x
snake_y = 55 #position of snake in y
snake_size = 10

fps = 30

clock = pygame.time.Clock() #we are making clock as we need time so that we can update our frames per second(time use krne ke liye time element toh chahiye hi)


#game loop 
while not exit_game:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN: #agar right key press kre toh 10 units aage jaega fir vapas 10 units but problem is ki dba ki rkhe toh nai chlega
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10
            
  


    gameWindow.fill(red)
    pygame.draw.rect(gameWindow,black, [snake_x,snake_y,snake_size,snake_size]) #for drawing a rectangle (screen,color,[])
    pygame.display.update()
    clock.tick(fps) #jitna bhi fps chahte ho idhar daaldo 

pygame.quit()
quit()





