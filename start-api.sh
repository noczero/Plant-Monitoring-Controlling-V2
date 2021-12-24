#!/bin/sh

echo "Start API Service"
path_app="/home/pi/Plant-Monitoring-Controlling-V2"
echo $path_app
cd $path_app

uvicorn api.app:app --host 0.0.0.0 --reload --port 8081

