# We build from python3.6 which provides a python3.6 insatlled ubuntu OS.
FROM python:3.8.1

# Set working directory within docker container
WORKDIR /usr/src/boticario

# Copy python reqs
COPY requirements.txt ./

# Install reqs
RUN pip install --no-cache-dir -r requirements.txt

# Specity flask app entry point
ENV FLASK_APP=boticario.py

# Necessary Folders
COPY app ./app
COPY migrations ./migrations

# Necessary Files
COPY .env config.py boticario.py boot.sh gunicorn.ini ./
RUN chmod +x ./boot.sh

# Expose port
EXPOSE 8000

# Specify entry point script
ENTRYPOINT ["./boot.sh"]