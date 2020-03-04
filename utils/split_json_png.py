"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

import os
import shutil
import multiprocessing


def read_data_path(data_path, hidename):
    outputpath = []
    outputname = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ("." + hidename):
                path = [dirpath, filename]
                outputpath.append(dirpath)
                outputname.append(filename)
    return outputpath, outputname


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile, dstfile)
        print("move %s -> %s" % (srcfile, dstfile))


def move_json_png(fn):
    # path1 = read_data_path()
    path = "F:/BRD_data/Segmentation_BRD/初步打标数据/png"
    i = fn[0]
    j = fn[1]
    mymovefile(os.path.join(i, j), os.path.join(path, j))
    return 1


def main(filepath):
    a, b = read_data_path(filepath, "png")
    testFL = []
    for i, j in zip(a, b):
        testFL.append([i, j])
    pool = multiprocessing.Pool(processes=6)
    total = pool.map(move_json_png, testFL)
    pool.close()
    pool.join()
    print(len(total))


if __name__=="__main__":
    path = "F:/BRD_data/Segmentation_BRD/初步打标数据"
    main(path)