FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2
RUN apt update ; apt install -y cron
WORKDIR /BOFAEB
EXPOSE 443
CMD service cron start && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py