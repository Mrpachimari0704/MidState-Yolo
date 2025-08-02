from ultralytics import YOLOv10
# Load a model
# model = YOLOv10.from_pretrained('jameslahm/yolov10n')
model = YOLOv10('cfg/models/v10/yolov10n+C2f-DualConv.yaml')
# train
model.train(data='cfg/datasets/data.yaml',
                cache=False,
                imgsz=640,
                epochs=30,
                batch=16,
                device='0',
                optimizer='SGD', # using SGD
                )