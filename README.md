# OpenPose on Video

Based on the great presention from [Medium](https://arvrjourney.com/human-pose-estimation-using-openpose-with-tensorflow-part-2-e78ab9104fc8). I've used the model from [this Repo](https://gist.github.com/alesolano/b073d8ec9603246f766f9f15d002f4f4) and weights from [dropbox](https://www.dropbox.com/s/2dw1oz9l9hi9avg/optimized_openpose.pb) to create a complete pipeline to add the predicted skeleton from OpenPose on a complete video. 
I used _Skibidi_ sound clip and this is the result (click to see the video):

[![movie](https://github.com/Coni63/Pose_video/blob/master/img/193.jpg)](https://www.youtube.com/watch?v=n-5LQMDHrtE)

I used this clip for several reasons :

* There is fast movements
* There is one or more peoples
* There is costumes
* There is animals
* It's a viral video :)


## Prediction Quality

I used a model from 2017 predicting 17 keypoints (eyes, ears, nose, arms, legs, ...). There is multiple other ones existing more accurate, faster or with more keypoints like [this one](https://github.com/CMU-Perceptual-Computing-Lab/openpose) which propose 135 keypoints. I didn't find everytime how to use or weights that's why I used this one. Now in term or succes or fail we can see :

#### Some success
Full body :
![193.jpg](https://github.com/Coni63/Pose_video/blob/master/img/193.jpg)
Partial body of baby doll :
![310.jpg](https://github.com/Coni63/Pose_video/blob/master/img/310.jpg)
Partial body :
![323.jpg](https://github.com/Coni63/Pose_video/blob/master/img/323.jpg)
Full bodies :
![366.jpg](https://github.com/Coni63/Pose_video/blob/master/img/366.jpg)
It works also from back :
![454.jpg](https://github.com/Coni63/Pose_video/blob/master/img/454.jpg)
Partial "cropped" body :
![532.jpg](https://github.com/Coni63/Pose_video/blob/master/img/532.jpg)
Body with complex texture :
![590.jpg](https://github.com/Coni63/Pose_video/blob/master/img/590.jpg)
Body with costume :
![635.jpg](https://github.com/Coni63/Pose_video/blob/master/img/635.jpg)
Monster with "human" skeleton:
![4596.jpg](https://github.com/Coni63/Pose_video/blob/master/img/4596.jpg)

#### Some fail
Missing arm due to constrast :
![319.jpg](https://github.com/Coni63/Pose_video/blob/master/img/319.jpg)
![1361.jpg](https://github.com/Coni63/Pose_video/blob/master/img/1361.jpg)
Costume with too big difference with human skeleton :
![619.jpg](https://github.com/Coni63/Pose_video/blob/master/img/619.jpg)
Complexe texture :
![646.jpg](https://github.com/Coni63/Pose_video/blob/master/img/646.jpg)
Non human detection (the model should skip if it's not human) : 
![719.jpg](https://github.com/Coni63/Pose_video/blob/master/img/719.jpg)
Same image multiple time, different prediction (due to resolution) :
![845.jpg](https://github.com/Coni63/Pose_video/blob/master/img/845.jpg)
1 leg not detected due to texture :
![2872.jpg](https://github.com/Coni63/Pose_video/blob/master/img/2872.jpg)
2 body merged :
![3343.jpg](https://github.com/Coni63/Pose_video/blob/master/img/3343.jpg)

## How to use

The code is now quite simple, you have to create some folders to store raw images and processed images. After you have to enter few parameters into *variable.py*. Once done, just run "create_video.bat".

## Possible improvements

Using other models more recent could be usefull to see how better they performs on previous images. In addition, this models can't be use on videos Live as it is too slow. It required around 20 minutes to render the 3.13 min of clip (4819 images) in a lower resolution (As it is now, it renders images 1 by 1 - like it it was a live video). Having batches may reduce a lot the process and is quite simple to implement. I'll probably add it in a future update. 