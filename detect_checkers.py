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

#This function is called everytime an image
#is published to the "camera/image_raw/" topic
def callback(data):

    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
    
    #Attempt to find checkerboard corners, ret = 1 if successful
    ret, corners = cv2.findChessboardCorners(img, (6,6), None)
    # If a checker board is detected, 
    if ret == True:
        #define arrays to hold xy coordinates
        x = []
        y = []
        
        print("Found checkers")
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #plot the image
        plt.imshow(img, interpolation='nearest')


        # pull the individual coordinates from the 
        # return value of findChessboard
        for xy in corners:
            x.append(xy[0][0])
            y.append(xy[0][1])
        #plot coordinates on top of image
        plt.scatter(x, y, color='blue')
        #display image
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

if __name__ == '__main__':
    
    listener()







