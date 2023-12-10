FROM python
RUN pip install telethon asyncio
COPY ./ /BOFAEB/
WORKDIR /app
EXPOSE 443