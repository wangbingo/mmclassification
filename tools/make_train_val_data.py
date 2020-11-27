import os
import shutil
from tqdm import tqdm

ROOT = r'/home/admin'
SRC_PATH = r'cassava-leaf-disease-classification-cut/train_images/'
DST_PATH = r'mmclassification/data/imagenet/train/'

os.mkdir(os.path.join(ROOT, DST_PATH))
for i in range(5):
    os.mkdir(os.path.join(ROOT, DST_PATH, 'n' + str(i)))

import pandas as pd
csv_file = open(os.path.join(ROOT, 'train.csv'))
df = pd.read_csv(csv_file, engine='python')

for i in tqdm(range(len(df))):
    file_name = df["image_id"][i]
    label = df["label"][i]
    shutil.copy(os.path.join(ROOT, SRC_PATH, file_name), 
                os.path.join(ROOT, DST_PATH, 'n' + str(label)))


