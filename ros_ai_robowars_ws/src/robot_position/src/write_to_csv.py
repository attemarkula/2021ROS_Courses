#!/usr/bin/python3

import rospy, random, math, message_filters
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range
from std_srvs.srv import Empty
import angles
import csv
from tf.transformations import euler_from_quaternion

class Robot_position:
    def __init__(self):
        self.node = rospy.init_node("position_from_ultrasonic")
        self.reset_simulation_call = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)

        self.us1_sub = message_filters.Subscriber('/ultrasonic1',Range)
        self.us2_sub = message_filters.Subscriber('/ultrasonic2',Range)
        self.us3_sub = message_filters.Subscriber('/ultrasonic3',Range)
        self.us4_sub = message_filters.Subscriber('/ultrasonic4',Range)
        self.us5_sub = message_filters.Subscriber('/ultrasonic5',Range)
        self.us6_sub = message_filters.Subscriber('/ultrasonic6',Range)
        self.odom_sub = message_filters.Subscriber('/robot1/odom',Odometry)

        self.subs = message_filters.ApproximateTimeSynchronizer([ self.us1_sub, self.us2_sub, self.us3_sub, self.us4_sub, self.us5_sub, self.us6_sub, self.odom_sub ],queue_size=1,slop=0.6, allow_headerless=True)
        self.subs.registerCallback(self.sensor_callback)
        
        self.positions_file = open('robots_positions.csv',mode='w')
        self.positions_writer = csv.writer(self.positions_file, delimiter=',')
        
        self.reset_counter = 0
        self.write_to_csv_counter = 0



    def sensor_callback(self, us1_sub, us2_sub, us3_sub, us4_sub, us5_sub, us6_sub, odom_sub):
        self.reset_counter+=1
        self.write_to_csv_counter +=1

        orientation_in_quaternions = (
        odom_sub.pose.pose.orientation.x,
        odom_sub.pose.pose.orientation.y,
        odom_sub.pose.pose.orientation.z,
        odom_sub.pose.pose.orientation.w)
        
        orientation_in_euler = euler_from_quaternion(orientation_in_quaternions)
        
        roll = orientation_in_euler[0]
        pitch = orientation_in_euler[1]
        yaw = orientation_in_euler[2]

        yaw_in_radians=angles.normalize_angle_positive(yaw)
        
        ground_truth_x = odom_sub.pose.pose.position.x
        ground_truth_y = odom_sub.pose.pose.position.y

        if self.write_to_csv_counter > 19:
            self.positions_writer.writerow([yaw,us1_sub.range,us2_sub.range,us3_sub.range,us4_sub.range,us5_sub.range,us6_sub.range,ground_truth_x,ground_truth_y])
            self.write_to_csv_counter = 0

        if self.reset_counter > 10000:
                self.reset_simulation_call()
                self.reset_counter = 0

if __name__ == "__main__":
    print("start write_to_csv")
    rbot= Robot_position()
    print("Robot_position "+str(rbot))
    rospy.spin()
                
