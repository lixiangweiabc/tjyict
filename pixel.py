from PIL import Image
import numpy as np
import glob
import os

img_paths = glob.glob('/data/jytang/BraTS_seg/SegmentationClass/*.png')
img_save = '/data/jytang/BraTS_seg/SegmentationClass-onelabel/'
# if not os.path.exists(img_save):
#     os.makedirs(img_save)
# f = open("/data/jytang/BraTS_seg/ImageSets/Segmentation/test500.txt") 
# lines = f.readlines()
# for line in lines:
#     print(line)
num = 0
for img_path in img_paths:
    image_id = img_path.split('/')[-1]
    print(image_id)
    output = img_save + image_id
    img = Image.open(img_path)
    #img.show()
    img_array = np.array(img)#把图像转成数组格式img = np.asarray(image)
    shape = img_array.shape
    print(img_array.shape)
    for i in range(0,shape[0]):
        for j in range(0,shape[1]):
            value = img_array[i, j]
            # print("",value)
            if value == 64:
                img_array[i, j] =1
            if value == 127:
                img_array[i, j] =1
            if value == 255:
                img_array[i, j] =1
    img2 = Image.fromarray(np.uint8(img_array))     
    # img2.show(img2)
    img2.save(output,"png") 
    print('processiong picture{} to {}'.format(img_path,output))