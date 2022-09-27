#!/bin/bash

## Checking root access
if [ $EUID -ne 0 ]; then
	ee "This script has to be ran as root!"
fi

sudo true
sudo apt update
sudo apt -y upgrade
sudo apt install curl

echo -e "\n\n"

function pause(){

 read -s -n 1 -p "Pulse cualquier tecla para continuar. . ."
 echo -e "\n\n[ * ] INSTALANDO WEBMIN...\n\n"
 sleep 3
 clear
}
## Pause it ##
pause
## rest of script below

sudo curl -fsSL https://download.webmin.com/jcameron-key.asc | sudo gpg --dearmor -o /usr/share/keyrings/webmin.gpg

sudo echo "deb [signed-by=/usr/share/keyrings/webmin.gpg] http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list

sudo apt update

sudo apt install -y webmin

sudo ufw allow 10000

clear

echo -e "\n\n"
echo "[ * ] WEBMIN INSTALADO CORRECTAMENTE"
sleep 2
echo -e "\n"
echo "SACANDO URL. . ."
echo -e "\n"
sleep 2
echo "https://Ip_Address:10000"



ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'
