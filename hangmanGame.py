import pygame
import random
pygame.init()

#the display
win = pygame.display.set_mode((800,500))
pygame.display.set_caption("Hangman")
bg = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'),pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'),pygame.image.load('hangman6.png')]


#variables list
global hangman
global checkIt
global font
global lettersGuessed
global youwin

hangman = 0
checkIt = False
font = pygame.font.SysFont("comicsans", 30)
lettersGuessed = 0
youwin = False
xIs = 400
yIs = 140



#choosing the word
chooseWord = ['BASSETHOUND', 'PIGEON', 'ROCKSTAR', 'SUPERMOON', 'pink', 'apple', 'orange', 'coding', 'python', 'huskey', 'lion', 'otter', 'alien', 'bunny', 'easter', 'chicken', 'giraffe', 'strawberry']
word = random.choice(chooseWord).upper()



#to print the right amount of _ for python
wordLength = len(word)
counter = wordLength
spacesList = []

while counter > 0:
    spacesList.append('_')
    counter -= 1

spacesDisplay = len(spacesList)


#splits the word into individual letters
wordList = list(word)

    
class letter(object):
    #will make a letter object for every letter of the alphabet
    def __init__(self, letterIs, x, y):
        self.used = False
        self.letterIs = letterIs
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("comicsans", 30)
        self.text = self.font.render(self.letterIs, 1, (0,0,0))
        self.drawLine = False


    def drawSelf(self):
        global checkIt
        global mousex
        global mousey
        global word
        global hangman
        global hangmanAdd
        global lettersGuessed
        hangmanAdd = 0
        
        win.blit(self.text, (self.x, self.y))

        if self.drawLine == True:
            pygame.draw.line(win, (0,0,0), (self.x - 4 ,self.y + 15), (self.x + 14, self.y + 2),4)

        if checkIt == True and mousex >= self.x and mousex <= self.x + 20 and mousey >= self.y and mousey <= self.y + 20 and self.used == False:
            
            self.used = True
            self.drawLine = True
            lettersRight = []
            i = 0
            pos = 0

            for a in range(len(wordList)):
                
                if self.letterIs == wordList[pos]:
                    spacesList[pos] = self.letterIs
                    lettersGuessed += 1

                else:
                    hangmanAdd += 1

                pos += 1

            if hangmanAdd == len(word):
                hangman += 1
                checkIt == False

            checkIt = False


def youLose():
    run = False
    global font
    global word
    global lettersGuessed
    fontBig = pygame.font.SysFont("comicsans", 100)
    text = fontBig.render("YOU LOSE!", 1, (0,0,0))
    textA = font.render("Letters guessed: " + str(lettersGuessed), 1,(0,0,0))
    pygame.draw.rect(win, (245,222,179), (200, 185, 400, 150))
    pygame.draw.rect(win, (128,0,0), (200, 185, 400, 150), 4)
    wordSize = text.get_size()
    wordWidth = wordSize[0]
    wordWidth /= 2
    wordWidth2 = int(400 - wordWidth)
    win.blit(text, (wordWidth2, 220))
    wordSize = textA.get_size()
    wordWidth = wordSize[0]
    wordWidth /= 2
    wordWidth2 = int(400 - wordWidth)
    win.blit(textA, (wordWidth2, 290))
    textB = font.render("Word: " + word, 1, (0,0,0))
    wordSize = textB.get_size()
    wordWidth = wordSize[0]
    wordWidth /= 2
    wordWidth2 = int(400 - wordWidth)
    win.blit(textB, (wordWidth2, 310))
    pygame.display.update()

def drawSpaces():
    global font
    xpos = 400
    a = 0
    for i in range(spacesDisplay):
        text = font.render(spacesList[a], 1, (0,0,0))
        win.blit(text, (xpos, 300))
        xpos += 30
        a += 1

def checkWinner():
    global youwin
    b = 0
    notWonLetters = 0

    if hangman == 6:
        youLose()

    if hangman < 6:
        for i in range(len(word)):
            if spacesList[b] == '_':
                notWonLetters += 1

            b += 1
    
    if notWonLetters == 0 and hangman < 6:
        youwin = True
        

#creates every letter
a = letter('A', xIs, yIs)
b = letter('B', xIs + 30, yIs)
c = letter('C', xIs + 60, yIs)
d = letter('D', xIs + 90, yIs)
e = letter('E', xIs + 120, yIs)
f = letter('F', xIs + 150, yIs)
g = letter('G', xIs + 180, yIs)
h = letter('H', xIs + 210, yIs)
i = letter('I', xIs + 240, yIs)
j = letter('J', xIs + 260, yIs)
yIs += 30
k = letter('K', xIs, yIs)
l = letter('L', xIs + 30, yIs)
m = letter('M', xIs + 60, yIs)
n = letter('N', xIs + 90, yIs)
o = letter('O', xIs + 120, yIs)
p = letter('P', xIs + 150, yIs)
q = letter('Q', xIs + 175, yIs)
r = letter('R', xIs + 205, yIs)
s = letter('S', xIs + 235, yIs)
t = letter('T', xIs + 260, yIs)
yIs += 30
u = letter('U', xIs, yIs)
v = letter('V', xIs + 30, yIs)
w = letter('W', xIs + 60, yIs)
x = letter('X', xIs + 90, yIs)
y = letter('Y', xIs + 120, yIs)
z = letter('Z', xIs + 150, yIs)

#drawing the game window
def redrawGameWindow():
    win.blit(bg[hangman], (0,0))
    a.drawSelf()
    b.drawSelf()
    c.drawSelf()
    d.drawSelf()
    e.drawSelf()
    f.drawSelf()
    g.drawSelf()
    h.drawSelf()
    i.drawSelf()
    j.drawSelf()
    k.drawSelf()
    l.drawSelf()
    m.drawSelf()
    n.drawSelf()
    o.drawSelf()
    p.drawSelf()
    q.drawSelf()
    r.drawSelf()
    s.drawSelf()
    t.drawSelf()
    u.drawSelf()
    v.drawSelf()
    w.drawSelf()
    x.drawSelf()
    y.drawSelf()
    z.drawSelf()

    drawSpaces()
    checkWinner()

    if youwin == True:
        
        fontBig = pygame.font.SysFont("comicsans", 100)
        text = fontBig.render("YOU WIN!", 1, (0,0,0))
        pygame.draw.rect(win, (245,222,179), (200, 185, 400, 150))
        pygame.draw.rect(win, (128,0,0), (200, 185, 400, 150), 4)
        wordSize = text.get_size()
        wordWidth = wordSize[0]
        wordWidth /= 2
        wordWidth2 = int(400 - wordWidth)
        win.blit(text, (wordWidth2, 230))
        pygame.display.update()
    
    pygame.display.update()
    

    
#main loop 
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            mousex = position[0]
            mousey = position[1]
            checkIt = True

    checkWinner()

    if hangman >= 6:
        youLose()
        run = False

    if youwin == True:
        run = False

    redrawGameWindow()
    pygame.display.update()


while run == False:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    checkIt = False


    redrawGameWindow()
    pygame.display.update()



    
    
        
