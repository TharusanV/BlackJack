import pygame, sys, os
import random
from pygame.locals import *
pygame.init()


pygame.display.set_caption('Black Jack')
WIDTH,HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

board = pygame.image.load("assets/board.png")

class Card:
    def __init__(self, value, name, suit, image):
        self.value = value
        self.name = name
        self.suit = suit
        self.image = image

CARD_VALUES = [11,2,3,4,5,6,7,8,9,10,10,10,10]
CARD_NAMES = ["ace","two","three","four","five","six","seven","eight","nine","ten","jack","king","queen"]
CARD_SUITS = ["clubs", "diamonds", "hearts", "spades"]
allCardImages_directory = []
allCardImages = []

for i in CARD_NAMES:
    for j in CARD_SUITS:
        allCardImages_directory.append("card_Images/"+str(i)+"_"+str(j)+".png")

for i in allCardImages_directory:
    allCardImages.append(pygame.image.load(i))
        


def createDeck():
    deck = []
    i = 0
    for j in range(len(CARD_VALUES)):
        for k in CARD_SUITS:
            deck.append(Card(CARD_VALUES[j], CARD_NAMES[j], k, allCardImages[i]
            i = i + 1

    return deck

og_deck = createDeck();
altered_deck = list(og_deck)

playerHand = []
playerInitialCard_X, playerInitialCard_Y = 100, 300
playerCardPos_X = []


computerHand = []
computerInitialCard_X, computerInitialCard_Y = 100, 100
computerCardPos_X = []


def drawCard():
    global altered_deck
    draw = random.randint(0, len(altered_deck) - 1)
    return altered_deck.pop(draw)

def playerHit():
    playerHand.append(drawCard())
    if (len(playerHand) == 0):
        playerCardPos_X.append(playerInitialCard_X)
    else:
        playerCardPos_X.append(playerInitialCard_X + (10*len(playerHand)))
        

def drawWindow():
    WIN.blit(pygame.transform.scale(board, (WIDTH, HEIGHT)), (0,0))
    pygame.display.update()
    


def computerHit():
    computerCard = random.choice(listOfCards)


def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()
        keys_pressed = pygame.key.get_pressed()
        
        click = False    

    pygame.quit()

if __name__ == '__main__':
    main()




