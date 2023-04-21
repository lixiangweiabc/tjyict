import scipy, numpy, shutil, os, nibabel
import sys, getopt
import imageio
import glob

def niito2D(filepath):
    paths = glob.glob(filepath) 
    # inputfiles = os.listdir(filepath)  #遍历文件夹数据
    outputfile = '/data/jytang/bysy_paired/MR_test/'       #输出文件夹
    # print('Input file is ', inputfiles)
    # print('Output folder is ', outputfile)
 
    for path in paths:
        image_array = nibabel.load(path).get_fdata() #数据读取
        print(image_array.shape[2])
        # case_name = path.split('/')[-2]
        # outputfile = '/home/jytang/data/train_cut/'+path.split('/')[-3]+'/'+path.split('/')[-2]+'/t1'
        # set destination folder
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)   #不存在输出文件夹则新建
            print("Created ouput directory: " + outputfile)
        print('Reading NIfTI file...')

        # total_slices = 120
        total_slices = image_array.shape[2]  #总切片数
        slice_counter = 0 #从第几个切片开始
 
        # iterate through slices
        for current_slice in range(0, total_slices-2):
            # alternate slices
            if (slice_counter % 1) == 0:
                data = image_array[ :, :,current_slice]  #保存该切片，可以选择不同方向。
 
                # alternate slices and save as png
                if (slice_counter % 1) == 0:
                    print('Saving image...')
                    #切片命名
                    image_name = path[:-7] +"{:0>3}".format(str(current_slice)) + ".png"
                    # image_name = path[:-7] + str(current_slice) + ".png"
                    # image_name = case_name +"_"+ "{:0>3}".format(str(current_slice)) + ".png"
                    image_name = image_name.replace('MR','')
                    # txt_name = image_name.split('/')[-1]
                    # txt_name = txt_name.replace('.png','')
                    # with open("/data/jytang/BraTS_seg/ImageSets/Segmentation/test.txt","a") as f:
                    #     f.write(txt_name + "\n")
                    # with open("/data/jytang/BraTS_seg/ImageSets/Segmentation/trainval.txt","a") as f:
                    #     f.write(txt_name + "\n")
                    #保存
                    imageio.imwrite(image_name, data)
                    print('Saved.')
 
                    # move images to folder
                    print('Moving image...')
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1
                    print('Moved.')
 
    print('Finished converting images')
 
if __name__ == '__main__':
    niito2D('/data/jytang/bysy_all_nii/220512289/220512289_MR.nii.gz')