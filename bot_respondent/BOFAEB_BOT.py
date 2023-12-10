# coding: utf-8
from telethon import TelegramClient, events
import PostgreSQL, os, random

# Переменная для рандома цитаток
randCit = 7

# Список команд
commandList = ['/start', '/help', '/info', '/motivation', '/sendTo', '/whoami', '/mytask', '/addtask']

# Считывание данных пользователя
a = PostgreSQL.takeVars()

# Создание сущности бота
client = TelegramClient('bot', int(a[0]), a[1]).start(bot_token=a[2])

# Обработка команды /start
@client.on(events.NewMessage(pattern='/start'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /start от: {sender.id} {sender.username}')
    if len(message.text) == 6:
        if (PostgreSQL.selectUserID(sender.id)) == "":
            infoString = PostgreSQL.textFromFile("/BOFAEB/bot_respondent/answers/start_add.txt")
            PostgreSQL.addUser(sender.id, sender.username)
            print("Добавлен")
        else:
            infoString = PostgreSQL.textFromFile("/BOFAEB/bot_respondent/answers/start_unk.txt")
            print("Уже есть")
        await client.send_message(chat, message=infoString)
    else:
        await client.send_message(chat, message='Может быть /start?')

# Обработка команды /help
@client.on(events.NewMessage(pattern='/help'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /help от: {sender.id} {sender.username}')
    if len(message.text) == 5:
        infoString = PostgreSQL.textFromFile("/BOFAEB/bot_respondent/answers/help.txt")
        await client.send_message(chat, message=infoString)
    else:
        await client.send_message(chat, message='Может быть /help?')

# Обработка команды /info
@client.on(events.NewMessage(pattern='/info'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /info от: {sender.id} {sender.username}')
    if len(message.text) == 5:
        infoString = PostgreSQL.textFromFile("/BOFAEB/bot_respondent/answers/info.txt")
        await client.send_message(chat, message=infoString)
    else:
        await client.send_message(chat, message='Может быть /info?')

# Обработка команды /motivation
@client.on(events.NewMessage(pattern='/motivation'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /motivation от: {sender.id} {sender.username}')
    if len(message.text) == 11:
        file_path = '/BOFAEB/bot_respondent/audio/w{0}.mp3'.format(random.randint(1,randCit))
        await client.send_file(chat, file=file_path)
    else:
        await client.send_message(chat, message='Может быть /motivation?')

# Обработка команды /sendTo
@client.on(events.NewMessage(pattern='/sendTo'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /sendTo от: {sender.id} {sender.username}')
    if (sender.id == 2054454238):
        arr = PostgreSQL.findSpace(message.text)
        chatID = message.text[8:arr[1]]
        textToSend = message.text[arr[1]+1:]
        await client.send_message(chatID, message=textToSend)
        textToSend = 'Отправил: ' + textToSend
        await client.send_message(chat, message=textToSend)
    else:
        await client.send_message(chat, message='У вас нет прав')

# Обработка команды /whoami
@client.on(events.NewMessage(pattern='/whoami'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /whoami от: {sender.id} {sender.username}')
    textToSend = 'Твой ID: ' + PostgreSQL.selectUserID(sender.id) + '\n' + 'Твой ник: ' + PostgreSQL.selectUserName(sender.id)
    await client.send_message(chat, message=textToSend)

# Обработка команды /addtask
@client.on(events.NewMessage(pattern='/addtask'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    if (len(message.text) > 9):
        print(f'Получена команда /addtask от: {sender.id} {sender.username}')
        textToSend = "Добавлена задача: '" + message.text[9:len(message.text)] + "'"
        textToSend = textToSend + " ID задачи: {0}".format(PostgreSQL.lastTask())
        PostgreSQL.addTask(message.text[9:len(message.text)], sender.id)
        await client.send_message(chat, message=textToSend)
    else:
        await client.send_message(chat, message='Добавьте название для новой задачи')

# Обработка команды /mytask
# /mytask all
@client.on(events.NewMessage(pattern='/mytask')) 
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    if (len(message.text) == 7):
        print(f'Получена команда /mytask от: {sender.id} {sender.username}')
        textToSend = "Напишите '/mytask id' или '/mytask all'"
        await client.send_message(chat, message=textToSend)
    else:
        print(f'Получена команда /mytask от: {sender.id} {sender.username}')
        print(f'Содержимое сообщения: {message.text}')
        records = str(message.text)
        if (records[8:11]) == 'all':
            textToSend = PostgreSQL.selectAllTasks(sender.id)
            if textToSend != '[]' or textToSend != '':
                await client.send_message(chat, message="Выводиться: ID, название задачи, дата и время создания")
                await client.send_message(chat, message=textToSend)
            else:
                await client.send_message(chat, message="Я не нашел задач")
        else:
            try:
                if isinstance(int(records[8:len(records)]), int):
                    textToSend = PostgreSQL.selectIdTask(sender.id, records[8:len(records)])
                    if textToSend != '[]' or textToSend != '':
                        await client.send_message(chat, message="Выводиться: ID, название задачи, дата и время создания")
                        await client.send_message(chat, message=textToSend)
                    else:
                        await client.send_message(chat, message="Я не нашел задач")
            except ValueError:
                await client.send_message(chat, message="ID это целочисленное число. Проверьте ваше сообщение")

if __name__ == "__main__":
    PostgreSQL.createUsers()
    PostgreSQL.createTasks()
    client.start()
    client.run_until_disconnected()

# Обработка неизвестного сообщения
# @client.on(events.NewMessage)
# async def handle_new_message(event):
#     message = event.message
#     sender = await message.get_sender()
#     chat = await message.get_chat()
#     exist = 0
#     for i in range (0, 4):
#         if (message.text in commandList[i]) and (exist == 0):
#             print(message.text)
#             print(commandList[i])
#             exist = 1
#     if exist != 1:
#         print(f'Новое сообщение от: {sender.id} {sender.username}')
#         print(f'Содержимое сообщения: {message.text}')
#         infoString = PostgreSQL.textFromFile("unknown.txt")
#         await client.send_message(chat, message=infoString)