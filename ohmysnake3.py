import random
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
snake_x= 45
snake_y = 55
snake_size = 12
fps = 30
velocity_x = 0
velocity_y = 0
food_x= random.randint(20,screen_width-20) #position of food in x .... 20 thoda extra isliye liya hai taaki jyada corner pr na jaaye food
food_y = random.randint(20,screen_height-20) #position of food in y 
foodsize = 12
score = 0

clock = pygame.time.Clock() 

#game loop 
while not exit_game:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                velocity_x = 8 #jab ek ki velocity then dusre ki 0
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -8
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -8
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 8
                velocity_x = 0
    
    snake_x= snake_x + velocity_x #position of x = position of x + 1
    snake_y = snake_y + velocity_y #position of y = position of y + 1
    if abs(snake_x-food_x)<4 and abs(snake_y-food_y)<4:
        score+=1
        print(score)



    gameWindow.fill(red)
    pygame.draw.rect(gameWindow,black, [snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow,white,[food_x,food_y,foodsize,foodsize]) 
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()





