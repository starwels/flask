FROM python:3.8.1

WORKDIR /usr/src/boticario

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

COPY app ./app
COPY migrations ./migrations
COPY .env config.py app.py boot.sh gunicorn.ini ./
RUN chmod +x ./boot.sh

EXPOSE 8000

ENTRYPOINT ["./boot.sh"]