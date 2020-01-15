FROM python:3.8-alpine

RUN apk update && apk upgrade
RUN pip install --upgrade pip

RUN mkdir /workdir
WORKDIR /workdir

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY hello_world.py hello_world.py

CMD ["python", "-m", "hello_world"]

