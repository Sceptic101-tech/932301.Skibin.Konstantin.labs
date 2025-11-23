from flask import Flask, render_template, url_for, request
app = Flask(__name__)

def calc_result(first_num:int, operand:str, second_num:int)->str:
    if operand == '+':
        return str(first_num + second_num)
    if operand == '-':
        return str(first_num - second_num)
    if operand == '*':
        return str(first_num * second_num)
    if second_num != 0:
        return str(first_num / second_num)
    else:
        return 'Деление на 0 не поддерживается'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Calc/Manual", methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        try:
            first_num=int(request.form['first_num'])
            operand=request.form['operand']
            second_num=int(request.form['second_num'])
        except:
            Exception('Ошибка при обработке полученных данных')
        return render_template('extended_result.html',
                               first_num=first_num,
                               operand=operand,
                               second_num=second_num,
                               result=calc_result(first_num, operand, second_num))
    else:
        return render_template('manual.html')

@app.route("/Calc/ManualWithSeparateHandlers", methods=['GET', 'POST'])
def ManualWithSeparateHandlers():
    if request.method == 'POST':
        try:
            first_num=int(request.form['first_num'])
            operand=request.form['operand']
            second_num=int(request.form['second_num'])
        except:
            Exception('Ошибка при обработке полученных данных')
        return render_template('extended_result.html',
                               first_num=first_num,
                               operand=operand,
                               second_num=second_num,
                               result=calc_result(first_num, operand, second_num))
    else:
        return render_template('manual_with_separate_handlers.html')

@app.route("/Calc/ModelBindingInParameters", methods=['GET', 'POST'])
def ModelBindingInParameters():
    if request.method == 'POST':
        try:
            first_num=int(request.form['first_num'])
            operand=request.form['operand']
            second_num=int(request.form['second_num'])
        except:
            Exception('Ошибка при обработке полученных данных')
        return render_template('truncated_result.html',
                               result=calc_result(first_num, operand, second_num))
    else:
        return render_template('model_binding_in_parameters.html')

@app.route("/Calc/ModelBindingInSeparateModel", methods=['GET', 'POST'])
def ModelBindingInSeparateModel():
    if request.method == 'POST':
        try:
            first_num=int(request.form['first_num'])
            operand=request.form['operand']
            second_num=int(request.form['second_num'])
        except:
            Exception('Ошибка при обработке полученных данных')
        return render_template('truncated_result.html',
                               result=calc_result(first_num, operand, second_num))
    else:
        return render_template('model_binding_in_separate_model.html')

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')
