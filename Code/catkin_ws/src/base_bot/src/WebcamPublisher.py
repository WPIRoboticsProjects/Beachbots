#! /usr/bin/env python
# ==============================================================================
# title           :WebcamPublisher.py
# description     :Node to publish opencv data to required topic for apriltag detection
# author          :James Casella
# date            :2021-11-16
# version         :0.1
# notes           :
# python_version  :3.8
# ros parameters  : 
# ==============================================================================
import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np
import sys
from cv_bridge import CvBridge, CvBridgeError

def webcam_pub():
    pub = rospy.Publisher('/camera_rect/image_rect', Image, queue_size=1)
    rospy.init_node('webcam_pub', anonymous=True)
    rate = rospy.Rate(60) # 60hz

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        sys.stdout.write("Webcam is not available")
        return -1

    while not rospy.is_shutdown():
        ret, frame = cam.read()
        bridge = CvBridge()
        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        if ret:
            rospy.loginfo("Capturing image")

        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        webcam_pub()
    except rospy.ROSInterruptException:
        pass