


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


clock = pygame.time.Clock() 

font = pygame.font.SysFont(None,50) 

def text_screen(text,color,x,y):  
    screen_text = font.render(text,True,color) 
    gameWindow.blit(screen_text,[x,y]) 

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color, [x,y,snake_size,snake_size])
    



def game_loop():
    
    #game specific variables
    exit_game = False
    game_over = False
    snake_x= 45
    snake_y = 55
    snake_size = 12
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x= random.randint(20,screen_width-20)
    food_y = random.randint(20,screen_height-20) 
    foodsize = 12
    init_velocity = 5
    score = 0

    snk_list = [] 
    snk_length = 1 #initial length of snake

    #game loop 
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("game over! press enter to continue",red,10, 270)
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT: 
                    exit_game = True 
                    
                if event.type == pygame.KEYDOWN: #press any key to continue after game over
                    game_loop()

        else:
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    exit_game = True
            
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
        
            snake_x= snake_x + velocity_x 
            snake_y = snake_y + velocity_y 
        
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score+=1
                print("score is", score)
                food_x= random.randint(20,screen_width-20)
                food_y = random.randint(20,screen_height-20) 
                snk_length+=5


            gameWindow.fill(red)
            text_screen("score: "+str(score*10),black,5,5) #calling the function 
        

            head = [] #this is head of the snake #first list of snk_list
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head) #head is added to snk_length

            if len(snk_list)>snk_length: #because snake_x and snake_y toh change hore hai toh if hum usse pehle wale head del ni krenge toh length badhti jayegi
                del snk_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height: #taaki if boundary touch kre toh out hojaye
                game_over = True

            if head in snk_list[:-1]: #if head is pehle in snk_list mtlb jo nya head aaya hai vo pele se exist krta hai mtlb snake khud pe touchh hua so out hojaega
                game_over = True  

            pygame.draw.rect(gameWindow,white,[food_x,food_y,foodsize,foodsize]) 

            plot_snake(gameWindow,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()    
game_loop()






