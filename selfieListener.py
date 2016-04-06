#!/usr/bin/env python
import rospy
import SelfieScript as SS
from std_msgs.msg import String

def callback(data):
    # Call seflie script
    print "Running selfie script..."
    SS.main()

def listener():
    rospy.init_node('selfielistener', anonymous=True)
    rospy.Subscriber("selfie", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
