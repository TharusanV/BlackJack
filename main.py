import pygame, sys, os
import random
from pygame.locals import *
pygame.init()


pygame.display.set_caption('Black Jack')
WIDTH,HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


def drawWindow():
    WIN.blit(pygame.transform.scale(board, (WIDTH, HEIGHT)), (0,0))
    pygame.display.update()

class Card:
    def __init__(self, value, name, suit, image):
        self.value = value
        self.name = name
        self.suit = suit
        self.image = image



def displayCard():
    global computerInitialCard_Y
    global playerInitialCard_Y
    
    if len(playerHand) != 0:
        for i in range(len(playerHand)):
            WIN.blit(playerHand[i].image, (playerCardPos_X[i], playerInitialCard_Y))
            
    if reveal:
        if len(computerHand) != 0:
            for i in range(len(computerHand)):
                WIN.blit(computerHand[i].image, (computerCardPos_X[i], computerInitialCard_Y))
                
    else:
        if len(computerHiddenHand) != 0:
            for i in range(len(computerHiddenHand)):
                WIN.blit(computerHiddenHand[i].image, (computerHiddenCardPos_X[i], computerInitialCard_Y))

    pygame.display.update() 






def drawCard():
    global altered_deck
    draw = random.randint(0, len(altered_deck) - 1)
    return altered_deck.pop(draw)


def playerHit():
    global playerInitialCard_X
    global playerInitialCard_Y
    playerHand.append(drawCard())
    if (len(playerHand) == 1):
        playerCardPos_X.append(playerInitialCard_X)
    else:
        playerCardPos_X.append(playerInitialCard_X + (50*len(playerHand)))

def computerHit():
    global computerInitialCard_X
    global computerInitialCard_Y

    
    if getCardValue(computerHand) < 18:
        computerHand.append(drawCard())
        computerHiddenHand.append(hiddenCard)

        if(len(computerHand) == 1):
            computerCardPos_X.append(computerInitialCard_X)
            computerHiddenCardPos_X.append(computerInitialCard_X)
        else:
            computerCardPos_X.append(computerInitialCard_X + (50*len(computerHand)))
            computerHiddenCardPos_X.append(computerInitialCard_X + (50*len(computerHiddenHand)))

        return True
    else:
        return False



def getCardValue(hand) :
    if len(hand) == 0:
        return 0
    else:
        Aces = []
        cardsValue = 0

        for i in hand:
            if i.name == "ace":
                Aces.append(i)

            cardsValue += i.value

        if cardsValue > 21 and (len(Aces) != 0):
            cardsValue -= 10
        return cardsValue
        

def drawText():
    computer_hand_text = GUI_font.render("Computer hand:",True,white)
    player_hand_text = GUI_font.render("Your hand:",True,white)
    hand_value_text = GUI_font.render('Hand value: '+ str(getCardValue(playerHand)),True,white)
    winner_text = WIN_font.render(winnerText,True,white)

    WIN.blit(winner_text, (300, 10))
    WIN.blit(hand_value_text, (10,450))
    WIN.blit(computer_hand_text, (10,150))
    WIN.blit(player_hand_text, (10,350))

    esc_text = INST_font.render('Press [ESC] to restart', True, white)
    space_text = INST_font.render('Press [SPACE] to hit', True, white)
    enter_text = INST_font.render('Press [ENTER] to pass', True, white)

    WIN.blit(esc_text, (650, 400))
    WIN.blit(space_text, (650,415))
    WIN.blit(enter_text, (650,430))


def handlePlayerInput(keys_pressed):
    global inSession
    global reveal
    global computerHand
    global playerHand
    global winnerText
    
    if keys_pressed[pygame.K_ESCAPE]:
        altered_deck = list(og_deck)
        inSession = True
        reveal = False
        playerHand = []

        playerCardPos_X = []
        playerCardValue = 0

        computerHand = []
        computerHiddenHand = []
        computerCardPos_X = []
        computerHiddenCardPos_X = []
        computerCardValue = 0

        winnerText = ''
    
    if keys_pressed[pygame.K_SPACE] and inSession:
        playerHit()

        computerDraw = computerHit()

        if getCardValue(computerHand) > 21 and getCardValue(playerHand) > 21:
            inSession = False
            winnerText = 'No winner, House wins'
            reveal = True
            
        elif getCardValue(computerHand) == 21 and getCardValue(playerHand) != 21:
            inSession = False
            winnerText = 'Computer wins'
            reveal = True
        elif getCardValue(computerHand) != 21 and getCardValue(playerHand) == 21:
            inSession = False
            winnerText = 'Player wins'
            reveal = True
            
        elif getCardValue(computerHand) > 21:
            inSession = False
            winnerText = 'Player wins'
            reveal = True
        elif getCardValue(playerHand) > 21:
            inSession = False
            winnerText = 'Computer wins'
            reveal = True
            
        elif getCardValue(computerHand) == 21 and getCardValue(playerHand) == 21:
            inSession = False
            winnerText = 'Tie'
            reveal = True

    if keys_pressed[pygame.K_RETURN] and inSession:
        computerDraw = computerHit()

        if computerDraw == False:
            if getCardValue(computerHand) > getCardValue(playerHand):
                inSession = False
                winnerText = 'Computer wins'
                reveal = True
            if getCardValue(computerHand) < getCardValue(playerHand):
                inSession = False
                winnerText = 'Player wins'
                reveal = True
        else:
            if getCardValue(computerHand) > 21 and getCardValue(playerHand) > 21:
                inSession = False
                winnerText = 'No winner, House wins'
                reveal = True
            elif getCardValue(computerHand) == 21 and getCardValue(playerHand) == 21:
                inSession = False
                winnerText = 'Tie'
                reveal = True
            elif getCardValue(computerHand) > 21:
                inSession = False
                winnerText = 'Player wins'
                reveal = True
            elif getCardValue(computerHand) == 21 and getCardValue(playerHand) != 21:
                inSession = False
                winnerText = 'Computer wins'
                reveal = True
            elif getCardValue(computerHand) != 21 and getCardValue(playerHand) == 21:
                inSession = False
                winnerText = 'Player Wins'
                reveal = True

            
#Initalising game data
black = (0,0,0)
white = (255,255,255)
GUI_font = pygame.font.SysFont(None, 32)
INST_font = pygame.font.SysFont(None, 16)
WIN_font = pygame.font.SysFont(None, 42)
        
board = pygame.image.load("assets/board.png")        
hiddenCardImage = pygame.image.load("card_Images/facedown_Card.png")
hiddenCard = Card(0,0,0,hiddenCardImage)

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
            deck.append(Card(CARD_VALUES[j], CARD_NAMES[j], k, allCardImages[i]))
            i = i + 1

    return deck

og_deck = createDeck();
altered_deck = list(og_deck)
        
playerHand = []
playerInitialCard_X, playerInitialCard_Y = 200, 300
playerCardPos_X = []
playerCardValue = 0

computerHand = []
computerHiddenHand = []
computerInitialCard_X, computerInitialCard_Y = 200, 100
computerCardPos_X = []
computerHiddenCardPos_X = []
computerCardValue = 0

winnerText = ''
reveal = False
inSession = True        


    

def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        pygame.time.delay(100)
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()
        drawText()

        keys_pressed = pygame.key.get_pressed()
        handlePlayerInput(keys_pressed)        
        
        displayCard()    

    pygame.quit()

if __name__ == '__main__':
    main()




