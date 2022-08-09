from os import system, name
from time import sleep
import random

def clear():
	# for windows(os.name is 'nt')
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(os.name is 'posix')
	else: 
		_ = system('clear') 

#Opening Message to Users
def people1():
    clear()
    print('                  ')
    print('        O         ')
    print('       <|>        ')
    print('        |\        ')
    print('        | \       ')
    print('^^^^^^^^^^^^^^^^^^')
    print('                  ')

def people2():
    clear()
    print('                      ')
    print('           O          ')
    print('          /|\         ')
    print('           \          ')
    print('          / \         ')
    print('^^^^^^^^^^^^^^^^^^^^^^')
    print('                      ')

def people3():
    clear()
    print('                         ')
    print('               O         ')
    print('              /|\        ')
    print('               |         ')
    print('              /|         ')
    print('^^^^^^^^^^^^^^^^^^^^^^^^ ')
    print('                         ')


def people4():
    clear()
    print('                            ')
    print('                 O          ')
    print('                /|\         ')
    print('                 \          ')
    print('                / \         ')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print('                            ')


def people5():
    clear()
    print('                                ')
    print('                      O         ')
    print('                     /|\        ')
    print('                      |         ')
    print('                     /|         ')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ')
    print('                                ')

i=0
while i<1:
  people1()
  sleep(0.5)
  people2()
  sleep(0.5)
  people3()
  sleep(0.5)
  people4()
  sleep(0.5)
  people5()
  sleep(0.5)
  i+=1
clear()
sleep(1)

#Greeting for Users
def intro1():
  clear()
  print ("                        .---------------------    ")
  print ("                        | Hi Friends !        |   ")
  print ("                        | How was your day?   |   ")
  print ("                       /.---------------------    ")
  print ("                  O /                             ")
  print ("                 /|/                               ")
  print ("                  |\                              ")
  print ("                  | \                              ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                     ")
  print ("                                                   ")

def intro2():
  clear()
  print ("                        .--------------------    ")
  print ("                        | Welcome to the    |    ")
  print ("                        | game of Hangman ! |    ")
  print ("                       /.--------------------    ")
  print ("                  O                              ")
  print ("                 \|\/                            ")
  print ("                  |\                             ")
  print ("                  | |                            ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                    ")
  print ("                                                 ")

def intro3():
  clear()
  print ("                        .--------------------    ")
  print ("                        | Are you ready to   |   ")
  print ("                        |   play the game?   |   ")
  print ("                ?  ?    /.--------------------   ")
  print ("                  O                              ")
  print ("                 \|>                             ")
  print ("                  |\                             ")
  print ("                  | |                            ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                   ")
  print ("                                                 ")

def intro4():
  clear()
  print ("                        .-----------------------    ")
  print ("                        | Make sure you choose  |   ")
  print ("                        |  every word wisely !  |   ")
  print ("                !!!     /.----------------------    ")
  print ("                  O                                 ")
  print ("                 <|>                                ")
  print ("                 / \                                ")
  print ("                /   |                               ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                      ")
  print ("                                                    ")

def intro5():
  clear()
  print ("                        .------------------------------     ")
  print ("                        | You are excited, aren't you? |    ")
  print ("                        |   So, let's get started!     |    ")
  print ("                  ^^   /.------------------------------     ")
  print ("                  O__                                       ")
  print ("                 /|                                         ")
  print ("                 /\                                         ")
  print ("                /  \                                        ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                               ")
  print ("                                                             ")

i=0
while i<1:
  intro1()
  sleep(3)
  intro2()
  sleep(3)
  intro3()
  sleep(3)
  intro4()
  sleep(3)
  intro5()
  sleep(3)
  i+=1
clear()
sleep(1)

