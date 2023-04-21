import nibabel as nib
import numpy as np
import torch
import torch.nn.functional as F

path = '/data/jytang/CT2MR_sample/200908517/200908517_CT.nii.gz'
img1 = nib.load(path)

data = img1.get_fdata()
origin_affine = img1.affine
# registration_affine = np.array(

# [[0.999918641269080, -8.219958611000000e-04, -0.012729303414000, -12.821358931309000],

# [0.001031114339960, 0.999864482214520, 0.016430277207150, 97.498224370448800],

# [0.012714072747110, -0.016442065827900, 0.999783982080880, 2.314898423000110],

# [0, 0, 0, 1]])

registration_affine = np.array(

[[0.999878332099870, -0.008739817944000, 0.012920393937080, -15.825540020137000],

[0.007855932991050, 0.997725697920340, 0.066945619918060, 63.872057676595300],

[-0.013476101588500, -0.066835973036100, 0.997672966153890, -4.146318687523100e+02],

[0, 0, 0, 1]])
# print(data)
# print(data.shape)
print(origin_affine)
print(type(origin_affine))
print(origin_affine.shape)
# nib.save(img1, '/data/jytang/200908517_CT.nii.gz')
# new_affine = registration_affine.dot(origin_affine)
# new_affine2 = origin_affine.dot(registration_affine)
# print(new_affine)
# print(type(new_affine))
# print(new_affine.shape)
# print(new_affine2)
# print(type(new_affine2))
# print(new_affine2.shape)
# new_image_1 = nib.Nifti1Image(data, origin_affine)
# nib.save(new_image_1, '/data/jytang/220211609_CT_affine1.nii.gz')
# new_image_2 = nib.Nifti1Image(data, registration_affine)
# nib.save(new_image_2, '/data/jytang/220211609_CT_affine2.nii.gz')
# new_image_3 = nib.Nifti1Image(data, new_affine)
# nib.save(new_image_3, '/data/jytang/220211609_CT_affine3.nii.gz')
# new_image_3 = nib.Nifti1Image(data, new_affine2)
# nib.save(new_image_3, '/data/jytang/220211609_CT_affine4.nii.gz')

# data = np.asarray( nib.load(path).get_fdata() )
# print(data.shape)
# print(type(data))
# data_dhw = np.transpose(data,(1,2,0))
# print(data_dhw.shape)
# print(type(data_dhw))
# data_tensor = torch.tensor(data_dhw)
# print(data_tensor.shape)
# print(type(data_tensor))
# img = torch.randn(1, 1, 160, 192, 160) #[batch_size, channel, D, H, W]
# print(img.shape)
# print(type(img))