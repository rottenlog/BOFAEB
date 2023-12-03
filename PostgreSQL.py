# coding: utf-8
import os, sys, time, datetime
import psycopg2
from psycopg2 import sql


# Открывает соединение с БД
def openConnection():
    conn = psycopg2.connect(dbname='Ebbinghaus', user='postgres', password='2000dfyz', host='158.160.35.205')
    return conn

# Закрывает соединение с БД
def closeConnection(conn):
    conn.commit()
    conn.close()

# Создание таблицы пользователией
def createUsers():
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users
    (
    user_id INT PRIMARY KEY,
    user_name VARCHAR NOT NULL
    );
    """)
    closeConnection(conn)

# Создание таблицы с задачами
def createTasks():
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tasks
    (
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR NOT NULL,
    user_id INT NOT NULL,
    data_create timestamp NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    """)
    closeConnection(conn)

# Выводит список всех пользователей
def selectUsers():
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    records = cursor.fetchall()
    closeConnection(conn)

# Выводит user_id пользователя по id
def selectUserID(user_id):
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM Users WHERE user_id = (CAST({0} AS INTEGER))".format(user_id))
    records = cursor.fetchall()
    records = str(records)
    records = records[2:len(records)-3]
    closeConnection(conn)
    return str(records)

# Выводит user_name пользователя по id
def selectUserName(user_id):
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM Users WHERE user_id = (CAST({0} AS INTEGER))".format(user_id))
    records = cursor.fetchall()
    records = str(records)
    records = records[3:len(records)-4]
    closeConnection(conn)
    return str(records)

# Добавляется пользователя в БД
def addUser(user_id, user_name):
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (user_id, user_name) VALUES ({0}, '{1}');".format(user_id, user_name))
    closeConnection(conn)

# Добавляет задачу в БД
def addTask(task_name, user_id):
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Tasks (task_name, user_id, data_create) VALUES ('{0}', {1}, '{2}');".format(task_name, user_id, datetime.datetime.now()))
    closeConnection(conn)

# Определяет id последней задачи
def lastTask():
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id FROM Tasks ORDER BY task_id DESC LIMIT 1")
    records = cursor.fetchall()
    records = str(records)
    records = records[2:len(records)-3]
    closeConnection(conn)
    return str(records)

# Ищет пробелы в строке
def findSpace(string):
    arr = []
    for i in range(0, len(string)):
        if (string[i] == " "):
            arr.append(i)
    return arr

# Возвращает текст из файла
def textFromFile(name):
    file = open(name)
    infoString = file.read()
    return infoString
    file.close()#addUser(2054454238, "rottenlog")   

createUsers()
createTasks()
# print(lastTask())
# addTask('lol', 2054454238)
# print(lastTask())
# addTask('lol', 2054454238)