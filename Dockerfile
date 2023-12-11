FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2
RUN apt update ; apt install -y cron
RUN chmod +x /BOFAEB/run_scheduler
RUN chmod 0777 /etc/cron.d/cronFile
RUN crontab /etc/cron.d/cronFile
RUN service cron start
WORKDIR /BOFAEB
EXPOSE 443
CMD python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py