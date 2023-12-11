FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2
RUN apt update ; apt install -y cro
RUN chmod +x /BOFAEB/run_scheduler
RUN chmod 0644 /etc/cron.d/cronFile
WORKDIR /BOFAEB
EXPOSE 443
CMD crontab /etc/cron.d/cronFile && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py