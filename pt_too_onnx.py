from torch.autograd import Variable
import torch.onnx
import torchvision
import torch
from PIL import Image
import numpy as np

# img_label = "trash"
# img = Image.open(f"input/{img_label}.jpg")
# img = img.resize((640, 480))
# img = np.asarray(img) / 255.
# print(len(img[0][1]))
# opt.device = torch.device('cuda:0')
dummy_input = Variable(torch.randn(480, 640, 3))
# dummy_input = Variable(img)
model = torch.load('./pretrained/AdaBins_nyu.pt')
# dummy_output = model(dummy_input)
torch.onnx.export(model, dummy_input, "depth.onnx")

# # img_label = "trash"
# # img = Image.open(f"input/{img_label}.jpg")
# # img = img.resize((640, 480))
# # img = np.asarray(img) / 255.
# # print(len(img[0][1]))
# # opt.device = torch.device('cuda:0')
# dummy_input = Variable(torch.randn(640, 640, 1))
# # dummy_input = Variable(img)
# model = torch.load('./detection_weights.pt')
# # dummy_output = model(dummy_input)
# torch.onnx.export(model, dummy_input, "yolo.onnx")