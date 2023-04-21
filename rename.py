import os

folder_path = r'/home/jytang/Restormer-main/Deraining/t1_2_t2_test/t1_val/'

if __name__ == '__main__':
    for file in os.listdir(folder_path):
        print(file)
        num = file.split('_')[-1]
        id = file.replace(num,'')
        num = num.replace('.png','')
        num = int(num)
        s = '%03d' % num  # 前面补零占位
        print(id)
        print(s)
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, id + str(s) + '.png'))
        # num += 1
