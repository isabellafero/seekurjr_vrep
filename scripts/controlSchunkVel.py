#!/usr/bin/env python
import rospy
import roslib
import math
import time
#import sys

#================ SCHUNK LWA 4P JOINT LIMITS ========================================

# Velocity limits
# Joints 1 to 6: 72 deg/s (1.25664 rad/s)

# Range limits
# Joint 1: -170 deg to +170 deg
# Joint 2: -170 deg to +170 deg
# Joint 3: -155.5 deg to +155;5 deg
# Joint 4: -170 deg to +170 deg
# Joint 5: -170 deg to +170 deg
# Joint 6: -170 deg to +170 deg

#====================================================================================


# Imports de messages
from geometry_msgs.msg import Twist


# Creating the class of the node that will publish on the joints
class ControlSchunk():

																																																																# Class creation method
	def __init__(self):

																																																																# Sending information to the user
		rospy.loginfo("Schunk LWA 4P control node initialized")

		# Variable that contains the current joint velocities in rad/s
		self.jointVel = [0 for x in range(6)]

		# Variable that contains the velocity commands to be sent to the joints (in deg/s)
		jointCommand = [0 for x in range(6)]

		# Variable that contains the velocity commands to be sent to the joints (in rad/s)
		jointCommandRad = [0 for x in range(6)]

		# Creating the ROS publishers and subscribers
		self.pub = rospy.Publisher('/vrep_ros_interface/SCHUNKLWA4P/joints', Twist, queue_size=1)
		# rospy.Subscriber('/vrep_ros_interface/SCHUNKLWA4P/jointsCurrentVel',joints,self.jointsVelCallback)
		# rospy.spin()

#====================================================================================================
		# ROBOT CONTROL LOOP
#====================================================================================================
		# while not rospy.is_shutdown():

		# Joint velocity commands [deg/s]
		jointCommand[0] = -2
		jointCommand[1] = -2
		jointCommand[2] = -2
		jointCommand[3] = 2
		jointCommand[4] = 2
		jointCommand[5] = 2

		print("\nJoint Commands [deg/s]: ")
		print(jointCommand)

		# Converts the values to radians
		i = 0
		for x in jointCommand:
			jointCommandRad[i] = math.radians(x)
			i += 1

		print("\nJoint Commands [rad/s]:")
		print(jointCommandRad)
		print("\n----------------------------")

		for y in range(3):
			self.applyJointCommand(jointCommandRad)
			time.sleep(3)

		i = 0
		for x in jointCommand:
			jointCommandRad[i] = 0
			i += 1
		self.applyJointCommand(jointCommandRad)

#====================================================================================================

	# Function called when a new message is published in the joint velocity topic
	def jointsVelCallback(self, data):

		self.jointVel[0] = data.linear.x
		self.jointVel[1] = data.linear.y
		self.jointVel[2] = data.linear.z
		self.jointVel[3] = data.angular.x
		self.jointVel[4] = data.angular.y
		self.jointVel[5] = data.angular.z

	# Function that publishes a velocity value to the joints
	def applyJointCommand(self, data):

		# Variable that receiver the commands to be sent to the joints
		commandPub = Twist()

		commandPub.linear.x = data[0]
		commandPub.linear.y = data[1]
		commandPub.linear.z = data[2]
		commandPub.angular.x = data[3]
		commandPub.angular.y = data[4]
		commandPub.angular.z = data[5]

		# Publishing the commands
		self.pub.publish(commandPub)


# Function that calls the class
if __name__ == '__main__':

	# Initiliazes the node
	rospy.init_node('controlSchunkVel', anonymous=True)

	# Instances the class and starts an error treatment regimen
	try:
		obj_no = ControlSchunk()
	except rospy.ROSInterruptException:
		pass
