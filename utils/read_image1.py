"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""
import numpy as np
from cv2 import cv2  #



def access_pixels(img):
    """遍历图像每个像素的每个通道"""
    height = img.shape[0]  # 将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]
    for row in range(height):  # 遍历每一行
        for col in range(width):  # 遍历每一列
            for channel in range(channels):  # 遍历每个通道（二值化后只有一个通道）
                val = img[row][col][channel]
                if val == 128 or val == 0:
                    pass
                else:
                    print(val)
    # print(val)


if __name__=="__main__":
    filename = "F:/BRD_data/segmentation/data_6/labels/安徽区域一部-宿松碧桂园-洋房-10#-终稿-0_json_label.png"
    img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
    access_pixels(img)