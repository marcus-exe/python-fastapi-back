import cv2
from ultralytics import YOLO

model_path = r'best.pt'

image_path = '../input/teste.jpeg'


model = YOLO(model_path)

model.predict(source=image_path, show =True, save =True, show_labels=True,show_conf=False,conf=0.2,save_txt=False)