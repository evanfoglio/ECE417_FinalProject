#!/usr/bin/python3
import rospy
import cv2
from std_msgs.msg import String


def callback(data):
    #once we have the image in here, we can error check to see if theres a checker board or not

    rospy.loginfo(rospy.get_caller_id() + "Oh boy, Garbage: ", str(data))
    

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/camera/image_raw", String, callback)

    rospy.spin()


if '__name__' == '__main__':
    listener()







