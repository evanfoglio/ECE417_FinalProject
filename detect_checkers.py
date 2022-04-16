#!/usr/bin/python3
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import time
from matplotlib import pyplot as plt
from PIL import Image as im
from threading import Thread


#This function is called everytime an image
#is published to the "camera/image_raw/" topic
def callback(data):
    global i
    if(i == 20):
        i = 1
        print("Checking...")
        img = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        #Attempt to find checkerboard corners, ret = 1 if successful
        ret, corners = cv2.findChessboardCorners(img, (7,7), None)
        # If a checker board is detected, 
        if ret == True:
            print("Found First Checkerboard")
            start_point = corners[0][0]
            end_point = corners[-1][0] 
            start_point = [int(start_point[0]), int(start_point[1])]
            end_point = [int(end_point[0]), int(end_point[1])]
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_copy = img.copy()
            color = [0, 0, 0]
            
            img2 = cv2.rectangle(img, start_point, end_point, color, -1)

            ret, corners2 = cv2.findChessboardCorners( img2, (7,7), None)

            if ret == True:
                print("Found Second Checkerboard")
                show_img(img_copy, corners, corners2)
            else:
                print("Second Board Not Found")

    else:
        i = i + 1

def show_img(img, corners, corners2):
    x = []
    y = []
    x1 = []
    y1 = []
    plt.imshow(img, interpolation='nearest')
    for xy in corners:
        x.append(xy[0][0])
        y.append(xy[0][1])
    for xy in corners2:
        x1.append(xy[0][0])
        y1.append(xy[0][1])
    #plot coordinates on top of image
    plt.scatter(x, y, color='blue')
    plt.scatter(x1, y1, color='green')
    plt.show()



# example checkerboard detecton line:
# Find the chess board corners
# ret, corners = cv.findChessboardCorners(gray, (7,6), None)
# Full code example: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
# Documentation on the function: https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga93efa9b0aa890de240ca32b11253dd4a

def listener():
    rospy.init_node('listener', anonymous=True)
    #subscribe to image node
    rospy.Subscriber("/camera/image_raw", Image, callback)
    #wait for callbacks
    rospy.spin()
i = 1
bridge = CvBridge() 
print("Bout to listen")
listener()







