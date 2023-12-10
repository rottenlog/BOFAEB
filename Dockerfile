FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio ; apt update ; apt install -y cron
RUN echo "*/10 * * * * python3 /BOFAEB/bot_respondent/BOFAEB_BOT" | crontab -
WORKDIR /app
EXPOSE 443
CMD cron && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py