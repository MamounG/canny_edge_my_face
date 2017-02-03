#!/usr/bin/env python
import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
#from matplotlib import pyplot as plt

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("edge_image",Image, queue_size=1)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
      
    edge = cv2.Canny(cv_image,50,150)
    
    vis = (cv_image.copy())
    vis = np.uint8(vis/2.)
    vis[edge != 0] = (255, 255, 255)

    #cv2.imshow('edge', vis)
    #cv2.waitKey(3)
    try:
      msg = self.bridge.cv2_to_imgmsg(vis, "passthrough")
    except CvBridgeError as e:
      print(e)

    msg.header.frame_id = "map"

    self.image_pub.publish(msg)

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
