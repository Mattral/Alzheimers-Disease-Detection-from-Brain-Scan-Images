
from PIL import Image
import cv2
import numpy as np
from fastapi import FastAPI, UploadFile
from .utils import classify_img,get_alzheimer_model

app = FastAPI(title="Alzheimer Detection API")

@app.get("/")
def display():
    return "Welcome to Alzheimer Detection Api"

model= get_alzheimer_model()

@app.post("/predict")
def predict(file: UploadFile):
    img=Image.open(file.file)
    img=np.array(img)

    # Ensure RGB format for both JPG and PNG images
    if img.shape[-1] == 4:
        img = img[:, :, :3]

    if len(img.shape) == 2:
        img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

    img=cv2.resize(img,(176, 176))
    label,probability=classify_img(model,img)
    return {"label":label.item(),"probability":probability.item()}