from hashlib import new
import numpy as np
import SimpleITK as sitk
import glob 
import os

# 对医疗图像进行重采样，仅仅需要将out_spacing替换成自己想要的输出即可
def resample_image(itk_image, out_spacing=[1.25, 1.25, 1.21]):
    original_spacing = itk_image.GetSpacing()
    original_size = itk_image.GetSize()
 
    # 根据输出out_spacing设置新的size
    out_size = [
        int(np.round(original_size[0] * original_spacing[0] / out_spacing[0])),
        int(np.round(original_size[1] * original_spacing[1] / out_spacing[1])),
        int(np.round(original_size[2] * original_spacing[2] / out_spacing[2]))
    ]
 
    resample = sitk.ResampleImageFilter()
    resample.SetOutputSpacing(out_spacing)
    resample.SetSize(out_size)
    resample.SetOutputDirection(itk_image.GetDirection())
    resample.SetOutputOrigin(itk_image.GetOrigin())
    resample.SetTransform(sitk.Transform())
    resample.SetDefaultPixelValue(itk_image.GetPixelIDValue())
 
    resample.SetInterpolator(sitk.sitkBSpline)
 
    return resample.Execute(itk_image)

def centerCrop(image, output_size):
    if image.shape[0] <= output_size[0] or image.shape[1] <= output_size[1] or image.shape[2] <= output_size[2]:
        pw = max((output_size[0] - image.shape[0]) // 2 + 3, 0)
        ph = max((output_size[1] - image.shape[1]) // 2 + 3, 0)
        pd = max((output_size[2] - image.shape[2]) // 2 + 3, 0)
        image = np.pad(image, [(pw, pw), (ph, ph), (pd, pd)], mode='constant', constant_values=0)
        
    (w, h, d) = image.shape
 
    w1 = int(round((w - output_size[0]) / 2.))
    h1 = int(round((h - output_size[1]) / 2.))
    d1 = int(round((d - output_size[2]) / 2.))
 
    # print(image.shape, output_size, get_center(label), w1, h1, d1)
    image = image[w1:w1 + output_size[0], h1:h1 + output_size[1], d1:d1 + output_size[2]]
    
    return image

gz_paths = glob.glob('/home/jytang/data/try/test/*.nii.gz') 
for gz_path in gz_paths:
    first_path=gz_path.split('/')[-2]
    second_path=gz_path.split('/')[-1]
    print('正在重采样文件名为：',second_path)
    Original_img = sitk.ReadImage(gz_path)
    print('原始图像的Spacing：', Original_img.GetSpacing())
    print('原始图像的Size：', Original_img.GetSize())
    Resample_img = resample_image(Original_img)
    print('经过resample之后图像的Spacing是：', Resample_img.GetSpacing())
    print('经过resample之后图像的Size是：', Resample_img.GetSize())
    new_path='/home/jytang/data/train_resample/LGG/'+first_path
    if os.path.exists(new_path) == False:
        os.makedirs(new_path, exist_ok=True)
    sitk.WriteImage(Resample_img,new_path+'/'+second_path)
# gz_path = 'BraTS19_TMC_30014_1_t1.nii.gz'
# print('测试文件名为：', gz_path)
 
# # 使用sitk读取对应的数据
# Original_img = sitk.ReadImage(gz_path)
# print('原始图像的Spacing：', Original_img.GetSpacing())
# print('原始图像的Size：', Original_img.GetSize())
 
# # 对数据进行重采样
# Resample_img = resample_image(Original_img)
# print('经过resample之后图像的Spacing是：', Resample_img.GetSpacing())
# print('经过resample之后图像的Size是：', Resample_img.GetSize())
# sitk.WriteImage(Resample_img,'/home/jytang/data/try/resample/'+gz_path)