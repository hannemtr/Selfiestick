#!/usr/bin/env python

import sys
import rospy
import roslib; roslib.load_manifest('beginner_tutorials')
from beginner_tutorials.srv import *

def selfie_status_client(a):
    rospy.wait_for_service('selfie_status')
    try:
        status = rospy.ServiceProxy('selfie_status', Status)
        resp1 = status(a)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    a = 0
    if len(sys.argv) == 2:
        a = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(a)
    print "%s = %s"%(a, selfie_status_client(a))
