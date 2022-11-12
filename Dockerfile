FROM nvcr.io/nvidia/pytorch:22.09-py3

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Ekaterinburg

WORKDIR /root

RUN apt-get update && apt-get -y install python3-pip ffmpeg libsm6 libxext6 libfreetype6-dev git

COPY requirements.txt requirements.txt

RUN python3 -m pip install --user -r requirements.txt

RUN python3 -m pip install --ignore-installed Pillow

WORKDIR /app
