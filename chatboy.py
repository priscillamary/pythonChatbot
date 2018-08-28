import random
import time
#okay to use these globals
listNo = ["No","Nah","nah","no"]
listYes = ["yes", "Yeah", "yeah", "Yes", "Sure","sure", "Maybe"]
# --- Define your functions below! ---
#defines intro function to start game
def intro():
    print("Hello! I'm THE GENIE...Let's talk!!")
    print("I'm Nicholas, THE BEST GENIE OF ALL TIME!!!!")
tellFuture= ["you will win a million dollars", "you will eat an apple tomorrow", "you will get arrested soon.",
 "you will get a mansion.", "you will meet me in person(rub your nearest lamp;)"]

# --- Put your main program below! ---
#defines sayHi function to display player name
def sayHi(userName):
    print("Hi, "+ userName)
    print("That's a nice name:)")
#this function activates game (gives choice of two games)
def processInput(userAnswer):
    while (userAnswer not in listYes and userAnswer not in listNo):
        print("Sorry, please type 'yes/Yes' or 'no/No'")
        userAnswer = input()

    if (isValidInput(userAnswer,listNo)):
        playLuckyNumber()
    elif (isValidInput(userAnswer,listYes)):
        guessFuture()
#begins guessFuture game (game randomizes from tellFuture)
def guessFuture ():
        print("Ok, let's play!")
        print("I'm going to predict your future.")
        time.sleep(1)
        print(random.choice(tellFuture))
# begins playLuckyNumber game (game randomizes from 1 to 99)
def playLuckyNumber():
    print("Ok, instead, you will have to guess your lucky number!")
    start = '''
    It's up to you to guess your lucky number from 1 to 99. You have to keep
    going until you get your lucky number or you will be cursed with bad luck!
    '''
    computerChoice = random.randint(1,99)
    userGuess = int(input("Type a number anywhere from 1 to 99. Good luck!"))
    while computerChoice != userGuess:
        if userGuess < computerChoice:
            print("The lucky number is larger than that... try again!")
        else:
            print("The lucky number is smaller than that... try again!")
        userGuess = int(input("Type a number anywhere from 1 to 99. Good luck!"))

#compares userInput to validResponses
#@param: userInput string matches list in validResponses
#@return:function returns Boolean depending on elements list (based on yes/no responses)
def isValidInput(userInput,validResponses):
    if userInput in validResponses:
        return True
    else:
        return False

def genieEscape():
    start = '''
    OK! Let me tell you a little about me: I've been stuck in this lamp for
    CENTURIES. All I've wanted to do is see the world through my own eyes
    rather than through the holes in a lamp, BUT NOW YOU'RE HERE. You can
    help me finally see the world. YOU CAN SHOW ME THE WORLD like Aladdin
    showed Jasmine.
    '''
    print (start)
    riddle = '''
    I have been cursed and you can break my curse as long as you can solve
    this riddle...
    There's a one-story house where everything inside is pink and white: pink walls,
    white doors, pink floors, white ceilings, pink windows, white curtains,
    pink chairs, and white tables.
    '''
    print (riddle)
    print ("remember.. if you want to save me, your answer must be one of my options word-for-word...")
    trickQuestion=input(" What 'color' would the 'stairs' be: 'pink stairs', 'pink stairs that do not exist','white stairs','white stairs that exist'?")
    if (trickQuestion!= "pink stairs that do not exist"):
        print("I guess I will be in this lamp for the rest of my life.. you are wrong")
        print("THE STAIRS DON'T EXIST... ITS A ONE STORY HOUSE... I guess this is goodbye")
    else:
        print("I HAVE ESCAPED... THANK YOU FOR PLAYING AND SAVING ME... you are a GENIE-us")

def loveMe(genieAnswer):
    if isValidInput(genieAnswer,listNo):
        print("IDC...")
    elif isValidInput(genieAnswer,listYes):
        print("i love you 2!")
    genieEscape()

def main():
    intro()
    answer = input("What is your name?")
    sayHi(answer)
    question= input("Do you want me to tell you your future?")
    processInput(question)
    print("Thanks for playing")
    exitCondition= input("Do you want to play again?")

    if(isValidInput(exitCondition,listNo)):
    #if (exitCondition== "no" or exitCondition== "No"):
        print("OK byeee...jk")
    elif (isValidInput(exitCondition,listYes)):
        question= input("Do you want me to tell you your future?")
        processInput(question)
        print("You are right!!! Thanks for playing!")
    genieAnswer= input("Do you love me?")
    loveMe(genieAnswer)



#DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
