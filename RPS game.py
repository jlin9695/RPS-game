import random

#def RPScheck(y):
#    if y.lower() != "rock" and y.lower() != "paper" and y.lower() != "scissors":
#        print("Whoops! That doesn't seem like you put in a proper hand. Try again!")
#        return input("Throw your hand: ")
#    else:
#        return y.lower()
def RPS(y,c):
    listing = ["rock","paper","scissors"]
    if y.lower() != "rock" and y.lower() != "paper" and y.lower() != "scissors":
        print("Whoops! That doesn't seem like you put in a proper hand. Try again!")
        y = input("Throw your hand: ")
        y = RPS(y,c)
    print("The computer has thrown their hand! They threw: " + c)
    if y == "rock" and c == "paper":
        print("You lose! Paper beats rock. Good luck next time!")
        y = input("Would you like to try again? Y or N : ")
        if y.lower() == "y":
            y = input("Throw your hand!")
            c = random.choice(listing)
            y = RPS(y,c)
        else:
            return "Thank you for playing, hope to see you soon!"
    elif y == "paper" and c == "scissors":
        print("You lose! Scissors beats paper. Good luck next time!")
        y = input("Would you like to try again? Y or N : ")
        if y.lower() == "y":
            y = input("Throw your hand!")
            c = random.choice(listing)
            y = RPS(y, c)
        else:
            return "Thank you for playing, hope to see you soon!"
    elif y == "scissors" and c == "rock":
        print("You lose! Rock beats scissors. Good luck next time!")
        y = input("Would you like to try again? Y or N : ")
        if y.lower() == "y":
            y = input("Throw your hand!")
            c = random.choice(listing)
            y = RPS(y, c)
        else:
            return "Thank you for playing, hope to see you soon!"
    elif y == c:
        print("You tied. Let's try this again.")
        y = input("Would you like to try again? Y or N : ")
        if y.lower() == "y":
            y = input("Throw your hand!")
            c = random.choice(listing)
            y = RPS(y, c)
        else:
            return "Thank you for playing, hope to see you soon!"
    else:
        print("Congratulations! You've won!")
        y = input("Would you like to try again? Y or N : ")
        if y.lower() == "y":
            y = input("Throw your hand!")
            c = random.choice(listing)
            y = RPS(y, c)
        else:
            return "Thank you for playing, hope to see you soon!"
play = "y"
game = ["rock", "paper", "scissors"]
you = input("Let's play rock, paper, scissors! Go ahead and throw your hand: ")
x = random.choice(game)
you = RPS(you,x)
#print(x)
#print(type(x))

#while play.lower() == "y":
#you = RPScheck(you)
#play = RPS(you,x)
#print(you)