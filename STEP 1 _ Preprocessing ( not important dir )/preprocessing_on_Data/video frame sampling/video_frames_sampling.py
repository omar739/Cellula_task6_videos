#------------------------------
import os 
import numpy as np
import cv2
import time
#------------------------------
path = "D:/DEEP Leaning dataset/shop videos/Shop DataSet/test_frames_sampling"
videos = os.listdir(path)
start = time.time()
for i in range(len(videos)) :
    video_path = os.path.join(path,videos[i])
    video  = cv2.VideoCapture(video_path)
    #---------------------------------------------------------
    # Get videos information ( width , height , frames , FPS )
    #---------------------------------------------------------
    width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = video.get(cv2.CAP_PROP_FPS)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Before :  ",[width,height,fps,frames])
    #-----------------------------------------------
    # Change ( FPS = 25 ) ( number_of_frames = 70 )
    #-----------------------------------------------
    FPS = 25
    path_of_save = os.path.join(path,"edited_"+videos[i])
    out_video = cv2.VideoWriter(path_of_save, cv2.VideoWriter_fourcc(*'mp4v'), 
                                FPS , isColor=True, frameSize=(width,height))
    step = int(frames /70)
    frame_index = 0
    frame_Written = 0
    while video.isOpened() and frame_Written < 70 :
        video.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret , frame = video.read()
        if not ret :
            break
        out_video.write(frame)
        frame_index += step
        frame_Written +=1
    out_video.release()
    video.release()
end = time.time()
print(f"Done in {end-start} sec")
for i in range(len(videos)) :
    video_path = os.path.join(path,"edited_"+videos[i])
    video  = cv2.VideoCapture(video_path)
    #---------------------------------------------------------
    # Get videos information ( width , height , frames , FPS )
    #---------------------------------------------------------
    width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = video.get(cv2.CAP_PROP_FPS)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Before :  ",[width,height,fps,frames])