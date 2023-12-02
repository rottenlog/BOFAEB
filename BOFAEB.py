# coding: utf-8
import os, sys, time
from telethon import TelegramClient, events

# Данные для подключения к API Telegram
api_id = 27497564
api_hash = '0e047d86aae06a1d04528be237fde107'
bot_token = '6864379726:AAFJ3kjlJYq7UNtVLfXuFZKCkSuFZnIWJ8Q'

# Список команд
commandList = ['/start', '/help', '/info', '/motivation']

# Создание сущности бота
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

def textFromFile(name):
    file = open(name)
    infoString = file.read()
    return infoString
    file.close()

# Обработка команды /start
@client.on(events.NewMessage(pattern='/start'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /start от: {sender.username}')
    if len(message.text) == 6:
        infoString = textFromFile("start.txt")
        await client.send_message(chat, message=infoString)
    else:
        await client.send_message(chat, message='Может быть /start?')

# Обработка команды /help
@client.on(events.NewMessage(pattern='/help'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /help от: {sender.username}')
    if len(message.text) == 5:
        infoString = textFromFile("help.txt")
        await client.send_message(chat, message=infoString)
    else:
        await client.send_message(chat, message='Может быть /help?')

# Обработка команды /info
@client.on(events.NewMessage(pattern='/info'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /info от: {sender.username}')
    if len(message.text) == 5:
        infoString = textFromFile("info.txt")
        await client.send_message(chat, message=infoString)
    else:
        await client.send_message(chat, message='Может быть /info?')

# Обработка команды /motivation
@client.on(events.NewMessage(pattern='/motivation'))  
async def handle_start_command(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(f'Получена команда /motivation от: {sender.username}')
    if len(message.text) == 11:
        file_path = 'w1.mp3'
        await client.send_file(chat, file=file_path)
    else:
        await client.send_message(chat, message='Может быть /motivation?')

# Обработка неизвестного сообщения
@client.on(events.NewMessage)
async def handle_new_message(event):
    message = event.message
    sender = await message.get_sender()
    chat = await message.get_chat()
    if message.text not in commandList:
        print(f'Новое сообщение от: {sender.username}')
        print(f'Содержимое сообщения: {message.text}')
        infoString = textFromFile("unknown.txt")
        await client.send_message(chat, message=infoString)

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()