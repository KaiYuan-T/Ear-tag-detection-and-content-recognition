
#After training on a custom dataset, the best weight is automatically stored in the runs/detect/train/weights directory as best.pt. When I retrain the model, I use the best.pt weight instead of yolov8x.pt to train the model.

echo "After training on a custom dataset, the best weight is automatically stored in the runs/detect/train/weights directory as best.pt. When I retrain the model, I use the best.pt weight instead of yolov8x.pt to train the model." >> tanky_train.log

nohup yolo detect train data=eartag.yaml model=yolov10n.yaml epochs=400 batch=256 imgsz=640 device=0,1 resume=true  save_period=5 optimizer=SGD cos_lr=True lr0=0.02 lrf=0.1 >> tanky_train.log 2>&1 &

