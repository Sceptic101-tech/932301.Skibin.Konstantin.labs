from flask import Flask, render_template, url_for, request, redirect
import random
app = Flask(__name__)

questions = {}
correct_num = 0

def generate_equation():
    new_question = len(questions)
    questions[new_question] = {}
    first_num = int(random.randint(0, 9)) # in range [0, 9]
    second_num = int(random.randint(-9, 9)) # in range [-9, 9]

    questions[new_question]['first_num'] = first_num
    questions[new_question]['second_num'] = abs(second_num)
    questions[new_question]['operator'] = '-' if second_num < 0 else '+'
    questions[new_question]['correct_ans'] = first_num + second_num
    questions[new_question]['user_ans'] = 0
    questions[new_question]['is_correct'] = False

@app.route("/")
def redirecter():
    return redirect(url_for('index'))

@app.route("/Mockups")
def index():
    questions = {}
    return render_template('index.html')

@app.route("/Mockups/Quiz", methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        last_question = len(questions)-1
        answer = int(request.form.get('answer').strip())
        action = request.form.get('action')
        questions[last_question]['user_ans'] = answer
        questions[last_question]['is_correct'] = int(answer == questions[last_question]['correct_ans'])
        if action == 'next':
            return redirect(url_for('quiz'))
        elif action == 'finish':
            correct_num = 0
            for _, question_dict in questions.items():
                correct_num += int(question_dict['is_correct'])
            return render_template('quiz_result.html', correct_num=correct_num, all_num=len(questions), questions=questions)
    else:
        generate_equation()
        last_question = len(questions)-1
        return render_template('quiz.html', first_num=questions[last_question]['first_num'],
                        operator=questions[last_question]['operator'],
                        second_num=questions[last_question]['second_num'])

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')
