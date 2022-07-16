#!/usr/bin/python

from mininet.net import Containernet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

# Change BINDING_VOLUME variable to your own directory in your current machine running this code
BINDING_VOLUME = f'{FOLDER_ROOT}:/home/TrafficGenerator/TCPDUMP_and_CICFlowMeter'

net = Containernet(controller=Controller)
# Create and connect to Controller
info('*** Adding controller\n')
c0 = RemoteController('c0', ip='127.0.0.1', port=6653)
net.addController(c0)
# Create Host for SDN network.
info('*** Adding docker containers\n')
d1 = net.addDocker('d1', ip='10.0.0.1', mac='00:00:00:00:00:01', dimage="ubuntu:attacker")
d2 = net.addDocker('d2', ip='10.0.0.2', volumes=[BINDING_VOLUME], mac='00:00:00:00:00:02', dimage="ubuntu:victim")
d3 = net.addDocker('d3', ip='10.0.0.3', volumes=[BINDING_VOLUME], mac='00:00:00:00:00:03', dimage="ubuntu:honeypot")
d4 = net.addDocker('d4', ip='10.0.0.4', mac='00:00:00:00:00:04', dimage="ubuntu:client")
d5 = net.addDocker('d5', ip='10.0.0.5', mac='00:00:00:00:00:05', dimage="ubuntu:client")
d6 = net.addDocker('d6', ip='10.0.0.6', mac='00:00:00:00:00:06', dimage="ubuntu:client")
d7 = net.addDocker('d7', ip='10.0.0.7', mac='00:00:00:00:00:07', dimage="ubuntu:client")
d8 = net.addDocker('d8', ip='10.0.0.8', mac='00:00:00:00:00:08', dimage="ubuntu:client")
# Create Switch for SDN network
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
# Create Link between Host and Switch
info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(d2, s1)
net.addLink(d3, s1)
net.addLink(d4, s1)
net.addLink(d5, s1)
net.addLink(d6, s1)
net.addLink(d7, s1)
net.addLink(d8, s1)
# Create SDN network
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2, d3, d4, d5, d6, d7, d8])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()

