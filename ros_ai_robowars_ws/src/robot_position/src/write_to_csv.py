#!/usr/bin/python3

import rospy, random, math, message_filters
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range
from sensor_msgs.msg import Imu
from std_srvs.srv import Empty
import angles
import csv
from tf.transformations import euler_from_quaternion
import time

# tiedoston nimi : "päiväys-odometry/imu/"
filename_prefix = "db_" +str(time.strftime("%Y%M%d%H%M%S", time.localtime())) + "_"

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
        self.imu_sub = message_filters.Subscriber('/robot1/imu',Imu)

        self.subs = message_filters.ApproximateTimeSynchronizer([ self.us1_sub, self.us2_sub, self.us3_sub, self.us4_sub, self.us5_sub, self.us6_sub, self.odom_sub, self.imu_sub ],queue_size=1,slop=0.6, allow_headerless=True)
        self.subs.registerCallback(self.sensor_callback)
        
        #myöhempi versio missä järkevämpi tapa lähettää kentät.
        self.positions_file = open(filename_prefix+'robots_positions.csv',mode='w')
        self.csv_fieldnames=['us1_sub.range','us2_sub.range','us3_sub.range','us4_sub.range','us5_sub.range','us6_sub.range','odom_yaw','imu_yaw','odom_pitch','imu_pitch','odom_roll','imu_roll','odom_truth_x','odom_truth_y']

        self.positions_writer = csv.DictWriter(self.positions_file,fieldnames=self.csv_fieldnames)
        self.positions_writer.writeheader()
        self.positions_file.flush()
        self.positions_file_writecounter = 0

        self.reset_counter = 0
        self.write_to_csv_counter = 0

    def sensor_callback(self, us1_sub, us2_sub, us3_sub, us4_sub, us5_sub, us6_sub, odom_sub, imu_sub):
        #print("debug:sensor_callback()")
        self.reset_counter = self.reset_counter+1
        self.write_to_csv_counter +=1

        orientation_in_quaternions = (
        odom_sub.pose.pose.orientation.x,
        odom_sub.pose.pose.orientation.y,
        odom_sub.pose.pose.orientation.z,
        odom_sub.pose.pose.orientation.w)

        orientation_in_euler = euler_from_quaternion(orientation_in_quaternions)
        odom_roll = orientation_in_euler[0]
        odom_pitch = orientation_in_euler[1]
        odom_yaw = orientation_in_euler[2]
        odom_yaw_in_radians=angles.normalize_angle_positive(odom_yaw)

        odom_truth_x = odom_sub.pose.pose.position.x
        odom_truth_y = odom_sub.pose.pose.position.y

        #Helppo. Tunnilla tehdyssä esimerkissä käytimme odmometria topicin asentotietoa, 
        # parempi kuitenkin olisi käyttää /robot1/imu tietoa. 
        # Muuta datan tallennus nodea, niin että se käyttää orientaatio datana imu tietoa.
        orientation_in_quaternions = (
        imu_sub.orientation.x,
        imu_sub.orientation.y,
        imu_sub.orientation.z,
        imu_sub.orientation.w)
        orientation_in_euler = euler_from_quaternion(orientation_in_quaternions)
        imu_roll = orientation_in_euler[0]
        imu_pitch = orientation_in_euler[1]
        imu_yaw = orientation_in_euler[2]
        imu_yaw_in_radians=angles.normalize_angle_positive(imu_yaw)

        #print("debug:",str(self.reset_counter))
        #print(odom_truth_x, odom_truth_y)
        #print(imu_sub.orientation.x, imu_sub.orientation.y)

        if self.write_to_csv_counter > 19:
            print("write line and flush") 
            print("Writing line", self.positions_file_writecounter)
            self.positions_file_writecounter += 1
            self.write_to_csv_counter = 0
            self.positions_writer.writerow({
                'us1_sub.range': us1_sub.range,
                'us2_sub.range': us2_sub.range,
                'us3_sub.range': us3_sub.range,
                'us4_sub.range': us4_sub.range,
                'us5_sub.range': us5_sub.range,
                'us6_sub.range': us6_sub.range,
                'odom_yaw': odom_yaw,
                'imu_yaw': imu_yaw,
                'odom_pitch': odom_pitch,
                'imu_pitch': imu_pitch,
                'odom_roll': odom_roll,
                'imu_roll': imu_roll,
                'odom_truth_x': odom_truth_x,
                'odom_truth_y': odom_truth_y
            }) #Huom. tämä sisältää kaikki tiedot, mutta täytetään vain tehtävän kirjain, niin poistetaan odom sarakkeet tallennuksesta. 
            # Kerätään tupla pitch, roll, yaw, jotta verrataan virheen määrää myöhemmin ohjelmalla, tai käsin.
            self.positions_file.flush()
        # resetissä ratkaisematon ongelma
        # katkaisee csv tulostuksen, koska kello nollaantuu resetissä.
#        if self.reset_counter > 10000:
#            # maybe this breaks ApproximateTimeSynchronizer
#            self.reset_simulation_call()
#            self.reset_counter = 0

if __name__ == "__main__":
    print("start write_to_csv")
    rbot= Robot_position()
    print("Robot_position "+str(rbot))

    #time.sleep(20)
    #print("20seconds done, exiting.")

    rospy.spin()
