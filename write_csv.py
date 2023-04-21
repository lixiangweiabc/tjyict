import csv
import glob

# with open("/data/jytang/bysy_data_information.csv","w", encoding='UTF8', newline='') as csvfile: 
#     writer = csv.writer(csvfile)
#     writer.writerow(['id'])
# f = open("/data/jytang/bysy_data_information.csv", 'a',newline='')
# writer = csv.writer(f)
# writer.writerow(["id"])

paths = glob.glob('/data/jytang/bysy_all_nii/*') 
for path in paths:
    id = path.split('/')[-1]
    print(type(id))
    # with open("/data/jytang/bysy_data_information.csv","w", encoding='UTF8', newline='') as csvfile: 
    # writer = csv.writer(csvfile)
    # writer.writerow(['id'])
    # f = open("/data/jytang/bysy_data_information.csv", 'a',newline='')
    # writer = csv.writer(f)
    # writer.writerow([id])
    # f.close()