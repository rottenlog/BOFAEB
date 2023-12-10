FROM python
RUN pip install telethon asyncio
COPY bot_respondent/ /app/BOFAEB_BOT/
COPY answers/ /app/answers/
COPY audio/ /app/audio/
WORKDIR /app
EXPOSE 443