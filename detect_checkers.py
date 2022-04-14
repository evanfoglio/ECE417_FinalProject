#!/usr/bin/python3
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import time
from matplotlib import pyplot as plt



def callback(data):
    #once we have the image in here, we can error check to see if theres a checker board or not

    #rospy.loginfo(rospy.get_caller_id() + " This will display to terminal ")

    print("type of original data: " + str(type(data)))
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
    
    #debug print statements
    print("Type of img: " + str(type(img)))
    print("img shape: " + str(img.shape)) 
   

    #Currently displays 1 frame at a time and
    # waits for the previous frome to be closed 
    # before it grabs the next frame

    #show image
    plt.imshow(img, interpolation='nearest')
    plt.show()

    #time.sleep(5)

def listener():
    rospy.init_node('listener', anonymous=True)
    #subscribe to image node
    rospy.Subscriber("/camera/image_raw", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    
    listener()







