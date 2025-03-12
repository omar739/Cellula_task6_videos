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
# Get Size of each video in bytes
#--------------------------------------------------------------
size_Shop = []
for i in range(len(videos_paths_shop)) :
    path_of_video = os.path.join(path_shop,videos_paths_shop[i])
    size_Shop.append(os.path.getsize(path_of_video)/(1024*1024))
size_non = []
for i in range(len(videos_paths_nonshop)) :
    path_of_video = os.path.join(path_nonshop,videos_paths_nonshop[i])
    size_non.append(os.path.getsize(path_of_video)/(1024*1024))
#----------------------------------------------------------------------
# Visualization of mean , max , min ( size of videos ) for each class
#----------------------------------------------------------------------
FPS_non , FPS_shop = np.array(size_non) , np.array(size_Shop)
max_shop , max_non , min_shop , min_non , mean_shop , mean_non = np.max(FPS_shop),np.max(FPS_non),np.min(FPS_shop),np.min(FPS_non),np.mean(FPS_shop),np.mean(FPS_non)
plt.style.use("dark_background")
plt.figure(figsize=(20,5))
plt.subplot(1,3,1)
plt.bar(["Shop","Non-shop"],[max_shop,max_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Max size with MB in RAM")

plt.subplot(1,3,2)
plt.bar(["Shop","Non-shop"],[min_shop,min_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Min size with MB in RAM")

plt.subplot(1,3,3)
plt.bar(["Shop","Non-shop"],[mean_shop,mean_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Mean size with MB in RAM")

plt.show()