import pygame
import random

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((600, 200))

# Set the title of the game
pygame.display.set_caption("Breakout")

#create the sprite using sprite.png
sprite = pygame.image.load("pygame_class_example/sprite.png")

# create a class for a sprite
class Sprite:
    def __init__(self, x, y):
        self.x = x # x position
        self.y = y # y position
        self.width = 20 # width of the sprite
        self.height = 20 # height of the sprite
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) # create a rectangle for the sprite
        self.image = sprite # image of the sprite

    def draw(self):
        screen.blit(self.image, (self.x, self.y)) # draw the sprite

    
#place a sprite in the middle of the screen
sprite = Sprite(300, 100)
sprite.draw()

# Update the screen
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
