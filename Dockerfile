FROM python
COPY ./ /BOFAEB/
RUN pip install telethon asyncio && crontab /BOFAED/bot_scheduler/cronFile
WORKDIR /app
EXPOSE 443
CMD cron && python3 /BOFAEB/bot_respondent/BOFAEB_BOT.py