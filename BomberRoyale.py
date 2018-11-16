import pygame
import time
import random

print("hello")

pygame.init()

red = (255,0,0)
black = (0, 0, 0)
green = (143,188,143)

bombimage = pygame.image.load("Vesipal.png")

Obst = []


block_size = 35





display_width = 17 * block_size
display_height = 15 * block_size


player = None
    





FPS = 60


clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("BomberMan")







def draw_obst(x, y):
    Rect = pygame.Rect(x, y, block_size, block_size)
    Obst.append(Rect)
    pygame.draw.rect(gameDisplay, black, Rect)

def draw_grid():
    gameDisplay.fill(green)

    for x in range(0, display_width, block_size):
        draw_obst(x, 0)

    for x in range(0, display_width, block_size):
        draw_obst(x, display_height - block_size)

    for y in range(0, display_height, block_size):
        draw_obst(0, y)

    for y in range(0, display_height, block_size):
        draw_obst(display_width - block_size, y)
    
    
    for x in range(2 * block_size, display_width - 2 * block_size, 2 * block_size):

        for y in range(2 * block_size, display_height - 2 * block_size, 2 * block_size):
            draw_obst(x, y)


class Bomb(object):
    def __init__(self, aposX, aposY, bombRange=5):
        self.posX = aposX 
        self.posY = aposY
        self.bombRange = bombRange
        self.timeToExplode = 3000

    def update(self, dt):
        # Subtract the passed time `dt` from the timer each frame.
        self.timeToExplode -= dt

    def explode(self, screen):
        pygame.draw.line(screen,(135,206,250),(self.posX,self.posY),(self.posX+block_size/2+(block_size*self.bombRange),self.posY),block_size)
        pygame.draw.line(screen,(135,206,250),(self.posX,self.posY),(self.posX-block_size/2-(block_size*self.bombRange),self.posY),block_size)
        pygame.draw.line(screen,(135,206,250),(self.posX,self.posY),(self.posX,self.posY+block_size/2+(block_size*self.bombRange)),block_size)
        pygame.draw.line(screen,(135,206,250),(self.posX,self.posY),(self.posX,self.posY-block_size/2-(block_size*self.bombRange)),block_size)

    def draw(self, screen):
        screen.blit(bombimage,(self.posX-0.5*bombimage.get_rect().width, self.posY-0.5*bombimage.get_rect().height))



      

def gameLoop():

    
    

    gameExit = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    speed = 2.5


    bomb_set = set()


    while not gameExit:


        dt = clock.tick(FPS)
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
                    
                elif event.key == pygame.K_x:
                    bomb_set.add(Bomb(*player.center))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0


        to_remove = set()
        
        for bomb in bomb_set:
            bomb.update(dt)
            # Add old bombs to the to_remove set.
            if bomb.timeToExplode <= -1000:
                to_remove.add(bomb)

        if to_remove:
            bomb_set -= to_remove

        

        for bomb in bomb_set:
            bomb.draw(gameDisplay)
            # I'm just drawing the explosion lines each
            # frame when the time is below 0.
            if bomb.timeToExplode <= 0:
                bomb.explode(gameDisplay)


        lead_y += lead_y_change
        lead_x += lead_x_change

        

        
        player = pygame.Rect(lead_x,lead_y, 15, 15)
        

        for part in Obst:
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



###                
##
##                # Game logic.
##                
##
##                # Update bombs. Pass the `dt` to the bomb instances.
##                
##
##                # Remove bombs fromt the bomb_set.
##                
##
##                # Draw everything.
##                
       
        

        
        pygame.display.update()

        

gameLoop()






pygame.quit()
quit()













                
