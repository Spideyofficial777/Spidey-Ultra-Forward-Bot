FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y && apt install git -y

COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

WORKDIR /fwdbot
COPY . /fwdbot

RUN chmod +x /fwdbot/start.sh
CMD ["/bin/bash", "/fwdbot/start.sh"]
