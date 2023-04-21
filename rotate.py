import os
from PIL import Image
import glob
img_paths = glob.glob('/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/*/*.png')
for img_path in img_paths:
    img = Image.open(img_path)
    img = img.transpose(Image.ROTATE_270)
    img.save(img_path)
# img = Image.open('img/1.jpg')
# img = img.transpose(Image.ROTATE_90)  # 将图片旋转90度
# #img = img.transpose(Image.ROTATE_180)  # 将图片旋转180度
# #img = img.transpose(Image.ROTATE_270)  # 将图片旋转270度
# img.show("img/rotateImg.png")
# #img.save("img/rotateImg.png")
