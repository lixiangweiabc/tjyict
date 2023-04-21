import os.path
from PIL import Image
import sys
import torchvision.transforms as transforms

# 图片的切块
def cut_image(image, patch_num):
    width, height = image.size
    item_width = int(width / patch_num)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0 ,patch_num)  :  # 两重循环，生成n张图片基于原图的位置
        for j in range(0 ,patch_num):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = ( j *item_width , i *item_width ,( j +1 ) *item_width ,( i +1 ) *item_width)
            box_list.append(box)
    print(box_list)
    image_list = [image.crop(box) for box in box_list]  #Image.crop(left, up, right, below)
    return image_list


# 保存
def save_images(image_list, save_path):
    index = 1
    for image in image_list:
        image.save(os.path.join(save_path, str(index) + '.png'))
        index += 1

# 图片的有间隙拼接
def image_compose(IMAGE_SIZE, IMAGE_ROW, IMAGE_COLUMN, padding, IMAGES_PATH, IMAGE_SAVE_PATH):
    IMAGES_FORMAT = ['.bmp', '.jpg', '.tif', '.png']  # 图片格式
    # 获取图片集地址下的所有图片名称
    image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
                   os.path.splitext(name)[1] == item]

    # 排序，这里需要根据自己的图片名称切割，得到数字
    image_names.sort(key=lambda x: int(x.split(("."), 2)[0]))

    # 简单的对于参数的设定和实际图片集的大小进行数量判断
    if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
        raise ValueError("合成图片的参数和要求的数量不能匹配！")

    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE + padding * (IMAGE_COLUMN-1), IMAGE_ROW * IMAGE_SIZE + padding * (IMAGE_ROW-1)), 'white')  # 创建一个新图,颜色为白色
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, (
            (x - 1) * IMAGE_SIZE + padding * (x - 1),  (y - 1) * IMAGE_SIZE + padding * (y - 1)))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


if __name__ == '__main__':
    padding=5
    IMAGE_SIZE = 256  # 每张小图片的大小
    IMAGE_ROW = 2  # 图片间隔，也就是合并成一张图后，一共有几行
    IMAGE_COLUMN = 2  # 图片间隔，也就是合并成一张图后，一共有几列
    IMAGES_PATH = r'/data/jytang/bysy_paired/CT_test_patch_restormer/CT_test_patch/'  # 图片集地址
    IMAGE_SAVE_PATH = r'/data/jytang/bysy_paired/CT_test_patch_compose_restormer/generate.png'  # 图片转换后的地址
    image_compose(IMAGE_SIZE, IMAGE_ROW, IMAGE_COLUMN, padding, IMAGES_PATH, IMAGE_SAVE_PATH) # 调用函数

# if __name__ == '__main__':
#     file_path = r'/data/jytang/bysy_paired/CT_test/220812981_023.png'
#     save_path = r'/data/jytang/bysy_paired/CT_test_patch/'
#     image = Image.open(file_path)
#     # image.show()
#     # transform = transforms.Resize(224)
#     # image = transform(image)
#     image_list = cut_image(image, patch_num=2)
#     save_images(image_list,save_path)
