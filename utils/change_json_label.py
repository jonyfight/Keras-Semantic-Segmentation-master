"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""


import json
import os,sys
import csv
import pandas as pd


# 读取json文件，存放到output_json列表里面
def read_json(data_path, hidename):
    output_json = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ("." + hidename):
                output_json.append(filename)
    return output_json


# 处理单个json文件的label
def single_labels(filename):
    labels = []
    with open(os.path.join(path, filename),'r') as load_f:
        file = json.load(load_f)
        shapes = file["shapes"]
        for shape in shapes:
            class_name = shape['label']
            if class_name == "卫生间" or class_name == "卫":
                shape['label'] = "卫生间"
            label = shape["label"]
            labels.append(label)
    load_f.close()
    with open(os.path.join(path, filename), "w") as load_f:
        json.dump(file, load_f)
    load_f.close()
    return load_f


# 批量处理json文件
def main(filepath):
    files = read_json(filepath, "json")
    for file in files:
        single_labels(file)
    return 1


# def rewrite_json_file(filepath, file):
#     with open(filepath, "w") as f:
#         json.dump(file, f)
#     f.close()


if __name__=="__main__":
    path = r"F:\BRD_data\Segmentation_BRD\origin\json4"
    # path1 = "F:/BRD_data/Segmentation_BRD/origin/json4/安徽区域二部-亳州江山赋-合同-洋房-33#.json"
    # single_labels(path1)
    main(path)