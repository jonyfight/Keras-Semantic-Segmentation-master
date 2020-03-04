
import os
import pandas as pd
#读取文件路径
def read_data_path(data_path,hidename):
    """
    内部功能函数：对文件夹路径下文件的进行搜索，并对其文件格式进行筛选
    :param data_path: 文件夹路径
    :param hidename: 文件筛选格式
    :return: 返回2个列表[filename][filepath]
    """
    #遍历文件夹内所有文件
    output = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            #进行扩展名筛选
            if os.path.splitext(filename)[1] == ('.' + hidename) :
                path = [dirpath ,filename]
                output .append(path )
    return output


def count_data(path):
    data = read_data_path(path,'json')
    a = []
    b = []
    for _ , i in data:
        # id = i.find('#')
        # id = i.find('-')
        # i = i[:id+1]
        i = str(i).split(".")[0]
        a.append(i)
        b.append(1)


    dataframe = pd.DataFrame({'file_name': a, '区域分割': b})
    dataframe.to_csv("test.csv", index=False, sep=',',encoding="utf-8-sig")

if __name__ == '__main__':
    path = r'F:\BRD_data\Segmentation_BRD\origin\json2'
    count_data(path)