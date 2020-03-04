"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter



import cv2
import matplotlib.pyplot as plt
import numpy as np


filename="F:/BRD_data/segmentation/data_6/labels/安徽区域一部-宿松碧桂园-洋房-10#-终稿-0_json_label.png"
img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
# img=cv2.imread(filename)
fig,ax=plt.subplots(1,2,figsize=(12,5))
colors=['blue','green','red']


for i in range(3):
    hist,x=np.histogram(img[:,:,i].ravel(),bins=256,range=(0,256))
    ax[0].plot(0.5*(x[:-1]+x[1:]),hist,label=colors[i],color=colors[i])


ax[0].legend(loc='upper left')
ax[0].set_xlim(0,256)
hist2,x2,y2=np.histogram2d(
    img[:,:,0].ravel(),img[:,:,2].ravel(),
    bins=(100,100),range=[(0,256),(0,256)])
ax[1].imshow(hist2,extent=(0,256,0,256),origin='lower',cmap='gray')
ax[1].set_ylabel('blue')
ax[1].set_xlabel('red')
plt.show()
# image = cv2.imread("E:/Smart_Image_Project/Image_segmetation/Keras-Semantic-Segmentation-master/data/train_label/0.png")
# image = cv2.imread("C:/Users/dell/Desktop/dataset1/annotations_prepped_train/0001TP_006690.png")
# image = cv2.imread("F:/BRD_data/segmentation/data_6/labels/安徽区域一部-宿松碧桂园-洋房-10#-终稿-0_json_label.png")
# image = cv2.imdecode(np.fromfile("F:/BRD_data/segmentation/data_6/labels/安徽区域一部-宿松碧桂园-洋房-10#-终稿-0_json_label.png", dtype=np.uint8), -1)
# image = np.asarray(image)
print(img.sum())
print(type(img))

print(np.min(img))
print(np.max(img))
# cv2.imshow("img",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.imshow(image * 255)
if np.min(img) or np.max(img):
    print("yes")

