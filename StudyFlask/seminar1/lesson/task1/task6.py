# Задание №6
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.get('/students/')
def students():
    students = [
        {'name': 'Ivan',
         'surname': 'Ivanov',
         'age': 21,
         'avg_mark': 5.0},
        {'name': 'Stepan',
         'surname': 'Yakovlev',
         'age': 25,
         'avg_mark': 4.0},
        {'name': 'Sidorov',
         'surname': 'Sergey',
         'age': 18,
         'avg_mark': 4.5}
    ]
    return render_template('students_task6.html', students=students)    #возвращается шаблон, который должен находится в папке templates проекта

@app.get('/html/')
def get_simple_html():
    text = """
        <h1>Моя первая html-страница</h1>
        <p>Привет, мир!</p>
    """
    return text

@app.get('/calc/<int:num1>/+/<int:num2>')
def calc_sum(num1, num2):
    summ = num1 + num2
    return f'{num1} + {num2} = {summ}'

@app.get('/')
def hello_world():
    return 'Hello world!'

@app.get('/about/')
def about():
    return 'About us.'

@app.get('/contacts/')
def contacts():
    return 'My contacts.'

if __name__ == "__main__":
    app.run(debug=True) #debug=True - позволяет вносить изменения в код при запущенном сервере.
                        #Также только в этом режиме видны ошибки в шаблонах.

