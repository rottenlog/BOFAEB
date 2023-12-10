FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2; apt update ; apt install -y cron ; echo "*/10 * * * * python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py &" | crontab -
WORKDIR /app
EXPOSE 443
CMD cron && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py &