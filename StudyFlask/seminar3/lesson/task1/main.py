# Задание №1
# 📌 Создать базу данных для хранения информации о студентах университета.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# 📌 В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# 📌 Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

from flask import Flask, render_template
from models import db, Faculty, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db.init_app(app)

# чтобы запустить в командной строке дать команду: flask init-db
# в каталоге проекта должен быть файл wsgi.py
# запуск в командной строке из пути проекта
# после выполнения, файл БД появится в проекте в подкаталоге instance
# работать с файлом SQLite можно с помощью DBeaver, SQLite Studio
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('init-db OK')


# наполнение БД тестовыми данными
# для запуска набрать в терминале команду: flask fill-db
@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем факультеты
    for number in range(1, count + 1):
        faculty = Faculty(title=f'faculty_{number}')
        db.session.add(faculty)
        db.session.commit()

        # Добавляем студентов
        for student_number in range(1, count+1):
            new_student = Student(
                name=f'name_{student_number}',
                surname=f'surname_{student_number}',
                age=22+student_number,
                gender='male',
                group_number=f'{student_number}_{12}',
                faculty_id=faculty.id
            )
            db.session.add(new_student)
            db.session.commit()

    print('fill-db OK')


@app.route('/')
def all_users():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)

# запускать надо файл wsgi.py