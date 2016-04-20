#!/usr/bin/env python

import rospy
import random

#from std_msgs.msg import String
from trollnode.msg import Expression
import sys

#question, expr = "", ""
pub = ""
def talker(speech, express):#speech):
	if express == "": express = talk_random_expression()
	speak(speech, express)


def talk_random_expression():
	expr = ["happy", "angry", "smile", "sad", "disgust", "surprise", "fear", "suspicios",
		"blink", "pain", "duckface"]
	#talker(speech, expr[random.randint(0, len(expr)-1)])
	return random.choice(expr)

#def talk_default_expression(speech):
#	talker(speech, "happy")


def createPub():
	try:
		global pub
		pub = rospy.Publisher('trollExpression', String, queue_size=10)
		rospy.init_node('talker', anonymous=True)
		#talker(pub)
	
		#talker(0)#rospy.myargv(argv=sys.argv)[0])
	except rospy.ROSInterruptException:
		pass

