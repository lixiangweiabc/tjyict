import glob
source_file = glob.glob('/home/jytang/MICCAI_BraTS_2019_Data_Training/test/*/*seg.nii.gz')
print(len(source_file))
for file in source_file:
    id = file.split('/')[-2]
    with open("/data/jytang/BraTS-convert/test.txt","a") as f:
        f.write(id + '\r\n')