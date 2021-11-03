FROM balenalib/raspberry-pi-debian-python:3.8.12-buster
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app/app.py" ]