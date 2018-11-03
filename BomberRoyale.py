import pygame
import time
import random

print("hello")

pygame.init()

red = (255,0,0)
black = (0, 0, 0)
green = (143,188,143)
light_brown = (182, 155, 76)


Obst = []
Boxes = []


block_size = 35





display_width = 17 * block_size
display_height = 15 * block_size


empty_square_percentage = 0.2





FPS = 60


clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("BomberMan")

def create_obst(x, y):
     Rect = pygame.Rect(x, y, block_size, block_size)
     Obst.append(Rect)

def create_box(x, y):
    Rect = pygame.Rect(x, y, block_size, block_size)
    Boxes.append(Rect)

def get_possible_box_locations():
    locations = []
    for x in range(0, display_width, block_size):
        for y in range(0, display_height, block_size):
            locations.append((x, y))
    for part in Obst:
        if (part.x, part.y) in locations:
            locations.remove((part.x, part.y))

    # Remove player starting locations and adjacent squares
    locations.remove((block_size, block_size))
    locations.remove((2 * block_size, block_size))
    locations.remove((block_size, 2 * block_size))
    locations.remove((display_width - 2 * block_size, block_size))
    locations.remove((display_width - 3 * block_size, block_size))
    locations.remove((display_width - 2 * block_size, 2 * block_size))
    locations.remove((block_size, display_height - 2 * block_size))
    locations.remove((2 * block_size, display_height - 2 * block_size))
    locations.remove((block_size, display_height - 3 * block_size))
    locations.remove((display_width - 2 * block_size, display_height - 2 * block_size))
    locations.remove((display_width - 3 * block_size, display_height - 2 * block_size))
    locations.remove((display_width - 2 * block_size, display_height - 3 * block_size))
    return(locations)

def create_grid():
    for x in range(0, display_width, block_size):
        create_obst(x, 0)

    for x in range(0, display_width, block_size):
        create_obst(x, display_height - block_size)

    for y in range(0, display_height, block_size):
        create_obst(0, y)

    for y in range(0, display_height, block_size):
        create_obst(display_width - block_size, y)
    
    
    for x in range(2 * block_size, display_width - 2 * block_size, 2 * block_size):

        for y in range(2 * block_size, display_height - 2 * block_size, 2 * block_size):
            create_obst(x, y)

    locations = get_possible_box_locations()
    for i in range(int(empty_square_percentage * len(locations))):
            locations.pop(random.randint(0, len(locations) - 1))
    for (x, y) in locations:
        create_box(x, y) 


def draw_obst(rect):
    pygame.draw.rect(gameDisplay, black, rect)

def draw_box(rect):
    pygame.draw.rect(gameDisplay, light_brown, rect)

def draw_grid():
    gameDisplay.fill(green)
    for part in Obst:
        draw_obst(part)
    for part in Boxes:
        draw_box(part)
            

def gameLoop():

    
    create_grid()
   

    gameExit = False

    lead_x = block_size + block_size / 2
    lead_y = block_size + block_size / 2

    lead_x_change = 0
    lead_y_change = 0

    speed = 2.5


    while not gameExit:

        draw_grid()

        
        
        for event in pygame.event.get():
            
                  

            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -speed
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = speed
                    lead_y_change = 0
                    
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -speed
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = speed
                    lead_x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0


        lead_y += lead_y_change
        lead_x += lead_x_change

        

        
        player = pygame.Rect(lead_x,lead_y, 15, 15)
        

        for part in Obst + Boxes:
            if player.colliderect(part):
                
                if lead_x_change > 0:
                    player.right = part.left
                if lead_x_change < 0:
                    player.left = part.right
                if lead_y_change > 0:
                    player.bottom = part.top
                if lead_y_change < 0:
                    player.top = part.bottom

        lead_x = player.x
        lead_y = player.y
        
        pygame.draw.rect(gameDisplay, red, player)
                    
        

       
        

        
        pygame.display.update()

        clock.tick(FPS)

gameLoop()






















pygame.quit()
quit()













                
