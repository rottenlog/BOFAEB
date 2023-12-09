import os, sys, time, datetime
import PostgreSQL

from telethon import TelegramClient, events
import PostgreSQL

api_id = 27497564
api_hash = '0e047d86aae06a1d04528be237fde107'
bot_token = '6864379726:AAFJ3kjlJYq7UNtVLfXuFZKCkSuFZnIWJ8Q'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client.start()


if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
    
    date = datetime.datetime.now()
    # Проверяем таски созданные 20 минут назад
    varDate = date - datetime.timedelta(minutes=20)
    PostgreSQL.checkTasks(varDate)
    # Проверяем таски созданные 12 часов назад
    varDate = date - datetime.timedelta(hours=12)
    PostgreSQL.checkTasks(varDate)
    # Проверяем такси созданные 24 часа назад
    varDate = date - datetime.timedelta(hours=24)
    PostgreSQL.checkTasks(varDate)
    # Проверяем такси созданные 72 часа назад
    varDate = date - datetime.timedelta(hours=72)
    PostgreSQL.checkTasks(varDate)

# 0 повторение — изучение.
# 1 повторение — сразу после изучения.
# 2 повторение — через 10-20 минут после первого.
# 3 повторение — через 8-12 часов после второго.
# 4 повторение — через 24-32 часа после третьего.
# 5 повторение — через 3-5 дней после четвертого.

