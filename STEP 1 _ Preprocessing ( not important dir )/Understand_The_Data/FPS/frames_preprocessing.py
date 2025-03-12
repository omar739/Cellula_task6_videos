import cv2
import os
import numpy as np
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
#Get number of frames per second for each video ( FPS )
#--------------------------------------------------------------
FPS_shop = []
FPS_non = []
for i in range(len(videos_paths_shop)) :
    path_of_video = os.path.join(path_shop,videos_paths_shop[i])
    video = cv2.VideoCapture(path_of_video)
    FPS_shop.append(video.get(cv2.CAP_PROP_FPS))
    video.release()
print("Done for video paths shop ")
for i in range(len(videos_paths_nonshop)) :
    path_of_video = os.path.join(path_nonshop,videos_paths_nonshop[i])
    video = cv2.VideoCapture(path_of_video)
    FPS_non.append(video.get(cv2.CAP_PROP_FPS))
    video.release()
print("Done for video paths non shop ")
#----------------------------------------------------------------
# Visualization of FPS
#----------------------------------------------------------------
FPS_shop , FPS_non = np.array(FPS_shop) , np.array(FPS_non)
FPS_shop_unique , FPS_non_unique = np.unique(FPS_shop) , np.unique(FPS_non)
counts_shop , counts_non = [] , []
for i in FPS_shop_unique :
    counts_shop.append(np.count_nonzero(FPS_shop == i))
for i in FPS_non_unique :
    counts_non.append(np.count_nonzero(FPS_non == i))
plt.style.use("dark_background")
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.bar(FPS_shop_unique , counts_shop,color=["skyblue","#19ab98"],
        edgecolor="black",linewidth=7,align="center",width=[0.8,0.5])
plt.title(f"Shop data FPS informations , FPS = {FPS_shop_unique[0]} and {FPS_shop_unique[1]} ")
plt.subplot(1,2,2)
plt.bar(FPS_non_unique,counts_non,color=["skyblue","#19ab98"],
        edgecolor="black",linewidth=7,align="center",width=[0.8,0.5])
plt.title(f"non-Shop data FPS information , FPS = {FPS_non_unique[0]} and {FPS_non_unique[1]}")
plt.show()
    

