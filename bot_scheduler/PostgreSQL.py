# coding: utf-8
import os, sys, time, datetime
import psycopg2
from psycopg2 import sql


# Открывает соединение с БД
def openConnection():
    conn = psycopg2.connect(dbname='Ebbinghaus', user='postgres', password='2000dfyz', host='158.160.45.161')
    return conn

# Закрывает соединение с БД
def closeConnection(conn):
    conn.commit()
    conn.close()

# Проверка тасков
def checkTasks(date):
    date = str(date.strftime("%x %X"))
    # print(date[0:15] + "00")
    # print(date[0:15] + "59")
    # print(date[0:13] + "0:00")
    # print(date[0:13] + "9:59")
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, user_id, CAST(data_create AS VARCHAR) FROM Tasks WHERE data_create BETWEEN '{0}' AND '{1}'".format((date[0:13] + "0:00"),(date[0:13] + "9:59")))
    arr = [[],[]]
    i = 0
    for row in cursor:
        varRow = str(row)
        varRow = varRow[1:len(varRow)-1]
        print(varRow)
        startRow = []
        for i in range(0, len(varRow)):
            if varRow[i] == ",":
                startRow.append(i)
        arr.append([varRow[startRow[1]+2:startRow[2]],varRow[0:startRow[0]],varRow[startRow[0]+3:startRow[1]-1]])
    return arr
    closeConnection(conn)

# print(varRow[0:startRow[0]])
# print(varRow[startRow[0]+3:startRow[1]-1])
# print(varRow[startRow[1]+2:startRow[2]])
