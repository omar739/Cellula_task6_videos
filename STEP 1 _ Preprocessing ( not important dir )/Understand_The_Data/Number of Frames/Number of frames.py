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
# Get ToTal Number of Frames
#--------------------------------------------------------------
FPS_shop = []
FPS_non = []
for i in range(len(videos_paths_shop)) :
    path_of_video = os.path.join(path_shop,videos_paths_shop[i])
    video = cv2.VideoCapture(path_of_video)
    FPS_shop.append(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()
print("Done for video paths shop ")
for i in range(len(videos_paths_nonshop)) :
    path_of_video = os.path.join(path_nonshop,videos_paths_nonshop[i])
    video = cv2.VideoCapture(path_of_video)
    FPS_non.append(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()
print("Done for video paths non shop ")
#------------------------------------------------------------------------
# Visualization of mean , max , min ( number of frames ) for each class
#------------------------------------------------------------------------0
print(FPS_non)
FPS_non , FPS_shop = np.array(FPS_non) , np.array(FPS_shop)
max_shop , max_non , min_shop , min_non , mean_shop , mean_non = np.max(FPS_shop),np.max(FPS_non),np.min(FPS_shop),np.min(FPS_non),np.mean(FPS_shop),np.mean(FPS_non)
plt.style.use("dark_background")
plt.figure(figsize=(20,5))
plt.subplot(1,3,1)
plt.bar(["Shop","Non-shop"],[max_shop,max_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Max number of frames")

plt.subplot(1,3,2)
plt.bar(["Shop","Non-shop"],[min_shop,min_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Min Number of frames")

plt.subplot(1,3,3)
plt.bar(["Shop","Non-shop"],[mean_shop,mean_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Mean Number of frames")

plt.show()