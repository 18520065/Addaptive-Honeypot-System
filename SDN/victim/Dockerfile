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
	python \
	tcpdump

WORKDIR /home
RUN git clone https://github.com/HKUST-SING/TrafficGenerator.git 

WORKDIR /home/TrafficGenerator
RUN make

COPY ./server.sh /home/TrafficGenerator
COPY ./server2.sh /home/TrafficGenerator
RUN chmod 777 server.sh
RUN chmod 777 server2.sh


CMD /bin/bash
