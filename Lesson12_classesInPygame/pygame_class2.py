import pygame
import random

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((600, 200))

# Set the title of the game
pygame.display.set_caption("Breakout")

# create a class for a brick
class Brick:
    def __init__(self, x, y, color):
        self.x = x # x position
        self.y = y # y position
        self.color = color # color of the brick
        self.width = 100 # width of the brick
        self.height = 20 # height of the brick
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) # create a rectangle for the brick

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect) # draw the brick

for i in range(6):
    brick = Brick(100 * i, 100, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    brick.draw()

# Update the screen
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the game
pygame.quit()

