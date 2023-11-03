# Создание подключения к базе данных
# FastAPI предоставляет встроенную поддержку работы с базами данных. Мы
# обсудим, как создать подключение к базе данных и выполнить миграцию базы
# данных в FastAPI. FastAPI поддерживает различные базы данных, такие как SQLite,
# PostgreSQL, MySQL и MongoDB. Выбор базы данных зависит от требований и
# предпочтений проекта.
# Рассмотрим, как создать подключение к базе данных и выполнить миграцию базы
# данных с использованием SQLAlchemy ORM и базы данных SQLite.
# SQLite — это облегченная система управления реляционными базами данных на
# основе SQL.
# Чтобы создать соединение с базой данных, нам нужно определить конфигурацию
# базы данных и использовать библиотеку ORM (Object-Relational Mapping), такую как
# Tortoise ORM, SQLAlchemy или Peewee.
# 🔥Важно! Если вы не устанавливали SQLAlchemy и databases раньше,
# выполните команды:
# pip install sqlalchemy
# pip install databases[aiosqlite]
# В этом примере мы используем SQLAlchemy для создания подключения к базе
# данных SQLite. Переменная DATABASE_URL определяет строку подключения.
# 8
# Событие запуска используется для создания схемы базы данных. Событие
# выключения используется для удаления ядра базы данных.
# Подключение к PostgreSQL
# Если мы хотим зменить SQLite на PostgreSQL, достоточно заменить данные в
# константе подключения к БД:
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
# Указав тип базы данных, имя пользователя, пароль, хост и название базы данных
# мы установим с ней соединение.

# Пример:

import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
