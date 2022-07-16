FROM ubuntu:xenial
MAINTAINER manuel.peuster@uni-paderborn.de

RUN apt-get update && apt-get install -y \
	iproute \
	iputils-ping \
	net-tools \	
	tcpdump \
	gcc \
	make \
	git \
	build-essential \
	libpcap-dev \
	libnet1-dev \
	python 
	
WORKDIR /home
RUN git clone https://github.com/HKUST-SING/TrafficGenerator.git 

WORKDIR /home/TrafficGenerator
RUN make

COPY ./server.sh /home/TrafficGenerator
RUN chmod 777 server.sh

WORKDIR /home

CMD /bin/bash

