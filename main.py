import pygame, sys, os
from pygame.locals import *
pygame.init()

pygame.display.set_caption('Black Jack')
WIDTH,HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


#Load Images (Global)
path = 'assets'
filenames = [f for f in os.listdir(path) if f.endswith('.png')]
for name in filenames:
    imagename = os.path.splitext(name)[0] 
    globals()[imagename] =  pygame.image.load(os.path.join(path, name)).convert_alpha()

listOfCards = []

class Card:
    def __init__(self, name, value, image):
        self.name = name
        self.value = value
        self.image = image

        listOfCards.append(self)


aceH = Card('ace_hearts', 1, ace_hearts)
aceD = Card('ace_diamonds', 1, ace_diamonds)
aceS = Card('ace_spades', 1, ace_spades)
aceC = Card('ace_clubs', 1, ace_clubs)

2H = Card('2_hearts', 2, 2_hearts)
2D = Card('2_diamonds', 2, 2_diamonds)
2S = Card('2_spades', 2, 2_spades)
2C = Card('2_clubs', 2, 2_clubs)

3H = Card('3_hearts', 3, 3_hearts)
3D = Card('3_diamonds', 3, 3_diamonds)
3S = Card('3_spades', 3, 3_spades)
3C = Card('3_clubs', 3, 3_clubs)

4H = Card('4_hearts', 4, 4_hearts)
4D = Card('4_diamonds', 4, 4_diamonds)
4S = Card('4_spades', 4, 4_spades)
4C = Card('4_clubs', 4, 4_clubs)

5H = Card('5_hearts', 5, 5_hearts)
5D = Card('5_diamonds', 5, 5_diamonds)
5S = Card('5_spades', 5, 5_spades)
5C = Card('5_clubs', 5, 5_clubs)

6H = Card('6_hearts', 6, 6_hearts)
6D = Card('6_diamonds', 6, 6_diamonds)
6S = Card('6_spades', 6, 6_spades)
6C = Card('6_clubs', 6, 6_clubs)

7H = Card('7_hearts', 7, 7_hearts)
7D = Card('7_diamonds', 7, 7_diamonds)
7S = Card('7_spades', 7, 7_spades)
7C = Card('7_clubs', 7, 7_clubs)

8H = Card('8_hearts', 8, 8_hearts)
8D = Card('8_diamonds', 8, 8_diamonds)
8S = Card('8_spades', 8, 8_spades)
8C = Card('8_clubs', 8, 8_clubs)

9H = Card('9_hearts', 9, 9_hearts)
9D = Card('9_diamonds', 9, 9_diamonds)
9S = Card('9_spades', 9, 9_spades)
9C = Card('9_clubs', 9, 9_clubs)

10H = Card('10_hearts', 10, 10_hearts)
10D = Card('10_diamonds', 10, 10_diamonds)
10S = Card('10_spades', 10, 10_spades)
10C = Card('10_clubs', 10, 10_clubs)

JH = Card('J_hearts', 11, jack_hearts)
JD = Card('J_diamonds', 11, jack_diamonds)
JS = Card('J_spades', 11, jack_spades)
JC = Card('J_clubs', 11, jack_clubs)

QH = Card('Q_hearts', 12, queen_hearts)
QD = Card('Q_diamonds', 12, queen_diamonds)
QS = Card('Q_spades', 12, queen_spades)
QC = Card('Q_clubs', 12, queen_clubs)

KH = Card('K_hearts', 13, king_hearts)
KD = Card('K_diamonds', 13, king_diamonds)
KS = Card('K_spades', 13, king_spades)
KC = Card('K_clubs', 13, king_clubs)




def drawWindow():
    WIN.blit(board, (0,0))
    pygame.display.update()

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




