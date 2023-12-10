FROM python
RUN pip install telethon asyncio
COPY ./BOFAEB/bot_respondent/ /app/BOFAEB_BOT/
COPY ./BOFAEB/answers/ /app/answers/
COPY ./BOFAEB/audio/ /app/audio/
WORKDIR /app
EXPOSE 443