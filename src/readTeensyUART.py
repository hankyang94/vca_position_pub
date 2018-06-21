#!/usr/bin/env python
import sys
import time
import rospy

import serial
import numpy as np
from std_msgs.msg import Float32, Int32
from vca_position_pub.msg import vcaPosition

teensy = serial.Serial('/dev/ttyUSB0', 230400)

pub = rospy.Publisher('/vcaPosition', vcaPosition, queue_size=10)
rospy.init_node('vca_position_pub', anonymous = True)
#~ r = rospy.Rate(2000)
msg = vcaPosition()
voltageScale = 5.0/2**16


while not rospy.is_shutdown():
    #~ print repr(teensy.readline())
    rawRead = teensy.readline().replace('\x00', '').replace('\r', '').replace('\n', '')
    #~ print repr(rawRead)
    if len(rawRead) != 0:
        msg.header.stamp = rospy.Time.now()
        msg.bit = int(rawRead)
        msg.voltage = int(rawRead) * voltageScale
        print msg.voltage
        pub.publish(msg)
        #~ r.sleep()
