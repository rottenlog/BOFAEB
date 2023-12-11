FROM python
COPY ./ /BOFAEB/
COPY cronFile /etc/cron.d/cronFile
RUN pip install telethon asyncio psycopg2
RUN apt update ; apt install -y cron
RUN chmod +x /BOFAEB/run_scheduler
RUN chmod 0777 /etc/cron.d/cronFile
RUN chmod 0777 /BOFAEB/startDocker
RUN crontab /etc/cron.d/cronFile
WORKDIR /BOFAEB
EXPOSE 443
CMD /BOFAEB/startDocker