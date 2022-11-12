#!/bin/bash

if ! [ -d /app/yolov5 ]
then
    echo "Directory yolov5 is not found. Downloading..."
    cd /app && git clone https://github.com/ultralytics/yolov5.git
fi

python3 /app/yolov5/train.py --img 320 --batch 2 --epochs 100 --data /app/data/train/v8/dataset.yaml --name yolov5x_dv8_tmp --weights yolov5x.pt --hyp /app/yolov5/data/hyps/hyp.scratch-low.yaml --project /app/train_logs --cache ram --patience 20 --bbox_interval 1 --exist-ok
