FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2; apt update ; apt install -y cron ; echo "*/1 * * * * /BOFAEB/run_scheduler" | crontab -
WORKDIR /BOFAEB
EXPOSE 443
CMD cron && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py