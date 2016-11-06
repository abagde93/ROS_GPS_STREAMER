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

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      pub = rospy.Publisher('position_info', Float32, queue_size=10)
      rospy.init_node('gps_streamer', anonymous=True)
      pub.publish(gpsd.fix.latitude)


  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."

