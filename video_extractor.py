import cv2

from variable import *

vid = cv2.VideoCapture(original_video_path)

index = 0
while (True):
    ret, frame = vid.read()

    if not ret:  # if we still have images in the video
        break

    name = img_path_raw + "{}.jpg".format(index)
    cv2.imwrite(name, frame)

    index += 1