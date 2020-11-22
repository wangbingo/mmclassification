import os

path = r'/Users/wangbing/Downloads/tiny-imagenet-100-A-m/train'

for i in os.listdir(path):
    xxx_boxes_txt_name = '{0}_boxes.txt'.format(i)
    xxx_boxes_txt_path = os.path.join(path, i, xxx_boxes_txt_name)
    os.remove(xxx_boxes_txt_path)
    print('deleting', i)
