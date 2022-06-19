FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
CMD ["/usr/bin/python", "bot.py"]