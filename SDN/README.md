## SDN (Software Defined Networking)
**Requirement** <br> 
>  **Docker:** https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04 <br>
   **Containernet:** https://github.com/containernet/containernet <br>
   **Floodlight Controller:** https://hub.docker.com/r/glefevre/floodlight <br>
  
**Build Attacker:** <br> 
```bash
  cd ./attacker/ 
  sudo docker build -t ubuntu:attacker .
```
**Build Client:**
```bash
  cd ./client/
  sudo docker build -t ubuntu:client . 
```
**Build Honeypot:**
```bash
  cd ./honeypot/ 
  sudo docker build -t ubuntu:honeypot . 
``` 
**Build Victim:** 
```bash
  cd ./victim/
  sudo docker build -t ubuntu:victim .
```
**Run code:**
```bash
  # Note: Before running sdn.py, change the BINDING_VOLUME variable to your own directory
  sudo python3 sdn.py
```
## Redirect network traffic:
**Referrence:**               https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/45645828/How+to+Perform+Transparent+Packet+Redirection+with+OpenFlow+and+Floodlight <br>
**Note:** Change the paremeter in **flow1.json** and **flow2.json** to your own option before running the shell script <br>
**Note:** Change the directory where you store **flow1.json** and **flow2.json** in **addflow.sh**
```bash
  # Add flow redirect:
  sudo ./add_flow.sh 
  # or sudo bash add_flow.sh
```
```bash
  # Delete flow redirect: 
  sudo ./del_flow.sh 
  # or sudo bash del_flow.sh
```

