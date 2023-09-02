# import other files
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# question_bank to make list and append each questions
question_bank = []
for data in question_data:
    # print(data)
    question = data["question"]
    answer = data["correct_answer"]
    # Using Question class
    new_question = Question(question, answer)
    question_bank.append(new_question)

# initialize QuizBrain Class (question_bank = question_list)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


