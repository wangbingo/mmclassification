import os
import shutil

path = r'/Users/wangbing/Downloads/tiny-imagenet-100-A-m/train'

for nxxx in os.listdir(path):
    nxxx_dir = os.path.join(path, nxxx)
    nxxx_images_dir = os.path.join(path, nxxx, 'images')

    print('proceed folder:', nxxx_dir)
    for pic in os.listdir(nxxx_images_dir):
        pic_path = os.path.join(nxxx_images_dir, pic)
        shutil.move(pic_path,nxxx_dir)

    os.removedirs(nxxx_images_dir)

