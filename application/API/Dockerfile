# Dockerfile
FROM ubuntu:22.04
WORKDIR /api
COPY . .
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip
RUN pip3 install -r ./requirements.txt
RUN apt install -y default-jre
RUN apt install -y default-jdk