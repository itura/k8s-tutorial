FROM python:3.8-alpine

RUN apk update && apk upgrade

RUN mkdir /workdir
WORKDIR /workdir

COPY hello_world.py hello_world.py

CMD ["python", "-m", "hello_world"]

