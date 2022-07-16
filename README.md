# Addaptive-Honeypot-System
Addaptive Honeypot System include SDN with floodlight controller and IDS using DNN

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
  
> **Redirect network traffic:** <br>
  **Referrence:**               https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/45645828/How+to+Perform+Transparent+Packet+Redirection+with+OpenFlow+and+Floodlight <br>
  **Note:** You should change the paremeter in flow1.json and flow2.json to your own option before running the shell script and change the directory where you store       flow1.json   and flow2.json in **addflow.sh** <br>
  **Add flow:** sudo ./add_flow.sh <br>
  **Delete flow:** sudo ./del_flow.sh
  
## IDS (in IDS directory)
> You can run the code in **jupyter notebook, google collab** <br>
  Data i collecting using Nmap for scanning attack (nmap_exploit.csv) and HKUST for normal traffic (Normal.csv)

> **Requirement** <br> 
  All necessary module in CSE-CIC-IDS-2018.ipynb <br>
  Dataset **CSE-CIC-IDS-2018** on training phase: https://www.unb.ca/cic/datasets/ids-2018.html <br>
  Predict data using Normal.csv and nmap_exploit.csv 
  
> **Note:** Before running code in CSE-CIC-IDS-2018.ipynb, change data, data1 and data2 variables to your own directory
   
