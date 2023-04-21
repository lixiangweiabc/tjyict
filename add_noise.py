import os
import numpy as np
import cv2
import glob
t2_paths = glob.glob('/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/t2_test/*.png')
output = '/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/try.png'
for path in t2_paths:
    image = cv2.imread(path) # 读取图像 path为存储图像路径，img_name为图像文件名
# 添加噪声
    output = path.replace('t2_test','t2_test_noise')
    noise_type = np.random.poisson(lam=50,size=(192,192,1)).astype(dtype='uint8') # lam>=0 值越小，噪声频率就越少，size为图像尺寸
    noise_image = noise_type+image  # 将原图与噪声叠加
    cv2.imwrite(output,noise_image)
# # cv2.imshow('添加噪声后的图像',noise_image)
# # cv2.waitKey(0)
# # cv2.destroyWindow()
# import numpy as np
# import cv2
# def gauss_noise(img, mean, var):
#     '''
#     添加高斯噪声
#     :param img: 原始图像
#     :param mean: 均值
#     :param var: 方差,越大，噪声越大
#     :return: resultImg
#     '''
#     image = np.array(img / 255, dtype=float)  # 将原始图像的像素值进行归一化，除以255使得像素值在0-1之间
#     noise = np.random.normal(mean, var ** 0.5, image.shape)  # 创建一个均值为mean，方差为var呈高斯分布的图像矩阵
#     out = image + noise  # 将噪声和原始图像进行相加得到加噪后的图像
#     if out.min() < 0:
#         low_clip = -1.
#     else:
#         low_clip = 0.
#     resultImg = np.clip(out, low_clip, 1.0)  # clip函数将元素的大小限制在了low_clip和1之间了，小于的用low_clip代替，大于1的用1代替
#     resultImg = np.uint8(resultImg * 255)  # 解除归一化，乘以255将加噪后的图像的像素值恢复
#     return resultImg
 
# if __name__ == '__main__':
#     img = cv2.imread('/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/t2_val/BraTS19_2013_14_1_70.png')
#     noise_image = gauss_noise(img, 0, 0.0005)
#     output = '/home/jytang/Restormer-main/Deraining/Datasets/t12t2_192/try.png'
#     cv2.imwrite(output,noise_image)
#     # cv2.imshow('origin', img)
#     # cv2.imshow('result', noise_image)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
