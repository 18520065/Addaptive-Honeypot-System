## SDN (in SDN directory)
> **Requirement** <br> 
  Docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04 <br>
  Containernet: https://github.com/containernet/containernet <br>
  Floodlight Controller: https://hub.docker.com/r/glefevre/floodlight <br>
  
> **Build Attacker:** <br> cd ./attacker/ <br> sudo docker build -t ubuntu:attacker . <br>
  **Build Client:** <br> cd ./client/ <br> sudo docker build -t ubuntu:client . <br>
  **Build Honeypot:** <br> cd ./honeypot/ <br> sudo docker build -t ubuntu:honeypot . <br>
  **Build Victim:** <br> cd ./victim/ <br> sudo docker build -t ubuntu:victim . <br>
  
> **Run code:** <br> 
  Before running sdn.py, change the BINDING_VOLUME variable to your own directory <br>
  sudo python3 sdn.py
