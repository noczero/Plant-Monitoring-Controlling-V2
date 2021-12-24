#!/bin/sh

echo "Start Jupyter Notebook Service"
jupyter notebook --ip=0.0.0.0 --port=8082 --NotebookApp.token='' --NotebookApp.password='' --no-browser
