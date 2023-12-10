FROM python
COPY ./ /BOFAEB/
RUN pip install telethon asyncio ; apt update ; apt install -y cron ; crontab -l /BOFAEB/bot_scheduler/cronFile
WORKDIR /app
EXPOSE 443
CMD cron && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py