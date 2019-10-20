#Gabe Dials
#NarutoTriviaGame

import Question
def doTest(questions):
    score = 0
    for ques in questions:
        answer = input(ques.prompt)
        if answer == ques.answer:
            score += 1
    print("Ninja Knowledge: " + str(score) + "/" + str(len(questions)) + "Correct" )
    doTest(questions)


def intro():
    print("hello!")
    print("Welcome to A Naruto Adventure")
    name =input("What is your name?")
    #add kun to end of name
    print("Cool! Your Ninja Name is", name + "-kun")
    enteredNum=int(input("type 1 if you are ready to start: "))
    if enteredNum == 1:
        print("Lets Begin! **SPOILERS AHEAD**")
    else:
        print("You must enter 1 to start")
        enteredNum = int(input("type 1 if you are ready to start: "))
    quesListLevel1 = [
            "What clan is Naruto in?\n(a) Sarutobi\n(b) Uzumaki\n(c) Uchiha\n\n",
            "What clan is Sasuke in?\n(a) Sarutobi\n(b) Uzumaki\n(c) Uchiha\n\n",
            "What clan is Itachi in?\n(a) Sarutobi\n(b) Uzumaki\n(c) Uchiha\n\n",
            "What village does Naruto live in?\n(a) Hidden Leaf\n(b) Hidden Sand\n(c) Hidden Sound\n\n"
    ]

    q1 = Question.Question(quesListLevel1[0], "b")
    q2 = Question.Question(quesListLevel1[1], "c")
    q3 = Question.Question(quesListLevel1[2], "c")
    q4 = Question.Question(quesListLevel1[3], "a")
    questions = [q1, q2, q3, q4]
    print(questions[0].prompt)
    print(questions[0].answer)
    print(questions[1].prompt)
    print(questions[2].prompt)
    print(questions[3].prompt)


intro()


