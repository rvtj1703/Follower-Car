#!/usr/bin/env python

#Importing rospy library and Int32 library
import rospy
from std_msgs.msg import Int32

#Intialising valraibles to zero
pirFront_data = 0
pirLeft_data = 0
pirRight_data = 
ultrasonic_data = 0

#Creating callback function to fetch the status of front PIR sensor
def callbackFrontPIRSensor(data):
    global pirFront_data
    pirFront_data = data.data
    print("Front PIR sensor reading: " + str(pirFront_data))

#Creating callback function to fetch the status of left PIR sensor
def callbackLeftPIRSensor(data):
    global pirLeft_data
    pirLeft_data = data.data
    print("Left PIR sensor reading: " + str(pirLeft_data))

#Creating callback function to fetch the status of right PIR sensor
def callbackRightPIRSensor(data):
    global pirRight_data
    pirRight_data = data.data
    print("Right PIR sensor reading: " + str(pirRight_data))

#Creating callback function to fetch the status of ultrasonic sensor
def callbackUltrasonicSensor(data):
    global ultrasonic_data
    ultrasonic_data = data.data
    print("Ultrasonic sensor reading: " + str(ultrasonic_data))
    
if __name__ == '__main__':

    #Initialising ros node
    rospy.init_node('robot_controller', anonymous=True)

    rate = rospy.Rate(10) # 10hz

    #Creating Subscribers for all sensors
    rospy.Subscriber("pirFront", Int32, callbackFrontPIRSensor)
    rospy.Subscriber("pirLeft", Int32, callbackLeftPIRSensor)
    rospy.Subscriber("pirRight", Int32, callbackRightPIRSensor)
    rospy.Subscriber("ultrasonic", Int32, callbackUltrasonicSensor)

    #Creating publishers for channel A and channel B motor speeds
    channelA_speed_publisher = rospy.Publisher('speedChannelA', Int32, queue_size=10)
    channelB_speed_publisher = rospy.Publisher('speedChannelB', Int32, queue_size=10)
	

    while not rospy.is_shutdown():

        #Based on status for which PIR sensor is high, motor speeds are set for both the channels
	if(1 == pirFront_data):
            motor_speed_channelA = 124
            motor_speed_channelB = 124 
        elif(1 == pirLeft_data):
            motor_speed_channelA = 184
            motor_speed_channelB = 0
        elif(1 == pirRight_data):
            motor_speed_channelA = 0
            motor_speed_channelB = 184
        else:
            motor_speed_channelA = 0
            motor_speed_channelB = 0

        #Publishing channel A and channel B motor speeds to arduino    
	channelA_speed_publisher.publish(motor_speed_channelA)
	channelB_speed_publisher.publish(motor_speed_channelB)
	
	
	rate.sleep()
