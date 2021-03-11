from PIL import Image
from yolov5 import YOLOv5

# set model params
model_path = "detection_weights.pt" # it automatically downloads yolov5s model to given path
device = "cuda" # or "cpu"

# init yolov5 model
yolov5 = YOLOv5(model_path, device)

# load images
image1 = Image.open("input/trash.jpg")

# perform inference
results = yolov5.predict(image1)

