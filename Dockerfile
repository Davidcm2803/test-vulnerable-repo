FROM python:3.9

USER root

ENV DB_PASSWORD=SuperSecret123

RUN pip install fastapi

ADD . /app

WORKDIR /app

EXPOSE 22

CMD ["python", "main.py"]
