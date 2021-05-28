# the data from https://opentdb.com
from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_number in range(len(question_data)):
    question = QuestionModel(question_data[question_number]["question"], question_data[question_number]["correct_answer"])
    question_bank.append(question)

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

# while there is a number of question the loop will running
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz and your final score is : ", quiz.score, " / ", len(question_bank))
