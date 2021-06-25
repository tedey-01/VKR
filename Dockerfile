FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && apt-get install poppler-utils -y

RUN apt-get update \
    && apt install -y wget \
    && apt-get install apt-transport-https -y \
    && apt install --no-install-recommends -y build-essential gcc\
    && apt-get install -y software-properties-common \
    && apt clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx


WORKDIR /usr/src
COPY . /usr/src

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

