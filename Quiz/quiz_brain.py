class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: "
                            f"{self.questions_list[self.question_number].text}. (True/False)?: ")

        # check the answer
        self.check_answer(user_answer, self.questions_list[self.question_number].answer)
        # increment the number to take the next question
        self.question_number += 1

    def still_has_questions(self):
        if len(self.questions_list) != self.question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.upper() == correct_answer.upper():
            self.score += 1
            print("Great it is the correct answer ")
        else:
            print("sorry the answer is wrong")
        print(f"Your current score is : {self.score}/{self.question_number + 1} \n")

# TODO: 1. asking the questions
# TODO: 2. checking if the answer was correct
# TODO: 3. checking if we are the of the quiz
