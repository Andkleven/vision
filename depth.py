# # EASY WAY
import sys

# insert at 1, 0 is the script path (or '' in REPL)

sys.path.insert(1, "./AdaBins")
from infer import InferenceHelper

sys.path.pop()

from PIL import Image
from time import time
import matplotlib.pyplot as plt
import numpy

# Load and preprocess image
sys.path.insert(1, "./AdaBins")
img_label = "trash"
img = Image.open(f"input/{img_label}.jpg")
img = img.resize((640, 480))
# img.save(f"input/{img_label}-processed.jpg")
# img = Image.open(f"input/{img_label}-processed.jpg")
# sys.path.pop()

# Infer
infer_helper = InferenceHelper(device='cpu')

start = time()

centers, pred = infer_helper.predict_pil(img)

stop = time()
print(f"took: {stop - start}s")
print(pred.squeeze())
plt.imshow(pred.squeeze(), cmap="magma_r")
plt.show()
result = Image.fromarray(pred.squeeze().astype(numpy.uint8))
result.save("output/depth.jpg")


# sys.path.insert(1, "./AdaBins")
# from models import UnetAdaptiveBins
# import model_io
# from PIL import Image

# MIN_DEPTH = 1e-3
# MAX_DEPTH_NYU = 10
# MAX_DEPTH_KITTI = 80

# N_BINS = 256 
# # # NYU
# model = UnetAdaptiveBins.build(n_bins=N_BINS, min_val=MIN_DEPTH, max_val=MAX_DEPTH_NYU)
# pretrained_path = "./pretrained/AdaBins_nyu.pt"
# pretrained_path = "./input/trash.jpg"
# model, _, _ = model_io.load_checkpoint(pretrained_path, model)

# bin_edges, predicted_depth = model()
# print(bin_edges, predicted_depth)