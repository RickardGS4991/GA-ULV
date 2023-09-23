#!/usr/bin/env python3
from __future__ import print_function
import math
from interbotix_xs_modules.locobot import InterbotixLocobotXS
 
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 
class image_converter:
   def __init__(self):
 
     self.bridge = CvBridge()
     self.image_sub = rospy.Subscriber("/locobot/camera/color/image_raw",Image,self.callback)

   
   def callback(self,data):
     try:
       cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
     except CvBridgeError as e:
       print(e)
 
     (rows,cols,channels) = cv_image.shape
     
     cv2.imshow("Image window", cv_image)
     cv2.waitKey(3)
 
def main(args):
   ic = image_converter()
   rospy.init_node('image_converter', anonymous=True)
   try:
     rospy.spin()
   except KeyboardInterrupt:
    print("Shutting down")
   cv2.destroyAllWindows()
if __name__ == '__main__':
       main(sys.argv)