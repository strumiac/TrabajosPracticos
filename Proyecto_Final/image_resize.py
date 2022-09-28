import os
import shutil
from pathlib import Path
from tqdm import tqdm
from collections import defaultdict

import numpy as np
import pandas as pd

from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt


DATA_DIR = "/home/carlos/Escritorio/dataset"
DATA_DIR_OUT = "/home/carlos/Escritorio/png_resize"

# check images size
img_size = defaultdict(int)

for fPath in tqdm(Path(DATA_DIR).iterdir(), total = len(os.listdir(DATA_DIR))):
    img = Image.open(fPath)
    img_size[img.size] += 1
  
print("\n\nTamaño de las imágenes :", img_size)


# cambio tamano
img_h = 608
img_w = 608

for i in os.listdir(DATA_DIR):
  img = cv.imread(os.path.join(DATA_DIR + '/' + i))
  height, width, channel = img.shape
  img_resized = cv.resize(img, (img_w, img_h), interpolation = cv.INTER_CUBIC)
  cv.imwrite(os.path.join(DATA_DIR_OUT, i.rsplit('.', 1)[0]+'.png'), img_resized)