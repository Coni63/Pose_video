'''
All code is highly based on Ildoo Kim's code (https://github.com/ildoonet/tf-openpose)
and derived from the OpenPose Library (https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE)
'''

import os
import cv2
import numpy as np
import glob
import gc

import tensorflow as tf
from tensorflow.core.framework import graph_pb2

from variable import *
from common import estimate_pose, draw_humans, read_imgfile

tf.reset_default_graph()

graph_def = graph_pb2.GraphDef()
# Download model from https://www.dropbox.com/s/2dw1oz9l9hi9avg/optimized_openpose.pb
with open(mdl_path, 'rb') as f:
    graph_def.ParseFromString(f.read())
tf.import_graph_def(graph_def, name='')

inputs = tf.get_default_graph().get_tensor_by_name('inputs:0')
heatmaps_tensor = tf.get_default_graph().get_tensor_by_name('Mconv7_stage6_L2/BiasAdd:0')
pafs_tensor = tf.get_default_graph().get_tensor_by_name('Mconv7_stage6_L1/BiasAdd:0')

with tf.Session() as sess:
    for imgpath in glob.glob(img_path_raw + "*.jpg"):
        basename = os.path.basename(imgpath)
        outpath = img_path_final + basename

        if os.path.exists(outpath):  # in case of crash to not restart from 0
            print("Skipping image \t {}".format(basename))
            continue
        else:
            print("Processing image \t {}".format(basename))

        image = read_imgfile(imgpath, img_width, img_height)

        heatMat, pafMat = sess.run([heatmaps_tensor, pafs_tensor], feed_dict={
            inputs: image
        })

        humans = estimate_pose(heatMat[0], pafMat[0])

        # display
        image = cv2.imread(imgpath)
        image_h, image_w = image.shape[:2]
        image = draw_humans(image, humans)

        scale = 480.0 / image_h
        newh, neww = 480, int(scale * image_w + 0.5)

        image = cv2.resize(image, (neww, newh), interpolation=cv2.INTER_AREA)

        cv2.imwrite(outpath, image)

        gc.collect()