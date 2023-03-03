FROM python:3.9.16-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN adduser app-user
RUN chown app-user /flask-app
USER app-user

CMD ["python3", "main.py"]

EXPOSE 5001
