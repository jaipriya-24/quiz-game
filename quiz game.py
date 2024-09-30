print("---------------------------------")
print("Welcome to my Quiz :)")
print("---------------------------------")

question_bank=[{"que":"Which of these is the most visited attraction in the world?" ,"ans":"c"},
               {"que":"What’s the heaviest organ in the human body?", "ans":"c"},
               {"que":"Where is recognized as the location of the hottest temperature ever recorded on Earth?","ans":"b"},
               {"que":"Which country’s national animal is a unicorn?","ans":"a"},
               {"que":"Mycology is the scientific study of what?","ans":"c"},
               {"que":"Which sea creature has three hearts?","ans":"d"},
               {"que":"From which country do French fries originate?","ans":"a"}]

answers=[["a)Eiffel Tower","b)Statue of Liberty","c)Forbidden City","d)Colosseum"],
         ["a)Brain","b)Liver","c)Skin","d)Heart"],
         ["a)Mitribah, Kuwait","b)Death Valley, California","c)Yuma, Arizona","d)Key West, Florida"],
         ["a)Scotland","b)Denmark","c)New Zealand","d)France"],
         ["a)Cancer cells","b)Flowers","c)Fungi","d)Blood"],
         ["a)Shark","b)Jellyfish","c)Stingray","d)Octopus"],
         ["a)Belgium","b)France","c)USA","d)England"],
]

score = 0

def check_answer(user_guess, correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
    
def next_question():
    go_to_next=input("Do you want to go to the next question?(yes/no)")
    if (go_to_next == "yes"):
          check_answer(guess, question_bank[ques_no]["ans"])
    else:
          return "You quit the game!!"
    

for ques_no in range(len(question_bank)):
    print("--------------------------------------")
    print(question_bank[ques_no]["que"])
    for i in answers[ques_no]:
        print(i)

    guess =input("Enter your answer(a/b/c/d): ")
    is_correct=check_answer(guess, question_bank[ques_no]["ans"])
    
    if is_correct is True:
        print("Correct answer")
        score += 1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {question_bank[ques_no]["ans"]} ")

    status = next_question()
    if status == "You quit the game!!":
        print(status)
        exit()

    
        

print(f"Your have given {score} correct answers out of 7 questions.")
print(f"Your score is {format((score/len(question_bank))*100, ".2f")}%")
