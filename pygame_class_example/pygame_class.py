def click_brick(bricks, x, y):
    for brick in bricks:
        if brick.rect.collidepoint(x, y):
            brick.state = 0
            brick.draw()
            pygame.display.update()
