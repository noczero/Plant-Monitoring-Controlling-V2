#!/bin/sh

echo "Start API Service"
uvicorn api.app:app --host 0.0.0.0 --reload --port 8081

echo "Start Jupyter Notebook Service"
jupyter notebook --ip=0.0.0.0 --port=8082 --NotebookApp.token='' --NotebookApp.password=''
