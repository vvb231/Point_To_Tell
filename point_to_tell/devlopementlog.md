#development log



----
Date: 2019-01-04
Author:wenjun

The point to tell is implemented by two parts:

1.finger detection
the basic idea is to filter the contour of human hand by the color of human skin,
then find the tips of finger with corner detection.
choose the highest(smallest y) one as the designated one.

2.object detection and depth computation
implemented by Yolov3 and Zed SDK.


How to choose the object pointed to?
we detect the finger on each frame the camera captured, if no finger is detected,save the current frame;
Otherwise, do the object detection on the frame saved, and return the classification and distance of the 
object in the current frame.


To-Do:
1.finger detection is fragile in the current one, needs to be more stable and precise in the next version.

2.do not need to return results for each frame(otherwise it will be too frequently for the user)

3.voice output of detected result.

----
Date: 2019-01-08
Author:wenjun

fingerdetection:

1.use HSV function to seperate hand from backgroundcolor


