FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2; apt update ; apt install -y cron ; chmod 0644 /etc/cron.d/cronFile ; crontab /etc/cron.d/cronFile
WORKDIR /BOFAEB
EXPOSE 443
CMD crontab /etc/cron.d/cronFile && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py