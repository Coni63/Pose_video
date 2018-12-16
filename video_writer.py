import cv2
import os

from variable import *

img_list = [os.path.join(img_path_final, name) for name in os.listdir(img_path_final) if os.path.isfile(os.path.join(img_path_final, name))]
n_images = len(img_list)
out_size = cv2.imread(img_list[0]).shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_without_sound, fourcc, fps, (out_size[1], out_size[0]))


for i in range(n_images):
    img_path = os.path.join(img_path_final,"{}.jpg".format(i))
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()