#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import  Imu
import math
from std_msgs.msg import Float32


# 현재의 orientation 정보를 얻어 오는 IMU 콜백 함수
def getIMU( data):
    global pu
    qx=data.orientation.x
    qy=data.orientation.y
    qz=data.orientation.z
    qw=data.orientation.w
    heading=-math.atan2(2.0*(qw*qz+qx*qy), 1.0-2.0*(qy*qy+qz*qz))
    heading_deg= heading*180/math.pi
    print "yaw(deg)",heading_deg

    pub.publish(heading_deg)

rospy.init_node("heading", anonymous=False)
pub = rospy.Publisher("heading",Float32,queue_size= 1)
rospy.Subscriber("/imu/imu", Imu, getIMU)
rospy.spin()

