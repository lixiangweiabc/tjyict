import SimpleITK as sitk
import glob
import shutil
import os

# source_path = glob.glob('/home/jytang/Restormer-main/Deraining/t1_2_t2_192_result/t1_val/*.png')
# for file in source_path:
#     num = file.split('_')[-1]
#     id = file.replace('_1_'+num,'').split('/')[-1] + '_1'
#     # print(num)
#     # print(id)
#     new_dir = '/home/jytang/Restormer-main/Deraining/t1_2_t2_192_result/'+ id +'/'
#     if not os.path.exists(new_dir):
#         os.makedirs(new_dir)
#     shutil.copy(file,new_dir)

# save_path = './BraTS19_2013_15_1_0_old'
source_paths = glob.glob('/home/jytang/Restormer-main/Deraining/t1_2_t2_192_result/BraTS19*')
save_path = '/data/jytang/MICCAI_BraTS_2019_Data_Training/generate_t2_val/'
for source_path in source_paths:
    print(source_path)
    file_list = os.listdir(source_path)
    file_list.sort()
    file_names = [os.path.join(source_path,f) for f in file_list]
    # print(file_names)
    newspacing = [1, 1, 1]  # 设置x，y, z方向的空间间隔
    reader = sitk.ImageSeriesReader()
    reader.SetFileNames(file_names)
    vol = reader.Execute()
    vol.SetSpacing(newspacing)
    save_dir = save_path + source_path.split('/')[-1] + '/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir) 
    final_save_dir = save_dir +source_path.split('/')[-1] +'_t2.nii.gz'
    sitk.WriteImage(vol, final_save_dir) # 保存为volume.nii.gz也可
