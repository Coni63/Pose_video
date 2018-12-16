import os
import imageio
import cv2

from variable import *

img_list = [os.path.join(img_path_final, name) for name in os.listdir(img_path_final) if os.path.isfile(os.path.join(img_path_final, name))]
n_images = len(img_list)
out_size = imageio.imread(img_list[0]).shape
images = []
for i in range(0, 125, 5):
    img_path = os.path.join(img_path_final,"{}.jpg".format(i))
    frame = imageio.imread(img_path)
    images.append(frame)

imageio.mimsave('movie.gif', images, duration = 0.2)