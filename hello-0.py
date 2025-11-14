# single line comment

"""
multi-line comment
"""

"""
VARIABLE: 
- container that stores ref to something
- type inferencing
- Scopes (Global & Local )

==== Rules ====
- name it in accordance to what it is eg person name => name= "Jne Does, but not x = "John Doe"
- do not use inbuilt keywords/ primitives eg if, when, match, while, and, or etc
- do not start it with special characters or number eg 123... , %...
- name it either using camelcase(firstName) or snakecase(first_name)

"""

firstName = "Jane" # global vairable
lastName = "Jules" # global variable


# standard Input
# secondName = input("Kindly enter secondName: ") 

# # standard output
# print("================================================")
# print(firstName,lastName, sep=" <===> " )
# print(firstName,lastName, sep=" <****> ")
# print(firstName,lastName, secondName, sep=" <****> ")
# print("================================================")

"""
FUNCTIONS:
- a group/ block of code that does something
- parameterized and non parameterized functions
- functions can return a value

==== RULES ====
- must have the keyword def
- name of the function must be able to explain itself( name it in accordance to what it does)
- add a parenthesis () followed by a colon :
- the function precedures should be indented with 4 spaces (press tab)

"""

# defined a function 
def greetings(): 
    print("Hello World!")

# call the function
# greetings()
 
#  parameterized function
def morningGreeting(name):
    print("Good morning", name)

# call the function
# morningGreeting(name="Juliet")    

#  function definition
def updateFirstName():
    firstName = input("Enter new name: ")
    middleName = "Kong" # local variable
    print(firstName,middleName, lastName)


#  call function
# updateFirstName()
# print(firstName)



"""
ROCK PAPER SCISSORS:

- 2 players: player & computer
- player 1 is rock and computer is paper => computer wins
- player 1 is paper and computer is paper => it's a tie
- player 1 is scissors and computer is paper => player 1 wins

"""
import random

#  list of choices
playerOptions = ["rock", "scissors","paper"]

# player choices
def getPlayerChoices():
    playerChoice =  input("Enter your choice(rock, paper, scissors): ")
    computerChoice = random.choice(playerOptions)
    # getting the selections
    print("Player 1:",playerChoice, " || Computer:", computerChoice)
    return playerChoice, computerChoice
   

# deciding the winner
def selectWinner():
    if playerChoice == computerChoice:
        print("It's a tie")

    elif playerChoice == "rock":
        if computerChoice == "paper":
            print("Paper covers rock. You lose!")
        elif computerChoice == "scissors":
            print("Rock crashes scissors. You win!")

    elif playerChoice == "paper":
        if computerChoice == "rock":
            print("Paper covers rock. You win!")
        elif computerChoice == "scissors":
            print("Scissors cut paper. You lose!")

    elif playerChoice == "scissors":
        if computerChoice == "rock":
            print("Rock crashes scissors. You lose!")
        elif computerChoice == "paper":
            print("Scissors cut paper. You win!")
