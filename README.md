# Setup Raspberry Pi
This command run 
```bash

# Python Package
$  sudo apt-get install python3-dev python3-pip
$  sudo apt-get update
$  sudo python3 -m pip install --upgrade pip setuptools wheel
$  sudo pip3 install Adafruit_DHT
$  sudo pip3 install adafruit-circuitpython-bh1750
$  sudo pip3 install adafruit-blinka
$  sudo apt-get install build-essential python-dev python-smbus python-pip
$  sudo pip install adafruit-ads1x15
$  sudo pip3 install adafruit-ads1x15

# Docker Setup
$  sudo apt-get update
$  sudo apt-get upgrade
$  curl -fsSL https://get.docker.com -o get-docker.sh
$  sudo sh get-docker.sh
$  sudo usermod -aG docker pi
$  sudo reboot
$  sudo pip3 install docker-compose
$  sudo systemctl enable docker

# Change python default to 3.7
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --list python
```