#Display of Hangman
display = [
"""
=========
  +---+
  |   |
      |
 GAME |
 OVER |
      |
=========
""",
"""
=========
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
=========
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
=========
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
=========
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
=========
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
""" 
=========
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

#Closing 
def outro_success1():
  clear()
  print ("                        .-----------------     ")
  print ("                        | Wow, you did a    |  ")
  print ("                        | great job", name_user, " |  ")
  print ("                       /.-----------------     ")
  print ("                  O                            ")
  print ("                 \|\/                          ")
  print ("                  |\                           ")
  print ("                  | |                          ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                 ")
  print ("                                               ")

def outro_success2():
  clear()
  print ("                        .-----------------------    ")
  print ("                        | Thank you for saving  |   ")
  print ("                        | me ! Have a nice day  |   ")
  print ("                       /.-----------------------    ")
  print ("                  O /                               ")
  print ("                 /|/                                ")
  print ("                  |\                                ")
  print ("                  | \                               ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                      ")
  print ("                                                    ")

def outro_failed1():
  clear()
  print ("                        .------------------------   ")
  print ("                        | It's okay,", name_user, " | ")
  print ("                        | You've done your best!  |  ")
  print ("                       /.------------------------    ")
  print ("                  O                                  ")
  print ("                 \|\/                                ")
  print ("                  |\                                ")
  print ("                  | |                                ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                       ")
  print ("                                                     ")

def outro_failed2():
  clear()
  print ("                        .--------------------------    ")
  print ("                        | See you in another game! |   ")
  print ("                        |   Have a nice day        |   ")
  print ("                       /.--------------------------    ")
  print ("                  O /                                 ")
  print ("                 /|/                                  ")
  print ("                  |\                                  ")
  print ("                  | \                                 ")
  print ("         ^^^^^^^^^^^^^^^^^^^^^                        ")
  print ("                                                      ")

#List of Words
fruits = ["APPLE", "BANANA", "WATERMELON", "ORANGE", "MANGO","PEAR", "MELON", "STRAWBERRY", "RASPBERRY", "KIWI", "PEACH","APRICOT", "GRAPE", "LIME", "BLUEBERRY", "PLUM", "AVOCADO", "CHERRY","DURIAN", "GUAVA"]

vegetables = ["LETTUCE", "SPINACH", "CABBAGE", "CAULIFLOWER", "CELERY", "ONION", "GARLIC", "SHALLOT", "BROCCOLI", "SPROUTS", "ASPARAGUS", "CARROT", "EGGPLANT", "KALE", "PUMPKIN", "ZUCCHINI", "MUSHROOMS", "LEEKS", "CUCUMBER" ] 

#Pick a random word
name_user = input("Firstly, write down your name : ")
clear()
print("""Type of Object:
1. Fruits
2. Vegetables""")
pick_list = input("Now, choose object you want to guess :")

while (pick_list != "1" and pick_list != "2"):
  print("Please choose between 1 or 2")
  pick_list = input("Now, choose object you want to guess :")

if (pick_list == "1") :
  word = random.choice(fruits)
elif (pick_list == "2"):
  word = random.choice(vegetables)

sleep(0.5)
print ("Let me think of a word....")
sleep(1)
clear()

#Make list of every alphabet in Word
letters = []
for alpha in word :
  letters.append(alpha)

#Print the characteristics of word
length = len(word)
list_underscores = []
for char in range(0,length) :
  char = "__ "
  list_underscores.append(char)
print ("This word has", length, "letter")
sleep(1)
print("It's time to guess!")
sleep(0.5)

#Print Lives
lives = 6
print ("Your lives is : ", lives)
print()

#Print Display
guessed_letters = []
print (display[lives])
print()

#Print Underscores
for char in list_underscores :
  print (char, end = " ")
print()

#Action to do when user guess
while lives > 0 and list_underscores != letters:
  print()
  guessed_letter = input("Please guess a letter: ").upper()
  if guessed_letter in letters and guessed_letter not in guessed_letters:
    clear()
    print ("This word has", length, "letter")
    print("It's time to guess!")
    print ("Your lives is : ", lives)
    print()
    print (display[lives])
    print()
    for index in range(0, length):
      if letters[index] == guessed_letter : 
        list_underscores[index] =  guessed_letter
    for char in list_underscores :
      print (char, end = " ")
    print()
    guessed_letters.append(guessed_letter)

  elif guessed_letter in guessed_letters:
    print("You have guess this letter, try guess the other word !")

  elif guessed_letter not in letters:
    clear()
    lives = lives-1
    print ("This word has", length, "letter")
    print("It's time to guess!")
    print ("Your lives is : ", lives)
    print()
    print (display[lives])
    print()
    for char in list_underscores :
      print (char, end = " ")
    print()
    print()
    print ("There is no ", guessed_letter, " in the word")
    guessed_letters.append(guessed_letter)

  else:
    print("There is not a valid letter")

#Outro
if list_underscores == letters and lives > 0:
  clear()
  i=0
  while i<1:
    outro_success1()
    sleep(2)
    outro_success2()
    sleep(2)
    i+=1
  clear()
  sleep(1)
else:
  print()
  print ("The answer is ", word)
  sleep(2)
  clear()
  i=0
  while i<1:
    outro_failed1()
    sleep(2)
    outro_failed2()
    sleep(2)
    i+=1
  clear()
  sleep(1)