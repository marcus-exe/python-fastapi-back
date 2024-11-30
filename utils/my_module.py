import cv2
import os
from ultralytics import YOLO

def ai_api(image_path, model_path):
    model = YOLO(model_path)
    model.predict(
        source=image_path, 
        show =False, 
        save =True,
        show_labels=True,
        show_conf=False,
        conf=0.2,
        save_txt=False
        )