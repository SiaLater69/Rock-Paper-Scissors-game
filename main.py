import random

player1 = input("Select Rock, Paper, Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()

if player1 == "rock" and player2 == "paper":
    print("PLAYER 2 WINS")
elif player1 == "paper" and player2 == "scissor":
    print("PLAYER 2 WINS")
elif player1 == "scissor" and player2 == "rock":
    print("PLAYER 2 WINS")
elif player1 == player2:
    print("TIE")
else:
    print("PLAYER 1 WINS")
