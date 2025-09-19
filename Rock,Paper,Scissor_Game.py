print("Welcome to Rock , Paper , Scissor Game!")
print("Choices: rock,paper,scissor")

while True:
    #Player 1 input
    player1=str(input("Player 1,enter your choice: ")).lower()
    #Player 2 input
    player2=str(input("Player 2,enter your choice: ")).lower()

    #Check whether the input is valid
    if player1 not in ["rock","paper","scissor"] or player2 not in ["rock","paper","scissor"]:
        print("Invalid choice!,Please type rock,paper, or scissor.")
        continue

    #Game's Logic
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissor") or \
         (player1 == "scissor" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
            print("Player 1 wins!")
    else:
            print("Player 2 wins!")

        #Play again option

    again =str(input("Do you want to play again? (yes/no): ")).lower()
    if again != "yes":
        print("Thanks for playing!")
        break
    