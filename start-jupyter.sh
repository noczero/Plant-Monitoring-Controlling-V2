#!/bin/bash

echo "Start Jupyter Notebook Service"
path_app="/home/pi/Plant-Monitoring-Controlling-V2"
echo $path_app
cd $path_app

jupyter notebook --ip=0.0.0.0 --port=8082 --NotebookApp.token='' --NotebookApp.password='' --no-browser
