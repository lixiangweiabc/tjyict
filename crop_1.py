import time, os
import nibabel as nib
import numpy as np
import glob

def cut_newdata(img_t1_name,img_t1_name1):
    img_t1 = nib.load(img_t1_name)
    
    img_t1_affine = img_t1.affine
    # print(img_t1_affine)
    img_t1_data = img_t1.get_fdata()
    print(img_t1_data.shape)
    img_t1_data1 = img_t1_data[0:img_t1_data.shape[0],0:img_t1_data.shape[1],17:48]
    # img_t1_data1 = np.zeros((img_t1_data.shape[0],img_t1_data.shape[1],35))
    # for i in range(0,34):
    #     img_t1_data1[0:img_t1_data.shape[0],0:img_t1_data.shape[1],i] = img_t1_data[0:img_t1_data.shape[0],0:img_t1_data.shape[1],35-i-1]
    img_t1 = nib.Nifti1Image(img_t1_data1, img_t1_affine)
    nib.save(img_t1, img_t1_name1)
def padding_data(img_t1_name,img_t1_name1):
    img_t1 = nib.load(img_t1_name)
    img_t1_affine = img_t1.get_affine()
    img_t1_data = img_t1.get_data()
    img_t1_data = np.squeeze(img_t1_data)
    empty_data = np.zeros([145,174,145])
    empty_data[10:138,10:170,10:138] = img_t1_data
    img_t1 = nib.Nifti1Image(empty_data, img_t1_affine)
    nib.save(img_t1, img_t1_name1)
if __name__ == '__main__':
    input = '/data/jytang/bysy_all_nii/220812992/220812992_CT.nii.gz'
    output = '/data/jytang/bysy_all_nii/220812992/220812992_CT_crop.nii.gz'
    cut_newdata(input,output)
    # paths = glob.glob('/home/jytang/MICCAI_BraTS_2019_Data_Training/*/*/*seg.nii.gz') 
    # for path in paths:
    #     print(path)
    #     # data_path = path + data
    #     cut_newdata(path,path)
    #     # cut_newdata(data_path, data_path)