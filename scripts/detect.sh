#!/bin/bash

python3 /app/yolov5/detect.py --weights /app/train_logs/yolov5x_baseline4/weights/best.pt --img 640 --conf 0.7 --source /app/data/train/images/val/ --name yolov5x_baseline4 --save-txt --save-conf --exist-ok --iou-thres 0.45