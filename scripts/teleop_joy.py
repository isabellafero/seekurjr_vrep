#!/usr/bin/env python
import rospy
import roslib

#imports de mensagens
from seekur_jr.msg import *
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class controlerobo():
	def __init__ (self):
		self.velocity_publisher = rospy.Publisher('seekur_jr/cmd_vel', Twist, queue_size=10)
		rospy.Subscriber('joy',Joy,self.joy_callback)
		
		rospy.spin()
	'''
			//Splitting the joystick buttons
			joy.axes[0];	//Left analog: Horizontal axis
			joy.axes[1];	//Left analog: Vertical axis
			joy.axes[3];	//Right analog: Horizontal axis
			joy.axes[4];	//Right analog: Vertical Axis
			joy.axes[5];	//Right digital Horizontal
			joy.axes[6];	//Left digital Vertical
			
			//buttons seems as a play-station joystick
			joy.buttons[0];	//A button
			joy.buttons[1];	//B button
			joy.buttons[2];	//X button
			joy.buttons[3];	//Y button
			joy.buttons[4];	//L1 button
			joy.buttons[5];	//R1 button
			joy.buttons[6];	//Select button
			joy.buttons[7];	//Start button
		uttons[1];		'''

	def joy_callback(self, joy):
		vel_msg=Twist()
		max_lx=joy.axes[5]*0.6
		max_az=joy.axes[5]*0.8
		vel_msg.linear.x=joy.axes[1]*max_lx

		'''if abs(joy.axes[0]>0.9) and abs(joy.axes[1])<0.2:
			vel_msg.linear.x=0
			vel_msg.angular.z=joy.axes[0]*max_az
			print(vel_msg.angular.z)
			self.velocity_publisher.publish(vel_msg)'''

		#vel_msg.linear.x = joy.axes[1]*max_lx
		#vel_msg.angular.z = joy.axes[0]*1
		


if __name__ == '__main__':
	#Inicializa o nosso no com o nome
	rospy.init_node('seekur_joy',anonymous=True)
	try:
		controlerobo()
	except rospy.ROSInterruptException:
		pass
