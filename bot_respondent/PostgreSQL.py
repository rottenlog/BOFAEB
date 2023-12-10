# coding: utf-8
import psycopg2, datetime, os
from psycopg2 import sql
a = ['api_id','','','','','','']

# Считывает данные для аунтификации
def takeVars():
    i = 0
    lines = open('./botVars.txt')
    for line in lines:
        a[i] = line.strip()
        i+=1
    return a

# Открывает соединение с БД
def openConnection():
    conn = psycopg2.connect(dbname=a[3], user=a[4], password=a[5], host=a[6])
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
    date = datetime.datetime.now().strftime("%x %X")
    cursor.execute("INSERT INTO Tasks (task_name, user_id, data_create) VALUES ('{0}', {1}, '{2}');".format(task_name, user_id, date))
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

# Определяет все задачи пользователя
def selectAllTasks(user_id):
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, to_char(data_create, 'dd-mm-yyyy hh24:mi:ss') FROM Tasks WHERE user_id = {0}".format(user_id))
    records = ''
    for row in cursor:
        varRow = str(row)
        records += varRow[1:len(varRow)-1] + "\n"
    closeConnection(conn)
    return str(records)

# Определяет определенную задачу пользователя по id
def selectIdTask(user_id, task_id):
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, to_char(data_create, 'dd-mm-yyyy hh24:mi:ss') FROM Tasks WHERE user_id = {0} AND task_id = {1}".format(user_id, task_id))
    records = str(cursor.fetchall())
    records = records[2:len(records)-2]
    closeConnection(conn)
    return str(records)

# Определяет такси
def checkTasks(date):
    date = str(date.strftime("%x %X"))
    # print(date[0:15] + "00")
    # print(date[0:15] + "59")
    # print(date[0:13] + "0:00")
    # print(date[0:13] + "9:59")
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, user_id, CAST(data_create AS VARCHAR) FROM Tasks WHERE data_create BETWEEN '{0}' AND '{1}'".format((date[0:13] + "0:00"),(date[0:13] + "9:59")))
    for row in cursor:
        varRow = str(row)
        varRow = varRow[1:len(varRow)-1]
        print(varRow)
        startRow = []
        for i in range(0, len(varRow)):
            if varRow[i] == ",":
                startRow.append(i)
        # print(varRow[0:startRow[0]])
        # print(varRow[startRow[0]+3:startRow[1]-1])
        # print(varRow[startRow[1]+2:startRow[2]])
        sendToUser

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
    file.close()
