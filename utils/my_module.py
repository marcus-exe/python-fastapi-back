import cv2
from ultralytics import YOLO


model_path = r'./best.pt'

model = YOLO(model_path)

def ai_api(image_path):
    model.predict(source=image_path, show =True, save =True, show_labels=True,show_conf=False,conf=0.2,save_txt=False)