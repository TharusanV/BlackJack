import pygame, sys, os
from pygame.locals import *
pygame.init()

pygame.display.set_caption('Black Jack')
WIDTH,HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60



#Images
background_resize_needed = pygame.image.load(os.path.join('assets', 'board.jpg'))
background = pygame.transform.scale(background_resize_needed, (1280,720))

listOfCards = []

class Card:
    def __init__(self, name, value, image):
        self.name = name
        self.value = value
        self.image = image

        listOfCards.append(self)


print        



def drawWindow():
    WIN.blit(background, (0,0))
    pygame.display.update();

def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()

    pygame.quit()

if __name__ == '__main__':
    main()




