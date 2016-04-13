#!/usr/bin/env python

import rospy
import random
from trollnode.msg import Expression

def talker(speech, expression):
	pub = rospy.Publisher('speaker', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	#TODO fix .msg!!
	expr_msg = Expression()
	expr_msg.expression = expression
	expr_msg.speech = speech
	pub.publish(expr_msg)

def talk_random_expression(speech):
	expr = ["happy", "angry", "smile", "sad", "disgust", "surprise", "fear", "suspicios",
		"blink", "pain", "duckface"]
	talker(speech, expr[random.randint(0, len(expr)-1)])

def talk_default_expression(speech):
	talker(speech, "happy")

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

