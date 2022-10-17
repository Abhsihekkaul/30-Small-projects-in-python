import random as rd
Choices = ['ROCK','PAPER','SCISSOR']
ComputerChoice = rd.choice(Choices)
print(ComputerChoice)
print("Hello My Name is Alex! Let's Play Rock, Paper and Scissor")
SuccessText = "Congratulation you've won the Match"
LossText = "Unfortunately you've Loss the Match"

UserChoice = input("Enter your Choice : ROCK, PAPER OR SCISSOR :- " ).upper()
if UserChoice not in Choices:
    raise ValueError("Please Enter a Valid Choice")

while True:
    def game():
        if ComputerChoice == 'ROCK' and UserChoice == 'PAPER':
            print(SuccessText)
        elif ComputerChoice == 'ROCK' and UserChoice == 'SCISSOR':
            print(LossText)

        elif ComputerChoice == 'PAPER' and UserChoice == 'ROCK':
            print(LossText)
        elif ComputerChoice == 'PAPER' and UserChoice == 'SCISSOR':
            print(SuccessText)

        elif ComputerChoice == 'SCISSOR' and UserChoice == 'ROCK':
            print(SuccessText)
        elif ComputerChoice == 'SCISSOR' and UserChoice == 'PAPER':
            print(LossText)
    game()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
else:
    print("Alex and you chose the same Choice therefore it's a tie game ")


#there are still some bugs but i will definately repair in the future
