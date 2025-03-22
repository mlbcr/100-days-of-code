from data import question_data
from question_model import Question
from random import shuffle
from quiz_brain import QuizBrain

nq = QuizBrain()
points = 0
shuffle(question_data)
for q in question_data:
    question = Question(q["text"], q["answer"])
    guess = input(f"Q{nq.question_number}:{question.text} True or False? ")


    if question.compare_question(guess):
        points += 1
        print(f"You got it right! Points: {points}")
        nq.next_question()

    elif points == 0:
        print('You lost.')
        break

    else:
        points -= 1
        print(f"It's incorrect. Points: {points}")