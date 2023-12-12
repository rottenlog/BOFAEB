FROM python
COPY ./ /BOFAEB/
RUN pip install telethon asyncio psycopg2
RUN apt update ; apt install -y cron
RUN cat /BOFAEB/cronfile >> /etc/crontab
WORKDIR /BOFAEB
EXPOSE 443
CMD service cron restart && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py