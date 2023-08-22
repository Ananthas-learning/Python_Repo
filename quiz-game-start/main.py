from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    answer = question["answer"]
    new_q = Question(q_text, answer)
    question_bank.append(new_q)

my_quiz = QuizBrain(question_bank)

while my_quiz.still_has_questions():
    my_quiz.next_question()




