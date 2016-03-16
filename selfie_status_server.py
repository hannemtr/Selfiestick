#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
from beginner_tutorials.srv import *
import rospy
import SelfieScript as TAS

def handle_selfie_status(req):
	if req.a == 1:
		print "Taking a selfie!"
		TAS.main()
		print "Running script %s"%(req.a)
		print "Returning 1"
		return StatusResponse(1)
	else:
		print "Returning %s"%(req.a)
		return StatusResponse(0)


def selfie_status_server():
    rospy.init_node('selfie_status_server')
    s = rospy.Service('selfie_status', Status, handle_selfie_status)
    print "Waiting for a selfie..."
    rospy.spin()

if __name__ == "__main__":
    selfie_status_server()
