#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32


import os
from gps import *
from time import *
import time
import threading

gpsd = None


class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info


    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer



    
def gpsStream():
    gpsp.start() 
    pub = rospy.Publisher('position_info', Float32, queue_size=10)
    rospy.init_node('gps_streamer', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(gpsd.fix.latitude)
        pub.publish(gpsd.fix.latitude)
        rate.sleep()
    gpsp.running = False
    gpsp.join()


if __name__ == '__main__':
    gpsp = GpsPoller()
    try:
        gpsStream()

    except rospy.ROSInterruptException:
        pass
