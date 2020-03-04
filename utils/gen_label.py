# coding:utf-8
import cv2
import os,sys
import json
import numpy as np

# 读取json文件，存放到output_json列表里面
def read_json(data_path, hidename):
    output_json = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ("." + hidename):
                output_json.append(filename)
    return output_json


# 对单个json文件
def single_json(filename):
    label = [[],[],[],[],[],[]]
    file = os.path.join(path, filename)
    img = cv2.imdecode(np.fromfile(file, np.unit8), 1)
    # img=cv2.imdecode(np.fromfile("安徽区域二部-亳州春暖花开-合同-洋房-7#.png",np.uint8),1)
    mask = np.zeros((img.shape[0],img.shape[1]))
    # with open("安徽区域二部-亳州春暖花开-合同-洋房-7#.json",'r') as load_f:
    with open(file, 'r') as load_f:
         load_dict = json.load(load_f)
         shapes=load_dict['shapes']
         for shape in shapes:
             labe=shape['label']
             ###
             labelvalue = 1
             ###
             points=shape['points']
             points=np.array(points).astype(np.int)
             shape_type=shape['shape_type']
             if shape_type=='rectangle':
                 p1=tuple((points[0]).astype(np.int))
                 p2 = tuple((points[1]).astype(np.int))
                 # cv2.rectangle(img, p1, p2, (0, 255, 0), -1)
                 cv2.rectangle(mask, p1, p2, (labelvalue), -1)
             if shape_type == 'polygon':
                 # cv2.drawContours(canvas, [approx], -1, (0, 0, 255), 2)
                 # cv2.drawContours(img,[points],-1,(0, 0, 255), -1)
                 # labelvalue=255
                 cv2.drawContours(mask, [points], -1, (labelvalue), -1)

         cv2.imencode('.png',img)[1].tofile('结果.png')
         cv2.imencode('.png', mask)[1].tofile('mask.png')
         a=1

         
if __name__=="__main__":
    path = r"F:\BRD_data\Segmentation_BRD\origin\json4"
    single_json(path)