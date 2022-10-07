import pygame, sys, os
import random
from pygame.locals import *
pygame.init()


pygame.display.set_caption('Black Jack')
WIDTH,HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

playerCardValue = 0
computerCardValue = 0

playerCardInitialPos_X, playerCardInitialPos_Y = 100, 500
computerCardInitialPos_X, computerCardInitialPos_Y = 100, 200

playerCardPosMultiplier_X = 5;
computerCardPosMultiplier_X = 5;

playerNumberOfCards = 0
computerNumberOfCards = 0

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

twoH = Card('2_hearts', 2, two_hearts)
twoD = Card('2_diamonds', 2, two_diamonds)
twoS = Card('2_spades', 2, two_spades)
twoC = Card('2_clubs', 2, two_clubs)

threeH = Card('3_hearts', 3, three_hearts)
threeD = Card('3_diamonds', 3, three_diamonds)
threeS = Card('3_spades', 3, three_spades)
threeC = Card('3_clubs', 3, three_clubs)

fourH = Card('4_hearts', 4, four_hearts)
fourD = Card('4_diamonds', 4, four_diamonds)
fourS = Card('4_spades', 4, four_spades)
fourC = Card('4_clubs', 4, four_clubs)

fiveH = Card('5_hearts', 5, five_hearts)
fiveD = Card('5_diamonds', 5, five_diamonds)
fiveS = Card('5_spades', 5, five_spades)
fiveC = Card('5_clubs', 5, five_clubs)

sixH = Card('6_hearts', 6, six_hearts)
sixD = Card('6_diamonds', 6, six_diamonds)
sixS = Card('6_spades', 6, six_spades)
sixC = Card('6_clubs', 6, six_clubs)

sevenH = Card('7_hearts', 7, seven_hearts)
sevenD = Card('7_diamonds', 7, seven_diamonds)
sevenS = Card('7_spades', 7, seven_spades)
sevenC = Card('7_clubs', 7, seven_clubs)

eightH = Card('8_hearts', 8, eight_hearts)
eightD = Card('8_diamonds', 8, eight_diamonds)
eightS = Card('8_spades', 8, eight_spades)
eightC = Card('8_clubs', 8, eight_clubs)

nineH = Card('9_hearts', 9, nine_hearts)
nineD = Card('9_diamonds', 9, nine_diamonds)
nineS = Card('9_spades', 9, nine_spades)
nineC = Card('9_clubs', 9, nine_clubs)

tenH = Card('10_hearts', 10, ten_hearts)
tenD = Card('10_diamonds', 10, ten_diamonds)
tenS = Card('10_spades', 10, ten_spades)
tenC = Card('10_clubs', 10, ten_clubs)

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
    #WIN.blit(board, (0,0))
    pygame.display.update()
    

def playerHit():
    playerCard = random.choice(listOfCards)
    if playerNumberOfCards == 0:
        WIN.blit(playerCard.image, (playerCardInitialPos_X, playerCardInitialPos_Y))
        playerNumberOfCards = playerNumberOfCards + 1
    else:
        WIN.blit(playerCard.image, (playerCardInitialPos_X + (), playerCardInitialPos_Y))
    

def computerHit():
    computerCard = random.choice(listOfCards)

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




