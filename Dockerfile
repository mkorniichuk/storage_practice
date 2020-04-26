FROM python:alpine

RUN pip install flask
EXPOSE 5000

WORKDIR /src

ENTRYPOINT ["python", "main.py"]