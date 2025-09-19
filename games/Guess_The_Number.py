## guess the number game
import random
import datetime
num = random.randint(1,100)
attempts = 0
start =datetime.datetime.now()
while True:
    guess =int(input("Enter a number between [1-100]: "))
    attempts += 1
    end =datetime.datetime.now()
    time_taken =(end - start).total_seconds()
    minutes = time_taken // 60
    seconds = time_taken % 60
    if guess >100 or guess <0:
               print("Invalid guess,please enter a valid number [1-100]")
    if guess == num:
               print(f'You guessed it right! in {attempts} attempts')
               print(f'Time Taken:{minutes} minutes {seconds} seconds')
               break
    elif guess> num:
        if guess - num >=10:
            print("You are far away!,guess lower")
        else:
            print("You are far close!,guess a bit lower")
    elif guess < num:
        if guess -num >=10:
            print("You are far away!,guess higher")
        else:
            print("You are far close!,guess a bit higher")
