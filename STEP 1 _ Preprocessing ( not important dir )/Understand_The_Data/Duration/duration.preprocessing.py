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
# Get Duration of videos ( duration =  Total Frames / FPS )
#--------------------------------------------------------------
Duration_shops = []
for i in range(len(videos_paths_shop)) :
    path_of_video = os.path.join(path_shop,videos_paths_shop[i])
    video = cv2.VideoCapture(path_of_video)
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    Duration_shops.append(total_frames/fps)
    video.release()
Duration_non = []
for i in range(len(videos_paths_nonshop)) :
    path_of_video = os.path.join(path_nonshop,videos_paths_nonshop[i])
    video = cv2.VideoCapture(path_of_video)
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    Duration_non.append(total_frames/fps)
    video.release()
#----------------------------------------------------------------
# Visualization of Duration mean
#----------------------------------------------------------------
Duration_mean_shop , Duration_mean_non = np.mean(np.array(Duration_shops)) , np.mean(np.array(Duration_non ))
plt.style.use("dark_background")
plt.bar(["Shop","Non-shop"],[Duration_mean_shop,Duration_mean_non],
        color=["skyblue","Green"],edgecolor="black",linewidth=8)
plt.title("Duration mean for each class")
plt.show()