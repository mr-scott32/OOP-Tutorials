import pygame
import random
import time

# Initialize the game
pygame.init()

#set fps
fps = 60
clock = pygame.time.Clock()

# Set the screen size
screen = pygame.display.set_mode((600, 200))

# Set the title of the game
pygame.display.set_caption("Breakout")

# create a class for a brick
class Brick:
    def __init__(self, x, y, color, state):
        self.x = x # x position
        self.y = y # y position
        self.color = color # color of the brick
        self.width = 100 # width of the brick
        self.height = 20 # height of the brick
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) # create a rectangle for the brick
        self.state = state # state of the brick

    # if the brick is active, draw it
    def draw(self):
        if self.state == 1:
            pygame.draw.rect(screen, self.color, self.rect) # draw the brick
        else:
            pygame.draw.rect(screen, (0, 0, 0), self.rect)

#place a brick in the middle of the screen
brick = Brick(300, 100, (255, 0, 0), 1)
brick.draw()

# if i press the space bard the brick will change state
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if brick.state == 1:
                    brick.state = 0
                else:
                    brick.state = 1
                brick.draw()
                pygame.display.update()

    clock.tick(fps)



