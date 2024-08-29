from ultralytics import YOLOv10

yolo10_pretrained = "/home/tanky/workspace/yolov10/yolov10n.pt"
cfg = "/home/tanky/workspace/yolov10/eartag.yaml"

# model = YOLOv10()
# If you want to finetune the model with pretrained weights, you could load the 
# pretrained weights like below
# model = YOLOv10.from_pretrained(yolo10_pretrained)
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
model = YOLOv10(yolo10_pretrained)

model.train(data=cfg, epochs=500, batch=256, imgsz=640)