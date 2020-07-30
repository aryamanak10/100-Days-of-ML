import pygame

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racing Mania')

black = (0,0,0)
white = (255,255,255)

car_width = 250

clock = pygame.time.Clock()
carImg = pygame.image.load('Week 2 - Game Development - PyGame\Car.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def game_loop():

    x = (display_width * 0.38)
    y = (display_height * 0.75)
    
    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()