from doctest import OutputChecker
import glob
import shutil
import os 
val_paths = glob.glob('/home/jytang/MICCAI_BraTS_2019_Data_Training/test/*')
source = '/data/jytang/MICCAI_BraTS_2019_Data_Training/'
outputfile = '/data/jytang/MICCAI_BraTS_2019_Data_Training/test/'
for val in val_paths:
    print(val)
    val = val.split('/')[-1]
    src = source + '/HGG/' + val
    
    if not os.path.exists(src):
        src = source + '/LGG/'+ val
        
    if not os.path.exists(src):
        print('wrong')
    else:
        print(src)
        print(outputfile)
    shutil.move(src, outputfile)
# import glob
# import shutil
# import os
# source_path = glob.glob('/home/jytang/MICCAI_BraTS_2019_Data_Training/test/*/*t1.nii.gz')
# print('1111111111')
# for file in source_path:
#     id = file.split('/')[-2]
#     print(file) 
#     new_dir = '/data/jytang/MICCAI_BraTS_2019_Data_Training/generate_t2_test/'+ id +'/'
#     shutil.copy(file,new_dir)