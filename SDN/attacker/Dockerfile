FROM ubuntu:xenial
MAINTAINER manuel.peuster@uni-paderborn.de


RUN apt-get update && apt-get install -y \
	iproute \
	iputils-ping \
	net-tools \	
	tcpdump \
	hping3 \
	nmap 
	
WORKDIR /home

CMD /bin/bash
