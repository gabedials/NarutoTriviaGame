"""This is my main file for my Naruto Integration Project
__author__ = "Gabe Dials"
"""

# Gabe Dials
# NarutoTriviaGame

import Question


# new function do_test


def do_test(questions):
    """
    Gives the instructions on how to run my test
    :param questions:
    :return:
    """

    score = 0
    total_score = 0
    for ques in questions:
        answer = input(ques.prompt)

        if answer == ques.answer:
            score += 1
    total_score += score
    if total_score >= 5:
        print("You've reached Jonin level!")
    elif 3 <= total_score <= 4:
        print("You've reached Chunin level!")
    else:
        print("Keep training, and you'll soon be a Chunin!")
    print("Ninja Knowledge: " + str(total_score) + "/" + str(
        len(questions)) + " correct")
    print("If you would like to learn more, select a character: ")


# new function main


def main():
    """
    Contains the introductory to my program as well as the questions for the
    test
    :return:
    """
    print("hello!")
    print("Welcome to A Naruto Adventure")
    name = input("What is your name?")
    # add kun to end of name
    print("Cool! Your Ninja Name is", name + "-kun")
    entered_num = int(input("type 1 if you are ready to start: "))
    if entered_num == 1:
        print("Lets Begin! **SPOILERS AHEAD**")
    else:
        print("You must enter 1 to start")
        entered_num = int(input("type 1 if you are ready to start: "))
        # next line starts my list
    ques_list_level1 = [
        "What clan is Naruto in?\n(a) Sarutobi\n(b) Uzumaki\n(c) Uchiha\n\n",
        "What clan is Sasuke in?\n(a) Sarutobi\n(b) Uzumaki\n(c) Uchiha\n\n",
        "What clan is Itachi in?\n(a) Sarutobi\n(b) Uzumaki\n(c) Uchiha\n\n",
        "What village does Naruto live in?\n(a) Hidden Leaf\n(b) Hidden Sand\n"
        "(c) Hidden Sound\n\n",
        "What village does Gaara live in?\n(a) Hidden Leaf\n(b) Hidden Sand\n"
        "(c) Hidden Sound\n\n",
        "How many tailed beasts are there?\n(a) 1 \n(b) 5\n(c) 9\n\n",
        "Who is on team 7?\n(a) Naruto, Sasuke, Kakashi \n"
        "(b) Naruto, Sasuke, Sakura\n(c) Naruto, Sasuke, Rock L\n\n"

    ]

    q1 = Question.Question(ques_list_level1[0], "b")
    q2 = Question.Question(ques_list_level1[1], "c")
    q3 = Question.Question(ques_list_level1[2], "c")
    q4 = Question.Question(ques_list_level1[3], "a")
    q5 = Question.Question(ques_list_level1[4], "b")
    q6 = Question.Question(ques_list_level1[5], "c")
    q7 = Question.Question(ques_list_level1[6], "b")

    questions = [q1, q2, q3, q4, q5, q6, q7]

    do_test(questions)


# main execution below
main()
input("\n\nPress the enter key to exit.")
