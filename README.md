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

# How to Run Apps
1. Konek ke reaspi, pakai teamviewer atau pakai monitor.
2. Buka terminal
3. cd ~/Plant-Monitoring-Controlling
4. cd app
5. python app.py

# How to reset databade
1. Buka terminal 
2. cd ~/Plant-Monitoring-Controlling
3. docker-compose down -v
4. docker-compose up -d
5. Buka phpmyadmin, bisa  cek IP raspi, kemudian di laptop lain dengan satu jaringan, bnuka browser 
ketik url IPrasI:8080
6. Pilih database plant, masuk ke menu SQL, copy query yang ada di query_create_table.sql
 kemudian tekan go.
7. Jalankan aplikasi pada step sebelunmya.

# How to change plant name
1. Masuk ke folder project
2. edit file .env pakai nano
```bash
nano .env
```
Edit PLANT_LIST dengan nama yang diinginakn.
untuk save tekan ctrl + x kemudian tekan y
3. docker-compose up -d


# How to run API service
1. Jalankan service
```bash
$ docker-compose up -d
```
2. Buka browser, ketik url localhost:8081

# Add script to boot
1. Make script link 
``` bash
$ ln -s start-api.sh start-api
$ ln -s start-jupyter.sh start-jupyter
```
2. Copy start-services-plant to /etc/init.d

3. Executer following command
```bash 
$ sudo chmod 755 /etc/init.d/start-services-plant
$ sudo update-rc.d start-services-plant defaults 
```
2. Using services, execute this command
```bash

# copy files
$ sudo cp start-api.service /etc/systemd/system/
$ sudo cp start-jupyter.service /etc/systemd/system/

# enable service
$ systemctl daemon-reload
$ systemctl enable start-api.service
$ systemctl enable start-jupyter.service

```


# How to run final application
Execute following command in terminal.
1. Start API service
```bash
$ start-api
```

2. Start App
Open new terimnal
```bash
$ cd ~/Plant-Monitoring-Controlling-V2/app
$ python app.py
```

# Training Ulang
1. Ubah mode di .env jadi  MODE=TRAINING
2. Ketika sudah selesai, export data ke file .csv
3. Buat models di jupyter notebooks, dengan nama file dataset yang disesuaikan. dan file model.sav yang disesuaikan di file API. 

misalnya :
  * dataset : dataset_kale_A.csv
Autogenerate (dari notebooks) :
  * dataset_kale_A.xlsx 
  * trained/kale_dt_model_A.sav

# Testing ulang
1. Ganti nilai MODE=TESTING
2. Sesuaikan api/router/dt_endpoint.py dengan hasil model
```python
            self.trained_model = pickle.load(open('api/trained/kale_dt_model_2.sav', 'rb'))
```
3. Jalankan service api
4. jalankan aplikasi utama


