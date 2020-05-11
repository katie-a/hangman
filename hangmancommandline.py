
hangman6 = '''
   _________
  |        |
  |       _|_               _____                      _____   ____  _____
  |      /   \      |   |  |     |  |    |     |      |     | |     |
  |      \___/       | |   |     |  |    |     |      |     | |___  |
  |        |          |    |     |  |    |     |      |     |     | |----
  |       /|\        |     |     |  |    |     |      |     |     | |
  |        |        |      |_____|  |____|     |_____ |_____| ____| |_____
__|__     / \             

'''

hangmanLooks = ['''
   _________
  |        |
  |       
  |
  |
  |
  |
  |
__|__

''', '''

   _________
  |        |
  | 	  _|_
  |      |   |
  |      |___|     
  |
  |
  |
__|__

''', '''

   _________
  |        |
  | 	  _|_
  |      |   |
  |      |___|     
  |        |
  |        |
  |        |
__|__

''','''

   _________
  |        |
  | 	  _|_
  |      |   |
  |      |___|     
  |       _|
  |      | |
  |        |
__|__

''','''
   _________
  |        |
  | 	  _|_
  |      |   |
  |      |___|     
  |       _|_
  |      | | |
  |        |
__|__

''','''
   _________
  |        |
  | 	  _|_
  |      |   |
  |      |___|     
  |       _|_
  |      | | |
  |        |
__|__     |

''']



import random


#list of word categories and possibilities
pets = ['cat', 'dog', 'hamster', 'goldfish', 'horse']
fruit = ['papaya', 'watermelon', 'orange', 'banana', 'grapes']
drinks = ['champagne', 'coffee', 'tea', 'water', 'juice']







#picks a word based on what category the user picks
type = input("Pick a category of words (pets, fruit, drinks):").lower().strip()

if type == 'pets':
    word = random.choice(pets)
elif type == 'fruit':
    word = random.choice(fruit)
elif type == 'drinks':
    word = random.choice(drinks)

#to print the right amount of _ for python
wordLength = len(word)
counter = wordLength
spacesList = []
wordLengthM1 = wordLength - 1

while counter > 0:
    spacesList.append('_')
    counter -= 1


#splits the word into individual letters
wordList = list(word)
#letterTrue = False

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

hangman = 0
amountGuessed = 0
play = True
hangmanAdd = 0


while play:
    
    print(hangmanLooks[hangman])
    print(' '.join(spacesList))
    print(' '.join(letterList))
    willYouAdd = 0
    hangmanAdd = 0
    inputLetter = input('Type a letter: ').lower()
    place = 0
    used = False
    letterPosition = 0


    for i in letterList:
        if letterList[letterPosition] == inputLetter:
            used = False
            del(letterList[letterPosition])
            break
        else:
            used = True
        letterPosition += 1



    for x in wordList:
        if wordList[place] == inputLetter and used == False:
            spacesList[place] = inputLetter
            print('letters left: ' + str(' '.join(letterList)))
            amountGuessed += 1
        else:
            hangmanAdd += 1


        place += 1

    if hangmanAdd == wordLength and hangman < 5:
        hangman += 1
    elif hangmanAdd == wordLength and hangman == 5:
        print(hangman6)
        break

    
    


    
        

    
    
    if amountGuessed == wordLength:
        print('''
        _____                       _______
|   |  |     |  |    |   |       |     |     ||   |
 | |   |     |  |    |   |       |     |     | |  |
  |    |     |  |    |   |   |   |     |     |  | |
 |     |     |  |    |    | | | |      |     |   ||
|      |_____|  |____|     |   |    ___|___  |    |
  



''')
        break



    
            

    

    

    
        
    
        




    
    



    
    


