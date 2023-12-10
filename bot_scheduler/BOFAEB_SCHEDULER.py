# coding: utf-8
import datetime, asyncio, psycopg2
from telethon import TelegramClient
from psycopg2 import sql

a = ['api_id','','','','','','']

# Считывает данные для аунтификации
def takeVars():
    i = 0
    lines = open('/BOFAEB/botVars.txt')
    for line in lines:
        a[i] = line.strip()
        i+=1

# Открывает соединение с БД
def openConnection():
    conn = psycopg2.connect(dbname=a[3], user=a[4], password=a[5], host=a[6])
    return conn

# Закрывает соединение с БД
def closeConnection(conn):
    conn.commit()
    conn.close()

# Проверка тасков
async def checkTasks(date):
    date = str(date.strftime("%x %X"))
    # print(date[0:15] + "00")
    # print(date[0:15] + "59")
    # print(date[0:13] + "0:00")
    # print(date[0:13] + "9:59")
    conn = openConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, user_id, CAST(data_create AS VARCHAR) FROM Tasks WHERE data_create BETWEEN '{0}' AND '{1}'".format((date[0:13] + "0:00"),(date[0:13] + "9:59")))
    i = 0
    for row in cursor:
        varRow = str(row)
        varRow = varRow[1:len(varRow)-1]
        startRow = []
        for i in range(0, len(varRow)):
            if varRow[i] == ",":
                startRow.append(i)
        #print (int(varRow[startRow[1]+2:startRow[2]]), 'ID: {0}\nЗадача: {1}'.format(varRow[0:startRow[0]],varRow[startRow[0]+3:startRow[1]-1]))
        await client.send_message(int(varRow[startRow[1]+2:startRow[2]]),'ID: {0}\nЗадача: {1}'.format(varRow[0:startRow[0]],varRow[startRow[0]+3:startRow[1]-1]))
    closeConnection(conn)

# Проверяет таски
async def scheduler():
    await client.start()
    date = datetime.datetime.now()
    # Проверяем таски созданные 20 минут назад
    varDate = date - datetime.timedelta(minutes=20)
    await checkTasks(varDate)
    # Проверяем таски созданные 12 часов назад
    varDate = date - datetime.timedelta(hours=12)
    await checkTasks(varDate)
    # Проверяем такси созданные 24 часа назад
    varDate = date - datetime.timedelta(hours=24)
    await checkTasks(varDate)
    # Проверяем такси созданные 72 часа назад
    varDate = date - datetime.timedelta(hours=72)
    await checkTasks(varDate)

if __name__ == "__main__":
    takeVars()
    client = TelegramClient('bot', int(a[0]), a[1]).start(bot_token=a[2])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scheduler())

# 0 повторение — изучение.
# 1 повторение — сразу после изучения.
# 2 повторение — через 10-20 минут после первого.
# 3 повторение — через 8-12 часов после второго.
# 4 повторение — через 24-32 часа после третьего.
# 5 повторение — через 3-5 дней после четвертого.

