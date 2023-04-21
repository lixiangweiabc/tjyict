# -*- coding: utf-8 -*- 
#! python3 
import cv2
import numpy as np
import glob 
import os
#原图
t1_paths = glob.glob('/data/jytang/bysy_paired/CT_test_patch/*.png')
for t1_path in t1_paths:
    img1 = cv2.imread(t1_path)
    # label = t1_path.split('/')[-4]
    id = t1_path.split('/')[-1]
    t2_path = t1_path.replace("CT","MR")
    # id = id.replace("t1","")
    img2 = cv2.imread(t2_path)
    image = np.concatenate([img1, img2], axis=1)
    output = '/data/jytang/bysy_paired_pix2pix/patch/test/' +  id
    cv2.imwrite(output,image)
# conut = 0
# src_paths = glob.glob('/data/jytang/bysy_paired/CT_train/*.png')
# seg_paths = glob.glob('/data/jytang/bysy_paired/MR_val/*.png')

# n = 0
# for i in range(len(src_paths)):
#     print(src_paths[i].split('/')[-1])
#     for j in range(len(seg_paths)):
#         if src_paths[i].split('/')[-1] == seg_paths[j].split('/')[-1]:
#             print(seg_paths[j].split('/')[-1])
#             n = n + 1
# print(len(src_paths))
# print(len(seg_paths))