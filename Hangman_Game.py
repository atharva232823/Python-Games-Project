# Hangman Game
print("Welcome to Hangman Game!")

#Player1 enters the word (secret word)
secret_word = input("Player1,enter the secret word to guess (don't show to Player2): ").lower()

#Hide the word with underscores
guessed_word =['_']*len(secret_word)
attempts = len(secret_word)+3 #limited attempts

print("\n"*50)               #Clear the screen(stimulated,so Player 2 can't see the word)

print("Player2,start guessing letters!")
print("Word to guess:"," ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess=input("Enter a letter: ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        attempts -=1
        print(f'Wrong guess!,Attempts left:{attempts}')
    print("Word:"," ".join(guessed_word))

#Game result

if "_" not in guessed_word:
    print("Congratulations!,You guessed the word:",secret_word)
else:
    print("Out of attempts!,The word was:",secret_word)