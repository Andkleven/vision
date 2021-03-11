# EASY WAY
import sys

# insert at 1, 0 is the script path (or '' in REPL)

sys.path.insert(1, "./AdaBins")
from infer import InferenceHelper

sys.path.pop()

from PIL import Image
from time import time
import matplotlib.pyplot as plt


# Load and preprocess image
sys.path.insert(1, "./AdaBins")
img_label = "trash"
img = Image.open(f"input/{img_label}.jpg")
img = img.resize((640, 480))
# img.save(f"input/{img_label}-processed.jpg")
# img = Image.open(f"input/{img_label}-processed.jpg")
# sys.path.pop()

# Infer
infer_helper = InferenceHelper()

start = time()

centers, pred = infer_helper.predict_pil(img)

stop = time()
print(f"took: {stop - start}s")

plt.imshow(pred.squeeze(), cmap="magma_r")
plt.show()


# # NYU
# model = UnetAdaptiveBins.build(n_bins=N_BINS, min_val=MIN_DEPTH, max_val=MAX_DEPTH_NYU)
# pretrained_path = "./pretrained/AdaBins_nyu.pt"
# model, _, _ = model_io.load_checkpoint(pretrained_path, model)

# bin_edges, predicted_depth = model(example_rgb_batch)
