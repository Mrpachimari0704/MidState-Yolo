from ultralytics import YOLOv10
# 加载训练好的模型或者网络结构配置文件
model = YOLOv10('F:\\xianyu\\2024.7.8\\yolov10\\runs\detect\\batch_size=32\\25\\YOLOv10n-tov8-2+EMA-25-2\\weights\\best.pt')
# 打印模型参数信息
print(model.info())

