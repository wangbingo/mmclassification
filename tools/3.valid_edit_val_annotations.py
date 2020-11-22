import os

if __name__ == '__main__':
    train_dir = r'/Users/wangbing/Downloads/tiny-imagenet-100-A-m/train'
    valid_txt_path = r'/Users/wangbing/Downloads/tiny-imagenet-100-A-m/val/val_annotations.txt'
    output_valid_txt_path = r'/Users/wangbing/Downloads/tiny-imagenet-100-A-m/val/val_annotations_new.txt'

    list_nxxx_under_train = []
    for i in os.listdir(train_dir):
        list_nxxx_under_train.append(i)

    list_nxxx_under_train=[i for i in list_nxxx_under_train if 'n' in i]
    list_nxxx_under_train=sorted(list_nxxx_under_train, key=lambda i:int(i.replace('n','')))
    print('list_nxxx_under_train:\n',list_nxxx_under_train)

    dict_nxxxx_vs_number = {}
    for i in range(len(list_nxxx_under_train)):
        nxxx = list_nxxx_under_train[i]
        dict_nxxxx_vs_number[nxxx] = i + 1

    print(dict_nxxxx_vs_number)

    list_valid = []
    with open(valid_txt_path, 'r') as f:
        for line in f.readlines():
            # import pprint
            # pprint.pprint(line)  # 'val_1.JPEG\tn04067472\t52\t55\t57\t59\n'
            image_name,class_name = line.split('\t')[:2]
            line_new = '{0} {1}'.format(image_name, dict_nxxxx_vs_number[class_name])
            list_valid.append(line_new)

    with open(output_valid_txt_path, 'w') as f:
        for i in list_valid:
            f.write(i + '\n')

