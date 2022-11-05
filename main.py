import pygame, sys, os
import random
from pygame.locals import *
pygame.init()


pygame.display.set_caption('Black Jack')
WIDTH,HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


#Card Constructor
class Card:
    def __init__(self, value, name, suit, image):
        self.value = value
        self.name = name
        self.suit = suit
        self.image = image

#Create Deck by appending the Card objects     
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



#Drawing a window placing the board as the background 
board = pygame.image.load("assets/board.png")

def drawWindow():
    WIN.blit(pygame.transform.scale(board, (WIDTH, HEIGHT)), (0,0))
    pygame.display.update()

    

#Display cards to screen
def displayCard():
    if len(playerHand) != 0:
        for i in range(len(playerHand)):
            WIN.blit(playerHand[i].image, (playerCardPos_X[i], playerCardPos_Y[i]))
            
    if reveal:
        if len(computerHand) != 0:
            for i in range(len(computerHand)):
                WIN.blit(computerHand[i].image, (computerCardPos_X[i], computerCardPos_Y[i]))
                
    else:
        if len(computerHiddenHand) != 0:
            for i in range(len(computerHiddenHand)):
                WIN.blit(computerHiddenHand[i].image, (computerHiddenCardPos_X[i], computerCardPos_Y[i]))

    pygame.display.update() 





#Draw a card from the deck (random)
def drawCard():
    global altered_deck
    draw = random.randint(0, len(altered_deck) - 1)
    return altered_deck.pop(draw)

#Player Hit Function
def playerHit():
    global playerCardPos_X
    global playerCardPos_Y
    playerHand.append(drawCard())
    if (len(playerCardPos_X) == 0):
        playerCardPos_X.append(PLAYER_DEFAULT_X)
    else:
        playerCardPos_X.append(playerCardPos_X[-1] + DEFAULT_OFFSET)

    playerCardPos_Y.append(PLAYER_DEFAULT_Y)


#Computer Hit Function
def computerHit():
    global computerCardPos_X
    global computerCardPos_Y
    global computerHiddenCardPos_X
    global computerHiddenCardPos_Y

    
    if getCardValue(computerHand) < 18:
        computerHand.append(drawCard())
        computerHiddenHand.append(hiddenCard)

        if(len(computerCardPos_X) == 0):
            computerCardPos_X.append(COMPUTER_DEFAULT_X)
            computerHiddenCardPos_X.append(COMPUTER_DEFAULT_X)
        else:
            computerCardPos_X.append(computerCardPos_X[-1] + DEFAULT_OFFSET)
            computerHiddenCardPos_X.append(computerHiddenCardPos_X[-1] + DEFAULT_OFFSET)

        computerCardPos_Y.append(COMPUTER_DEFAULT_Y)
        computerHiddenCardPos_Y.append(COMPUTER_DEFAULT_Y)
        
        return True
    else:
        return False


#Returns the card value of both hands
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


#Initalising game data
black = (0,0,0)
white = (255,255,255)
GUI_font = pygame.font.SysFont(None, 32)
INST_font = pygame.font.SysFont(None, 16)
WIN_font = pygame.font.SysFont(None, 42)
        
playerHand = []
PLAYER_DEFAULT_X = 200
PLAYER_DEFAULT_Y = 300
playerCardPos_X = []
playerCardPos_Y = []
playerCardValue = 0

computerHand = []
computerHiddenHand = []
COMPUTER_DEFAULT_X = 200
COMPUTER_DEFAULT_Y = 100
computerCardPos_X = []
computerCardPos_Y = []
computerHiddenCardPos_X = []
computerHiddenCardPos_Y = []
computerCardValue = 0

DEFAULT_OFFSET = 50

winnerText = ''
reveal = False
inSession = True     


def handlePlayerInput(keys_pressed):
    global inSession
    global reveal
    global computerHand
    global playerHand
    global winnerText
    
    if keys_pressed[pygame.K_ESCAPE]:
        altered_deck = list(og_deck)
        reveal = False
        inSession = True

        playerHand = []
        playerCardPos_X = []
        playerCardPos_Y = []
        playerCardValue = 0

        computerHand = []
        computerCardPos_X = []
        computerCardPos_Y = []
        
        computerHiddenHand = []
        computerHiddenCardPos_X = []
        computerHiddenCardPos_Y = []
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




