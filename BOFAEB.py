# coding: utf-8
import os, sys, time
from telethon import TelegramClient, events
import PostgreSQL

# Данные для подключения к API Telegram
api_id = 27497564
api_hash = '0e047d86aae06a1d04528be237fde107'
bot_token = '6864379726:AAFJ3kjlJYq7UNtVLfXuFZKCkSuFZnIWJ8Q'

# Список команд
commandList = ['/start', '/help', '/info', '/motivation', '/sendTo', '/whoami', '/mytask', '/addtask']

# Создание сущности бота
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Обработка команды /start
@client.on(events.NewMessage(pattern='/start'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /start от: {sender.id} {sender.username}')
    if len(message.text) == 6:
        if (PostgreSQL.selectUserID(sender.id)) == "":
            infoString = PostgreSQL.textFromFile("start_add.txt")
            PostgreSQL.addUser(sender.id, sender.username)
            print("Добавлен")
        else:
            infoString = PostgreSQL.textFromFile("start_unk.txt")
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
        infoString = PostgreSQL.textFromFile("help.txt")
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
        infoString = PostgreSQL.textFromFile("info.txt")
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
        file_path = 'w1.mp3'
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

@client.on(events.NewMessage(pattern='/addtask'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    if (len(message.text) > 9):
        print(f'Получена команда /addtask от: {sender.id} {sender.username}')
        textToSend = "Добавлена задача: " + message.text[8:len(message.text)]
        textToSend = textToSend + "ID задачи: {0}".format(PostgreSQL.lastTask())
        PostgreSQL.addTask(message.text[8:len(message.text)], sender.id)
        await client.send_message(chat, message=textToSend)
    else:
        await client.send_message(chat, message='Добавьте название для новой задачи')

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

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()

#Обработка неизвестного сообщения
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