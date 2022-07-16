FROM ubuntu:trusty
MAINTAINER manuel.peuster@uni-paderborn.de


RUN apt update && apt install -y \
	gcc \
	make \
	git \
	build-essential \
	libpcap-dev \
	libnet1-dev \
	htop \
	python

WORKDIR /home
RUN git clone https://github.com/HKUST-SING/TrafficGenerator.git 

WORKDIR /home/TrafficGenerator
RUN make

COPY ./client_cfg.txt /home/TrafficGenerator/conf
COPY ./client_cfg2.txt /home/TrafficGenerator/conf
COPY ./client.sh /home/TrafficGenerator
COPY ./client2.sh /home/TrafficGenerator
RUN chmod 777 client.sh
RUN chmod 777 client2.sh
CMD /bin/bash
