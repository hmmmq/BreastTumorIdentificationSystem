#把要转换格式的tif原始图片放到脚本文件同级的src目录下面，
#执行完这个Python脚本后，生成的图片会放在result文件里面。
#没有这两个文件夹的话，可以手动创建。
import os
import glob
from PIL import Image

current_dir = os.getcwd()
files = glob.glob(current_dir + "/JPEGImages/*.PNG")


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
    else:
        print(path + ' 目录已存在')

mkdir(current_dir + 'JPEGImages')
mkdir(current_dir + '/result')

def image_convert(image_file):
    image_name = image_file[:-4] + '.jpeg'
    with Image.open(image_file) as f:
        rgb_im = f.convert('RGB')
        #这是分辨率96的
        rgb_im.save(image_name.replace('src', 'result', 1), quality=95, subsampling=0)
        #当要设置分辨率就替换里面的这是300分辨率的
        #rgb_im.save(image_name.replace('src', 'result', 1), dpi=(300.0,300.0))


for file in files:
    image_convert(file)