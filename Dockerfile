FROM python:3.6.3-slim

RUN mkdir -p /code
WORKDIR /code

ADD ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT python
