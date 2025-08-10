# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
import colorgram

rgb_colors = [

]
colors = colorgram.extract('tite.jpg', 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

# question_bank = [

# ]


# for question in question_data:
#     question_obj = Question(question["text"], question['answer'])
#     question_bank.append(question_obj)


# quiz = QuizBrain(question_bank)

# quiz.nextquestion()


# question_bank = [

# ]

# for question in question_data:
#     question_text = question['text']
#     question_answer = question['answer']
#     question_obj = Question(question_text, question_answer)
#     question_bank.append(question_obj)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()
