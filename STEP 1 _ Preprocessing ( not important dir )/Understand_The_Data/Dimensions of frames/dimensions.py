import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
#-------------------------------------------------------------
# first : Load the paths of each video using os module
#-------------------------------------------------------------
path_shop = "D:/DEEP Leaning dataset/shop videos/Shop DataSet/shop lifters"
path_nonshop = "D:/DEEP Leaning dataset/shop videos/Shop DataSet/non shop lifters"
videos_paths_shop =  []
videos_paths_nonshop = []
for i in os.listdir(path_shop) :
    videos_paths_shop.append(i)
for j in os.listdir(path_nonshop) :
    videos_paths_nonshop.append(j)
#--------------------------------------------------------------
# Get Dimensions of each video frames
#--------------------------------------------------------------
shop_width , nonshop_width = [] , []
shop_height , nonshop_height = [] , []
for i in range(len(videos_paths_shop)) :
    path_of_video = os.path.join(path_shop,videos_paths_shop[i])
    video = cv2.VideoCapture(path_of_video)
    shop_height.append(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    shop_width.append(video.get(cv2.CAP_PROP_FRAME_WIDTH))
for i in range(len(videos_paths_nonshop)) :
    path_of_video = os.path.join(path_nonshop,videos_paths_nonshop[i])
    video = cv2.VideoCapture(path_of_video)
    nonshop_height.append(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    nonshop_width.append(video.get(cv2.CAP_PROP_FRAME_WIDTH))

print(f"The shape of shop videos is, width = {np.unique(np.array(shop_width))} and height = {np.unique(np.array(shop_height))}")
print(f"The shape of non-shop videos is, width = {np.unique(np.array(nonshop_width))} and height = {np.unique(np.array(nonshop_height))}")