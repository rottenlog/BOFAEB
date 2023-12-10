FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio ; apt update ; apt install -y cron ; crontab /etc/cron.d/cronFile
WORKDIR /app
EXPOSE 443
CMD cron && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py