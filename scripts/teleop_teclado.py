#!/usr/bin/env python
import rospy
import roslib
#import sys

#imports de mensagens
from keyboard.msg import Key
from geometry_msgs.msg import Twist

#Cria a classe do noo para publicar no motor


class ControleRobo():

	#Metodo criador da classe
	def __init__(self):

		#definindo variaveis
		self.keyUp=0  # 273
		self.keyDown=0  # 274
		self.keyLeft=0  # 276
		self.keyRight=0  # 275

		self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

		rospy.Subscriber('/keyboard/keydown', Key, self.keyDownCallback)
		rospy.Subscriber('/keyboard/keyup', Key, self.keyUpCallback)

		#rospy.spin()

		#Iniciio do comando do robo
		vel_msg=Twist()
		while not rospy.is_shutdown():

			if self.keyUp==1 and self.keyLeft==0 and self.keyRight==0:
				vel_msg.linear.x = 0.6
				vel_msg.angular.z = 0
			elif self.keyDown==1 and self.keyLeft==0 and self.keyRight==0:
				vel_msg.linear.x = -0.6
				vel_msg.angular.z = 0
			elif self.keyUp==1 and self.keyLeft==0 and self.keyRight==1:
				vel_msg.angular.z = -0.4
				vel_msg.linear.x = 0.6
			elif self.keyUp==1 and self.keyLeft==1 and self.keyRight==0:
				vel_msg.angular.z = 0.4
				vel_msg.linear.x = 0.6
			elif self.keyUp==0 and self.keyLeft==0 and self.keyRight==0:
				vel_msg.linear.x = 0
				vel_msg.angular.z = 0
			elif self.keyDown==1 and self.keyLeft==0 and self.keyRight==1:
				vel_msg.linear.x = -0.6
				vel_msg.angular.z = 0.8
			elif self.keyDown==1 and self.keyLeft==1 and self.keyRight==0:
				vel_msg.linear.x = -0.6
				vel_msg.angular.z = -0.8
			elif self.keyDown==0 and self.keyUp==0 and self.keyLeft==0 and self.keyRight==1:
				vel_msg.angular.z = -0.8
				vel_msg.linear.x = 0
			elif self.keyDown==0 and self.keyUp==0 and self.keyLeft==1 and self.keyRight==0:
				vel_msg.angular.z = 0.8
				vel_msg.linear.x = 0

			self.velocity_publisher.publish(vel_msg)

	#Funcao que recebe o topico key down
	def keyDownCallback(self, data):
		print(data.code)

		if data.code==273 and self.keyUp==0:
			self.keyUp=1

		if data.code==274 and self.keyDown==0:
			self.keyDown=1

		if data.code==275 and self.keyRight==0:
			self.keyRight=1

		if data.code==276 and self.keyLeft==0:
			self.keyLeft=1

	#Funcao que recebe o topico do key up
	def keyUpCallback(self, data):
		print(data.code)

		if data.code==273 and self.keyUp==1:
			self.keyUp=0

		if data.code==274 and self.keyDown==1:
			self.keyDown=0

		if data.code==275 and self.keyRight==1:
			self.keyRight=0

		if data.code==276 and self.keyLeft==1:
			self.keyLeft=0

#Funcao main que chama a classe criada


if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('controle_teclado', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		ControleRobo()
	except rospy.ROSInterruptException:
		pass
