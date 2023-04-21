import os
from PIL import Image

source_imgs_dir='/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/t2_test_96/'
target_imgs_dir='/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/t2_test_resize_192/'
for file in os.listdir(source_imgs_dir):
    im = Image.open(source_imgs_dir + file)
    out = im.resize((192, 192), Image.ANTIALIAS)
    out.save(target_imgs_dir + file)
