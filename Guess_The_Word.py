#Word Shuffle Game
import random
#List of words
words = ["dashboard","database","programming","python","visualization","normalization","analytics","constraints"]
print("Welcome to Word Shuffle Game!")
score = 0

#Select Random words(without repetition)
selected_words =random.sample(words,5)

#Play the game in 5 rounds
for i,word in enumerate(selected_words):
    
    #Jumble the word(shuffle letters)
    jumbled = "".join(random.sample(word,len(word)))

    print(f'\nRound {1+i}:')
    print("Jumbled word:" ,jumbled)

    guess =input("Your guess: ").lower()

    if guess == word:
        print("Correct!")
        score +=1
    else:
        print(f"Wrong!,The Correct word was:{word}")

#Final Score
print("\nGame Over!")
print(f'Your Final Score is {score} is 5')