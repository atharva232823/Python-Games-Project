# Quiz Game
print("Welcome to the Quiz Game!")

#List of questions,options and correct answers

questions=[
    {"question":"When was Chandrayaan-3 successfully launced by ISRO?",
     "options":["A:22 July 2023","B:14 July 2023","C:15 August 2023","D:23 July 2023"],
    "answer":"B"
    },
    {"question":"Chandrayaan-3 made India the ___ country to successfully soft-land on the Moon.",
    "options":["A:2nd","B:3rd","C:4th","D:5th"],
    "answer":"A" 
    },
    {"question":"Where did Chandrayaan-3 land on the Moon?",
     "options":["A:Near the South Pole","B:Near the North Pole","C:Near the Equator","D:More Tranquilliatis"],
    "answer":"A"
    },
    {"question":"What is the name of the rover carried by Chandrayaan-3",
     "options":["A:Vikram","B:Pragyan","C:Chandrayaan","D:Ganganyaan"],
    "answer":"B"
    },
    {"question":"What was the main objective of Chandrayaan-3?",
     "options":["A:Study Mars atmosphere",
                "B:Demonstrate safe and soft landing on Moon",
                "C:Send humans to the Moon",
                "D:Test nuclear propulsion"],
    "answer":"B"
    }]
score = 0 #Keep track of score

#Ask each questions
for q in questions:
    print("\n"+q["question"])
    for option in q ["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
         print("Correct!")
         score+=1
    else:
         print("Wrong!,The correct answer was:",q["answer"].upper())
    
#Final result
print("\n Quiz Over!")
print("Your final score is: ",score,"out of",len(questions))